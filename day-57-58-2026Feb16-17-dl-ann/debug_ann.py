import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
from sklearn.compose import ColumnTransformer 
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import os

# Essential for Mac with multiple TF/Keras installations
os.environ["KERAS_BACKEND"] = "tensorflow"

try:
    print("Clearing Keras session...")
    tf.keras.backend.clear_session()
    
    print("Loading and Preprocessing...")
    dataset = pd.read_csv('Churn_Modelling.csv')
    X = dataset.iloc[:, 3:-1].values
    y = dataset.iloc[:, -1].values

    # Gender Encoding
    le = LabelEncoder() 
    X[:, 2] = le.fit_transform(X[:, 2])

    # Geography Encoding
    ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [1])], remainder='passthrough')
    X = ct.fit_transform(X)
    
    # Ensure dense numeric array
    X = np.array(X, dtype=np.float32)
    y = np.array(y, dtype=np.float32)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    # Scaling
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    print(f"Final X_train shape: {X_train.shape}, dtype: {X_train.dtype}")

    print("Building model...")
    ann = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(X_train.shape[1],)),
        tf.keras.layers.Dense(units=6, activation='relu'),
        tf.keras.layers.Dense(units=6, activation='relu'),
        tf.keras.layers.Dense(units=1, activation='sigmoid')
    ])

    print("Compiling model...")
    ann.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    print("Fitting model (CPU context)...")
    with tf.device('/CPU:0'):
        ann.fit(X_train, y_train, batch_size=32, epochs=5)
    
    print("FIT SUCCESSFUL!")

except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()
