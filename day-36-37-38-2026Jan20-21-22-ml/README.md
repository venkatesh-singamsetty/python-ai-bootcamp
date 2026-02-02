## 📈 Simple & Multiple Linear Regression: Workshop Notes

This summary consolidates the core concepts and practical workflows for building, evaluating, and deploying regression models.

---

### 1. Simple Linear Regression (SLR)

SLR models the relationship between **two variables**: one Independent Variable () and one Dependent Variable ().

**The Mathematical Foundation:**


* **:** Predicted value (Target).
* **:** Input feature.
* ** (Slope):** The steepness of the line; how much  changes for every unit of .
* ** (Intercept):** The value of  when  is zero.

---

### 2. Model Evaluation: Bias & Variance

To move from a "working" model to a "production-grade" model, we analyze the relationship between training and testing performance.

* **Bias (Training Error):** Measures how well the model learns patterns from  and . High bias leads to **Underfitting**.
* **Variance (Testing Error):** Measures how sensitive the model is to new data (). High variance leads to **Overfitting**.

| Model Scenario | Bias (Train ) | Variance (Test ) | Status |
| --- | --- | --- | --- |
| **A** | 0.94 | 0.98 | **Best Fit** (Low Bias, Low Variance) |
| **B** | 0.60 | 0.58 | **Underfitting** (High Bias) |
| **C** | 0.98 | 0.43 | **Overfitting** (High Variance) |

---

### 3. Multiple Linear Regression (MLR)

In real-world business cases,  is rarely affected by only one factor. MLR accounts for multiple independent variables.

**The Formula:**


#### **Feature Selection Strategy**

To keep the model efficient, we use **Recursive Feature Elimination (RFE)** and **p-value** analysis.

* **Goal:** Identify and remove "noisy" or irrelevant attributes.
* **p-value:** A statistical check to see if an attribute is significant. If , the feature is often removed to improve model clarity.

---

### 4. Model Persistence: Serialization with Pickle

Once a model is trained, we don't want to re-train it every time a user opens the app. We save it as a **Pickle (`.pkl`)** file.

* **Serialization:** Converting the Python model object into a byte stream.
* **Efficiency:** A 50-line training script is compressed into a tiny `.pkl` file (often ~1KB), leading to faster load times in the frontend.

```python
import pickle

# Serializing the model
with open("regressor_model.pkl", "wb") as f:
    pickle.dump(regressor, f)

# Deserializing for the App
with open("regressor_model.pkl", "rb") as f:
    model = pickle.load(f)

```

---

### 5. Deployment Workflow

1. **Data:** Import and clean your dataset (1MB–10MB).
2. **Split:** Use a **80/20** split for training and testing.
3. **Train:** Fit the algorithm to find optimal  and .
4. **Validate:** Check  scores for both training and testing.
5. **Save:** Export the model as a `.pkl` file.
6. **Interface:** Use **Streamlit** to create a UI where users can input  and receive a predicted .
