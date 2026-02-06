Here are your organized study notes based on the session. I've structured these to highlight the relationships between the algorithms and the techniques used to improve model performance.

---

## 1. Ensemble Learning

Ensemble learning combines multiple models (often called "weak learners") to create one "strong learner" that is more accurate and robust than any single model.

### **Bagging (Bootstrap Aggregating)**

* **Concept:** Parallel processing. It takes random samples (with replacement) from the original dataset to train multiple models simultaneously.
* **Key Algorithm:** **Random Forest**.
* It builds multiple Decision Trees using random subsets of data and features.
* Final output is determined by "Voting" (for classification) or "Averaging" (for regression).
* **Status:** Bagging concepts completed.



### **Boosting**

* **Concept:** Sequential processing. Each new model attempts to correct the errors made by the previous model.
* **Key Algorithms:**
1. **XGBoost (Extreme Gradient Boosting):** Known for its speed and performance; utilizes advanced regularization to prevent overfitting.
2. **LGBM (Light Gradient Boosting Machine):** Faster than XGBoost; uses a leaf-wise growth strategy rather than level-wise, making it great for large datasets.



---

## 2. Techniques to Reduce Overfitting

Overfitting occurs when a model learns the "noise" in the training data too well and fails to generalize to new data. Use these tools to stop it:

* **Ensemble Learning:** (Bagging/Boosting) reduces variance and bias.
* **Cross-Validation:** Splitting data into multiple folds to ensure the model performs well across different subsets.
* **Regularization:** Adding a penalty to the model complexity (L1/L2).
* **PCA (Principal Component Analysis):** Reducing the number of input variables (Dimensionality Reduction).
* **Dropout:** Specifically for ANN (Artificial Neural Networks), where neurons are randomly "turned off" during training.

---

## 3. Model Performance Ranking

Based on the current evaluation, **Random Forest** is the top-performing model for this dataset.

| Rank | Algorithm | Accuracy (%) |
| --- | --- | --- |
| 1 | **Random Forest** | **96.25** |
| 2 | SVM (Support Vector Machine) | 95.00 |
| 3 | KNN (K-Nearest Neighbors) | 95.00 |
| 4 | Decision Tree (DT) | 95.00 |
| 5 | Logistic Regression | 92.50 |
| 6 | Gaussian Naive Bayes | 91.25 |

---

## 4. Hyperparameter Tuning

To find the absolute best version of a model (like XGBoost or LGBM), we use automated search techniques:

* **Grid Search CV:** Exhaustively searches through every possible combination of provided parameters. Accurate but slow.
* **Random Search CV:** Samples a random selection of parameters. Much faster and often yields similar results to Grid Search.

---

## 5. Practical Application: Customer Churn

* **Project:** Customer Churn Prediction.
* **Definition:** "Churn" refers to a customer exiting or leaving a service.
* **Key Insight:** While the **domain** changes (Banking, Telecom, Retail), the **ML concepts and algorithms** remain the same. The goal is to identify patterns in behavior that lead to a "Churn" label.
