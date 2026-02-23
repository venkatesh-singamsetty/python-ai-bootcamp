import os
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, callbacks
import time
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, mean_absolute_error, r2_score
from sklearn.linear_model import LogisticRegression, LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor, GradientBoostingClassifier, GradientBoostingRegressor
from sklearn.svm import SVC, SVR
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.naive_bayes import GaussianNB
from xgboost import XGBClassifier, XGBRegressor

# Environment setup
os.environ['KMP_DUPLICATE_LIB_OK']='True'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

print("--- Data Loading and Preprocessing (WeatherAUS) ---")
# Use a sample for speed if the file is very large, but here we use the full data
df = pd.read_csv('weatherAUS.csv')

# Handling missing values
# For numerical: use median
num_cols = df.select_dtypes(include=[np.number]).columns
imputer_num = SimpleImputer(strategy='median')
df[num_cols] = imputer_num.fit_transform(df[num_cols])

# For categorical: use mode
cat_cols = df.select_dtypes(include=['object']).columns
imputer_cat = SimpleImputer(strategy='most_frequent')
df[cat_cols] = imputer_cat.fit_transform(df[cat_cols])

# Date Preprocessing (Cyclic Engineering)
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day

# Cyclic encoding for month and day
df['Month_Sin'] = np.sin(2 * np.pi * df['Month'] / 12)
df['Month_Cos'] = np.cos(2 * np.pi * df['Month'] / 12)
df['Day_Sin'] = np.sin(2 * np.pi * df['Day'] / 31)
df['Day_Cos'] = np.cos(2 * np.pi * df['Day'] / 31)

df = df.drop(['Date', 'Month', 'Day'], axis=1)

# Categorical Encoding
le = LabelEncoder()
for col in ['Location', 'WindGustDir', 'WindDir9am', 'WindDir3pm', 'RainToday', 'RainTomorrow']:
    df[col] = le.fit_transform(df[col])

# Targets
target_class = 'RainTomorrow'
target_reg = 'MaxTemp'

# Features for Classification
X_class = df.drop([target_class], axis=1).values
y_class = df[target_class].values

# Features for Regression (Excluding MaxTemp)
X_reg = df.drop([target_reg], axis=1).values
y_reg = df[target_reg].values

print(f"Dataset processed. Classification shape: {X_class.shape}, Regression shape: {X_reg.shape}")

# ----- PART 1: CLASSIFICATION SUITE -----
X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(X_class, y_class, test_size=0.2, random_state=42)

sc_c = StandardScaler()
X_train_c = sc_c.fit_transform(X_train_c)
X_test_c = sc_c.transform(X_test_c)

ml_classifiers = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "KNN (5)": KNeighborsClassifier(n_neighbors=5),
    "Naive Bayes": GaussianNB(),
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier(n_estimators=100),
    "Gradient Boosting": GradientBoostingClassifier(),
    "XGBoost": XGBClassifier()
}

class_results = []
print("\n" + "="*60)
print("PART 1: CLASSIFICATION SUITE (Target: 'RainTomorrow')")
print("="*60)

for name, clf in ml_classifiers.items():
    print(f"Training {name}...", end=" ", flush=True)
    start = time.time()
    clf.fit(X_train_c, y_train_c)
    end = time.time()
    y_pred = clf.predict(X_test_c)
    acc = accuracy_score(y_test_c, y_pred)
    class_results.append([name, acc, round(end-start, 4)])
    print("Done.")

# ANN Classifier
print("Training ANN Classifier...", end=" ", flush=True)
ann_c = tf.keras.models.Sequential([
    layers.Input(shape=(X_train_c.shape[1],)),
    layers.Dense(units=32, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(units=16, activation='relu'),
    layers.Dense(units=1, activation='sigmoid')
])
ann_c.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
early_stop = callbacks.EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

start = time.time()
history_c = ann_c.fit(X_train_c, y_train_c, validation_split=0.2, epochs=50, batch_size=32, verbose=0, callbacks=[early_stop])
end = time.time()

y_pred_ann = (ann_c.predict(X_test_c, verbose=0) > 0.5).astype(int)
ann_acc = accuracy_score(y_test_c, y_pred_ann)
class_results.append(["ANN Classifier", ann_acc, round(end-start, 4)])
print("Done.")

# Display Classification Results
class_results.sort(key=lambda x: x[1], reverse=True)
print("\nClassification Comparison (Ranked by Accuracy):")
print(f"{'Algorithm':<25} | {'Accuracy':<10} | {'Time(s)':<8}")
print("-" * 50)
for res in class_results:
    print(f"{res[0]:<25} | {res[1]:<10.4f} | {res[2]:<8}")


# ----- PART 2: REGRESSION SUITE -----
print("\n" + "="*60)
print("PART 2: REGRESSION SUITE (Target: 'MaxTemp')")
print("="*60)

X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)

sc_r = StandardScaler()
X_train_r = sc_r.fit_transform(X_train_r)
X_test_r = sc_r.transform(X_test_r)

ml_regressors = {
    "Linear Regression": LinearRegression(),
    "Ridge Regression": Ridge(),
    "Lasso Regression": Lasso(),
    "Decision Tree Reg": DecisionTreeRegressor(),
    "Random Forest Reg": RandomForestRegressor(n_estimators=100),
    "Gradient Boosting Reg": GradientBoostingRegressor(),
    "XGBoost Reg": XGBRegressor()
}

reg_results = []

for name, reg in ml_regressors.items():
    print(f"Training {name}...", end=" ", flush=True)
    start = time.time()
    reg.fit(X_train_r, y_train_r)
    end = time.time()
    y_pred = reg.predict(X_test_r)
    mae = mean_absolute_error(y_test_r, y_pred)
    r2 = r2_score(y_test_r, y_pred)
    reg_results.append([name, r2, mae, round(end-start, 4)])
    print("Done.")

# ANN Regressor
print("Training ANN Regressor...", end=" ", flush=True)
ann_r = tf.keras.models.Sequential([
    layers.Input(shape=(X_train_r.shape[1],)),
    layers.Dense(units=64, activation='relu'),
    layers.Dense(units=32, activation='relu'),
    layers.Dense(units=1) 
])
ann_r.compile(optimizer='adam', loss='mse', metrics=['mae'])

start = time.time()
history_r = ann_r.fit(X_train_r, y_train_r, validation_split=0.2, epochs=50, batch_size=32, verbose=0, callbacks=[early_stop])
end = time.time()

y_pred_ann_r = ann_r.predict(X_test_r, verbose=0)
ann_r2 = r2_score(y_test_r, y_pred_ann_r)
ann_mae = mean_absolute_error(y_test_r, y_pred_ann_r)
reg_results.append(["ANN Regressor", ann_r2, ann_mae, round(end-start, 4)])
print("Done.")

# Display Regression Results
reg_results.sort(key=lambda x: x[1], reverse=True)
print("\nRegression Comparison (Ranked by R2 Score):")
print(f"{'Algorithm':<25} | {'R2 Score':<10} | {'MAE':<10} | {'Time(s)':<8}")
print("-" * 65)
for res in reg_results:
    print(f"{res[0]:<25} | {res[1]:<10.4f} | {res[2]:<10.2f} | {res[3]:<8}")

print("\nFull ML & ANN Comparison Script Completed for WeatherAUS.")
