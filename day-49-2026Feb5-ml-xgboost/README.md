Refer https://www.kaggle.com/code/prashant111/lightgbm-classifier-in-python

---

## 🏗️ Machine Learning Algorithms (Scikit-Learn Framework)

### Linear & Non-Linear Regression

* **Simple Linear Regression (SLR):** Focuses on finding the **Best Fit Line** by minimizing the error between predicted and actual values.
* **Multiple Linear Regression (MLR):** Uses multiple features. Key technique: **Backward Elimination** (Recursive Feature Elimination based on p-values).
* **Polynomial Regression:** A linear model used when data is **non-linear**; it increases the degree of the features to fit curves.

### Classification & Advanced Models

* **SVM / SVR:** Uses **Hyperplanes** and **Decision Boundaries**. Key concepts include Kernels (Linear, RBF, etc.) and maximizing the margin.
* **K-Nearest Neighbors (KNN):** Distance-based (Euclidean/Manhattan). Sensitive to **imbalanced data**.
* **Naive Bayes:** Based on **Bayesian Probability** (Conditional, Prior, and Posterior probability).
* **Decision Tree (DT):** Works on splitting nodes based on **Information Gain** and **Entropy**. Key parameters: `max_depth` and node **purity**.

### Ensemble Methods (Boosting & Bagging)

* **Random Forest (RF):** A collection of multiple Decision Trees (`n_estimators`) using bagging.
* **XGBoost:** Gradient boosting focused on training time and performance (popular in Kaggle competitions).
* **LGBM (LightGBM):** A high-performance gradient boosting framework that supports **GPU processing** for faster training.

---

## 📊 Evaluation & Model Performance

### Error Metrics

To measure the "loss" or distance from the best fit line:

* **MAE:** Mean Absolute Error
* **MSE:** Mean Squared Error
* **RMSE:** Root Mean Squared Error

### Classification Metrics (Confusion Matrix)

* **Components:** True Positive (TP), True Negative (TN), False Positive (FP), False Negative (FN).
* **F1-Score:** The harmonic mean of Precision and Recall.
* **SMOTE:** Used to handle imbalanced datasets by oversampling the minority class.

### Model Fit Issues

* **Overfitting:** High variance; model performs well on training data but poorly on validation data.
* **Underfitting:** High bias; model is too simple to capture the underlying pattern.
* **Regularization:** Using **L1 (Lasso)** or **L2 (Ridge)** penalties to prevent overfitting.

---

## 🛠️ Optimization & Validation

### Cross-Validation (Handling Overfitting)

When a model overfits, we use **K-Fold Cross-Validation** to ensure the model generalizes well by splitting the data into "K" different subsets and training/testing multiple times.

### Hyperparameter Tuning (Model Tuning)

* **Grid Search CV:** Exhaustively searches through a specified subset of hyperparameters.
* **Random Search CV:** Randomly selects combinations of hyperparameters (faster than Grid Search).
