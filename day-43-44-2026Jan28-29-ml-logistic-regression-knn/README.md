## 🚗 Customer Vehicle Purchase Prediction: Implementation Notes

This guide consolidates the key learnings from the classification workshop, focusing on Logistic Regression, KNN, and the practicalities of model deployment.

---

### 🧠 Core Concepts: Binary Classification

Classification is the process of predicting a discrete label (category). For vehicle purchases, this is a **Binary Classification** problem (1: Purchase, 0: No Purchase).

#### **Logistic Regression (Logit/MaxEnt)**

Unlike Linear Regression which predicts a continuous line, Logistic Regression uses the **Sigmoid Activation Function** to map any real-valued number into a probability between 0 and 1.

#### **K-Nearest Neighbors (KNN)**

KNN is an instance-based learning algorithm that classifies a data point based on how its neighbors are classified.

* **Euclidean Distance:** The "straight-line" distance between two points.
* **Manhattan Distance:** The distance measured along axes at right angles ("city block" distance).

---

### 🧪 Experimentation & Sensitivity Analysis

Model performance is highly sensitive to how data is prepared. We observed significant fluctuations based on three factors:

1. **Scaling Method:** **StandardScaler** (Standardization) significantly outperformed **Normalization** (Min-Max Scaling) in this specific use case (92.5% vs 72.5%).
2. **Test Split:** A **20%** test split provided a better balance for this dataset size than a 25% split.
3. **Random State:** This parameter controls the shuffling of data. Even with the same model, different shuffles resulted in an accuracy range of **82.5% to 92.5%**.

---

### ⚖️ Model Evaluation (Bias-Variance Tradeoff)

Finding the "Best Fit" requires evaluating both training error (**Bias**) and testing error (**Variance**).

| Fit Type | Bias (Training Error) | Variance (Testing Error) | Result |
| --- | --- | --- | --- |
| **Best Fit** | Low | Low | **Optimal Performance** |
| **Overfit** | Very Low | High | Fails on new, unseen data |
| **Underfit** | High | Low | Too simple to capture patterns |

---

### 🤖 Algorithm Comparison: Robustness vs. Sensitivity

| Feature | Logistic Regression | KNN (K-Nearest Neighbors) |
| --- | --- | --- |
| **Outlier Impact** | **Low.** Sigmoid function squashes extreme values. | **High.** Outliers distort the distance calculations. |
| **Interpretability** | High (Coefficients/Probabilities). | Low (Black-box distance logic). |
| **Best Accuracy** | 92.50% | **95.00%** (With cleaned data). |

---

### 🏗️ Deployment & The "Pickle" Workflow

In an organization, we don't just "run" models; we deploy them as services.

1. **Serialization (Pickle):** We convert the trained model object into a byte stream (a `.pkl` file).
2. **Integration:** This file is loaded into a web backend (Django/Flask/FastAPI).
3. **Inference:** When a user interacts with a website (like a flight booking portal), the model processes the input in real-time to predict probabilities (e.g., probability of ticket confirmation).

---

**Summary:** While KNN provided higher peak accuracy, **Logistic Regression** offered more stability and robustness against outliers. Mastering the **random_state** and **StandardScaler** was critical in achieving the 92.5% benchmark.
