https://archive.ics.uci.edu/dataset/2/adult

Here are your notes formatted in Markdown based strictly on the content provided.

---

# Machine Learning & Naive Bayes Notes

## 1. Probability & Bayes Theorem

* **Conditional Probability:** 
* **Bayes Theorem Components:**
* Prior
* Posterior
* Likelihood
* Marginal Likelihood

---

## 2. Naive Bayes Types & Performance

### Bernoulli Naive Bayes

* **Without Scaling:** 72.5% accuracy (20% test).
* **With Standard Scaler:** 82.5% accuracy (20% test).
* **With Normalizer:** 72.50% accuracy.
* **Observation:** Bernoulli NB performs well with Standard Scaler.

### Gaussian Naive Bayes

* **Without Scaling:** 92.50% accuracy.
* **With Standard Scaler:** 91.2% accuracy.
* **Observation:** Scaling leads to less accuracy; Gaussian NB never requires feature scaling.

### Multinomial Naive Bayes

* Used for multi-class classification (more than 2 classes).

---

## 3. Data Repositories

* **Kaggle:** Repository where you get both datasets and answers.
* **UCI:** Data repository with only datasets (no questions/answers).

---

## 4. CART & Ensemble Learning

**CART:** Classification and Regression Trees.

### Ensemble Learning Categories:

* **Bagging:** Example: Random Forest.
* **Boosting:**
* **AdaBoost:** Outdated/Not required.
* **CatBoost:** Not required.
* **Gradient Boost.**
* **XGBoost:** Extreme Gradient Boosting.
* **LGBM:** Light Gradient Boosting (6 times faster than XGBoost).

* **Voting or Stacking:** Declares a winner based on maximum votes.
