## 1. The ML Journey: Supervised Learning

In this journey, we work with **labeled datasets**. This falls under **Supervised Learning**, where the model learns the relationship between independent variables (features) and a target dependent variable (label).

## 2. Decision Tree: How it Makes Decisions

A Decision Tree splits data into branches based on feature values, forming a hierarchy that looks like an inverted tree.

### Building the Tree: Step-by-Step

1. **Understand Attributes:** Identify your features.
2. **Define Variables:** Separate your **Independent Variables** (inputs) and **Dependent Variable** (the target, e.g., "Profit").
3. **Calculate Information Gain (IG):** First, calculate the entropy (uncertainty) of the dependent variable.
4. **Calculate Feature Gain:** Determine how much "uncertainty" is reduced by splitting on a specific feature (like Age or Competition).

### The Math: Entropy vs. Gini

* **Entropy:** Measures impurity using logarithmic calculations.
* Formula: 
* *Note: Log calculations can be computationally slow.*


* **Gini Index:** A faster alternative to Entropy that avoids logs. It measures the probability of a variable being wrongly classified.
* **Information Gain:** 

### Important Tree Rules

* **The Root Node:** This is always the independent variable with the **highest Gain**. A dependent variable can never be a root node.
* **Leaf Nodes:** These are the end points. A node becomes a leaf when it is "pure" (e.g., all samples belong to one class, or one side becomes 0). Once a leaf is declared, that branch stops growing.
* **No Feature Scaling:** Unlike KNN or SVM, Decision Trees do **not** require feature scaling (standardization/normalization) because they split based on thresholds, not distances.

---

## 3. Overfitting and Pruning

When a tree grows too deep (usually because there are too many features), it memorizes the noise in the data rather than the pattern. This is **Overfitting**.

* **Pruning:** The process of cutting back branches to simplify the model and improve its ability to generalize to new data.

---

## 4. Model Ranking & Selection

Before saving your model (serialization via **Pickle**), you must compare performance.

| Model | Bias/Accuracy |
| --- | --- |
| **Decision Tree (DT)** | **95%** |
| KNN | 95% |
| SVM | 95% |
| Logistic Regression | 92.5% |
| Gaussian Naive Bayes | 91.25% |

---

## 5. Performance Metrics: AUC & ROC

The **ROC Curve** is a graphical representation of the **Confusion Matrix** performance across different thresholds.

* **X-Axis:** False Positive Rate (FPR)
* **Y-Axis:** True Positive Rate (TPR)
* **AUC (Area Under the Curve):** The closer the area is to 1.0, the better the model is at distinguishing between classes.
