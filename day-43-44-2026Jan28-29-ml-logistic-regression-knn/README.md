---

# 2026Jan28

# Customer Vehicle Purchase Prediction

This project implements a **Logistic Regression** classifier to predict future customer behavior based on historical purchase data.

## 🧠 Core Concepts

### Linear vs. Logistic Regression
* **Linear Regression:** Used for predicting continuous numerical values.
* **Logistic Regression:** Used for binary classification (0 or 1). Also known as **Logit** or **MaxEnt** (Maximum Entropy) classifier.

### Deep Learning & Activation Functions
* **Architectures:** ANN (Artificial Neural Networks), CNN (Convolutional), and RNN (Recurrent).
* **Activation:** The **Sigmoid** function is used to map predicted values to probabilities between 0 and 1.

---

## 🧪 Experimentation & Test Cases

We conducted multiple tests to observe how data splitting, scaling, and randomness affect model Accuracy (AC).

| Test Case | Test Split | Scaling / Method | Accuracy |
| :--- | :--- | :--- | :--- |
| **Case 1** | 25% | StandardScaler | 89.00% |
| **Case 2** | 20% | StandardScaler | **92.50%** |
| **Case 3** | 20% | Normalization | 72.50% |

### 🎲 Random State Analysis
Changing the `random_state` significantly impacts the model's split and final accuracy:
* `random_state = 0`: **92.50%**
* `random_state = 51`: 88.75%
* `random_state = 21`: 86.25%
* `random_state = 100`: 82.50%

---

## ⚖️ Model Evaluation (Bias-Variance Tradeoff)

Selecting the best model involves balancing Bias (error on training data) and Variance (error on test data).

1.  **Best Fit:** (AC: 92.50, Bias: 82.5, Var: 92.50) — Balanced and reliable.
2.  **Overfit:** (AC: 92.50, Bias: 34, Var: 90) — High variance; fails on new data.
3.  **Underfit:** (AC: 92.50, Bias: 90, Var: 34) — High bias; too simple to learn.
4.  **Low Accuracy:** (AC: 34, Bias: 90, Var: 89) — Fails on both training and testing.

---

## 🚀 Future Implementation: Real-Time Prediction

The ultimate goal is to move from historical analysis to active business intelligence:
* **Data Capture:** New customer data (e.g., from *tata.com*) is stored in the database.
* **ML Prediction:** The model runs "behind the scenes" to predict the probability of a purchase.
* **Outcome:** Classification of **1 (Will Purchase)** or **0 (Will Not Purchase)**.

**Next Step:** Implement a hyperparameter tuning table (GridSearch) to further refine the 92.5% accuracy benchmark.

---

# 2026Jan29

# Machine Learning: Classification & Deployment Strategy

This repository covers the implementation of various classification algorithms, model validation phases, and the transition from development to live deployment.

## 🧪 Model Validation & Testing Phases
We follow a 3-phase testing approach to ensure the model's reliability before it goes live:
1. **Training Phase:** Model learns patterns from historical data.
2. **Validation Phase:** Tuning hyperparameters and checking for overfitting (Validation data vs. Live data).
3. **Testing Phase:** Final evaluation using the best average score to determine the "Best Accuracy Model."

---

## 🤖 Algorithms Compared

### 1. Logistic Regression (Logit / MaxEnt)
* **Mechanism:** Uses the Sigmoid curve to classify data.
* **Outlier Impact:** **No significant impact.** The sigmoid function naturally squashes outliers, making the model robust.
* **Key Hyperparameters:** Solver selection (e.g., lbfgs, liblinear).

### 2. KNN (K-Nearest Neighbors)
* **Mechanism:** Classifies data points based on the proximity of $k$ neighbors.
    * **Classification:** Majority vote of $k$ points.
    * **Regression:** Mean of $k$ nearest neighbors.
* **Distance Metrics:** * **Euclidean Distance:** $d = \sqrt{\sum(x_i - y_i)^2}$
    * **Manhattan Distance:** $d = \sum |x_i - y_i|$
* **Outlier Impact:** **Yes.** Outliers significantly impact KNN because they distort the distance matrix.



---

## 📊 Performance Benchmark (Sample Dataset)
When applying multiple models to the same dataset, we compare accuracy to find the "Best Fit":

| Model | Accuracy | Notes |
| :--- | :--- | :--- |
| **KNN** | **95.00%** | Higher accuracy but sensitive to outliers. |
| **Logistic Regression** | 92.50% | Robust and consistent. |
| **SVM** | *TBD* | Pending evaluation. |

---

## 🏗️ Deployment & Real-World Use Case

### The "Pickle" Workflow
Once we identify the best model, we "freeze" it using the **Pickle** library. This allows us to save the trained model object and deploy it into a production environment without retraining.

### Use Case: Flight Booking Website
We can deploy a small ML snippet into a company website (e.g., a travel portal):
* **Input:** User enters flight details.
* **ML Logic:** The model runs in the background.
* **Output:** Predicts the **probability of ticket confirmation** in real-time.



---

## 📝 Summary of Findings
* **Overfitting:** A technique/risk where the model performs perfectly on training data but fails on validation data.
* **Binary vs. Multi-class:** While we started with binary (0 or 1), these algorithms extend to multi-class classification for images and text analysis.

