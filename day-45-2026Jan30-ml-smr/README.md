# Advanced Classification & Data Balancing Techniques

This project explores handling imbalanced datasets, high-margin classification with SVM, and probabilistic modeling using Naive Bayes.

---

## ⚖️ Handling Imbalanced Data
In real-world datasets (like fraud detection), one class often outweighs the other. 
* **SMOTE (Synthetic Minority Over-sampling Technique):** Used to convert imbalanced data into balanced data by generating synthetic examples of the minority class.
* **Impact:** Applying SMOTE is crucial for algorithms like **KNN** and **SVM** to prevent them from being biased toward the majority class.

---

## 🛡️ SVM (Support Vector Machine)
SVM seeks the optimal "Hyperplane" to separate data classes.

* **Support Vectors:** The data points nearest to the decision boundary.
* **Hyperplane vs. Best Fit Line:** Unlike Simple Linear Regression (SLR) which finds a central trend line, SVM creates a **Hyperplane** (or SVR for regression) bounded by two parallel decision boundaries.
* **Marginal Distance:** The distance between the two support vector lines. 
    * **Note:** We aim for **Maximum Marginal Distance** to ensure the model generalizes well and provides a clear "safety buffer" between classes.



---

## 🔮 Naive Bayes (Probabilistic Algorithm)
Naive Bayes is based on the principle of conditional probability and is widely used for text classification and real-time predictions.

### 1. Why "Naive"?
It is called "Naive" because it assumes that all features (Event A and Event B) are **independent** of each other. In reality, features often correlate, but this simplification makes the model incredibly fast and effective.

### 2. Bayes Theorem
The model calculates the probability of a hypothesis ($H$) given the evidence ($E$):
$$P(H|E) = \frac{P(E|H) \cdot P(H)}{P(E)}$$

### 3. Types of Naive Bayes
* **Bernoulli NB:** Used for binary/boolean features (Yes/No).
* **Multinomial NB:** Ideal for discrete counts (e.g., word counts in text mining).
* **Gaussian NB:** Used when features follow a normal (Gaussian) distribution.

---

## 🌲 Decision Trees (CART)
The **CART** algorithm serves two purposes:
1. **Classification Trees (CA):** Used to predict a categorical label.
2. **Regression Trees (RT):** Used to predict a continuous numerical value.

---

## 🏆 Final Model Comparison
After applying hyperparameters and balancing techniques (SMOTE), here is the performance summary:

| Algorithm | Accuracy | Key Parameter/Focus |
| :--- | :--- | :--- |
| **KNN** | **95.00%** | $k$ value & Distance Metric |
| **SVM** | **95.00%** | Kernel & Marginal Distance |
| **Logistic Regression** | 92.50% | Solver & Sigmoid Curve |
| **Naive Bayes** | *Pending* | Conditional Probability |

---

## 🛠️ Implementation Workflow
1. **Preprocessing:** Use `StandardScaler` or `Normalization`.
2. **Balancing:** Apply `SMOTE` if the classes are imbalanced.
3. **Training:** Train multiple models (Logit, KNN, SVM, NB, CART).
4. **Serialization:** Save the best performing model using `pickle`.
5. **Deployment:** Integrate the `.pkl` file into the website backend for real-time predictions (e.g., Ticket Confirmation Probability).
