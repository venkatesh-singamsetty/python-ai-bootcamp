## 🚀 Quick Start Guide (Using Root VENV)

```bash
# Ensure you are in the project folder and root .venv is active
python salary_prediction_model_training.py
python -m streamlit run streamlit_salary_prediction_app.py
```

The app should open automatically in your default browser at http://localhost:8501

---

## 📈 Simple & Multiple Linear Regression: Workshop Notes

This summary consolidates the core concepts and practical workflows for building, evaluating, and deploying regression models.

---

### 1. Simple Linear Regression (SLR)

SLR models the relationship between **two variables**: one Independent Variable ($X$) and one Dependent Variable ($Y$).

**The Mathematical Foundation:**
$Y = mX + c$

* **$Y$:** Predicted value (Target).
* **$X$:** Input feature.
* **$m$ (Slope):** The steepness of the line; how much $Y$ changes for every unit of $X$.
* **$c$ (Intercept):** The value of $Y$ when $X$ is zero.

---

### 2. Model Evaluation: Bias & Variance

To move from a "working" model to a "production-grade" model, we analyze the relationship between training and testing performance.

* **Bias (Training Error):** Measures how well the model learns patterns from $X$ and $Y$. High bias leads to **Underfitting**.
* **Variance (Testing Error):** Measures how sensitive the model is to new data ($X_{test}$). High variance leads to **Overfitting**.

| Model Scenario | Bias (Train $R^2$) | Variance (Test $R^2$) | Status |
| --- | --- | --- | --- |
| **A** | 0.94 | 0.98 | **Best Fit** (Low Bias, Low Variance) |
| **B** | 0.60 | 0.58 | **Underfitting** (High Bias) |
| **C** | 0.98 | 0.43 | **Overfitting** (High Variance) |

---

### 3. Multiple Linear Regression (MLR)

In real-world business cases, $Y$ is rarely affected by only one factor. MLR accounts for multiple independent variables.

**The Formula:**
$Y = b_0 + b_1X_1 + b_2X_2 + ... + b_nX_n$

#### **Feature Selection Strategy**

To keep the model efficient, we use **Recursive Feature Elimination (RFE)** and **p-value** analysis.

* **Goal:** Identify and remove "noisy" or irrelevant attributes.
* **p-value:** A statistical check to see if an attribute is significant. If $p > 0.05$, the feature is often removed to improve model clarity.

---

### 4. Model Persistence: Serialization with Joblib

Once a model is trained, we don't want to re-train it every time a user opens the app. We save it as a **Joblib (`.joblib`)** file.

* **Serialization:** Converting the Python model object into a byte stream.
* **Joblib Advantage:** Optimized for storing large numerical arrays (like coefficients) significantly faster than standard Pickle.

```python
import joblib

# Serializing the model
joblib.dump(regressor, "linear_regression_model.joblib")

# Deserializing for the App
model = joblib.load("linear_regression_model.joblib")
```

---

### 5. Deployment Workflow

1. **Data:** Import and clean your dataset.
2. **Split:** Use a **80/20** split for training and testing.
3. **Train:** Fit the algorithm to find optimal parameters.
4. **Validate:** Check $R^2$ scores for both training and testing.
5. **Save:** Export the model as a `.joblib` file.
6. **Interface:** Use **Streamlit** to create a UI where users can input $X$ and receive a predicted $Y$.
