import pandas as pd
import numpy as np
import joblib, os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import StandardScaler

# Load
path = os.path.dirname(__file__)
csv_path = os.path.join(path, "car-mpg.csv")
data = pd.read_csv(csv_path).drop("car_name", axis=1)

# --- CLEANING ---
# Convert '?' to NaN and then numeric
data = data.replace('?', np.nan)
for col in data.columns:
    data[col] = pd.to_numeric(data[col], errors='coerce')

# Fill NaNs with Column Median
data = data.fillna(data.median())

# Secondary check: Drop any row that STILL has NaN just in case
data = data.dropna()

# --- PREP ---
# 8 Features: cyl, disp, hp, wt, acc, yr, origin, car_type
X = data.drop('mpg', axis=1)
y = data[['mpg']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

sc_x, sc_y = StandardScaler(), StandardScaler()
X_train_s = sc_x.fit_transform(X_train)
y_train_s = sc_y.fit_transform(y_train)

# --- MODELS ---
models = {
    "linear": LinearRegression().fit(X_train_s, y_train_s),
    "ridge": Ridge(alpha=0.3).fit(X_train_s, y_train_s),
    "lasso": Lasso(alpha=0.1).fit(X_train_s, y_train_s)
}

# --- SAVE ---
print("\n--- Overwriting Model Artifacts ---")
for name, m in models.items():
    joblib.dump(m, os.path.join(path, f"{name}_model.joblib"))
joblib.dump(sc_x, os.path.join(path, "scaler_x.joblib"))
joblib.dump(sc_y, os.path.join(path, "scaler_y.joblib"))

# --- RESULTS ---
print(f"Dataset Size: {data.shape}")
X_test_s = sc_x.transform(X_test)
y_test_s = sc_y.transform(y_test)

for name, model in models.items():
    score = model.score(X_test_s, y_test_s)
    print(f"{name.capitalize()} R2 Score: {score:.4f}")

print("\nSuccess: Cleaned data and saved 8-feature models!")
