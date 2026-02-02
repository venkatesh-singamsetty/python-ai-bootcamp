## Machine Learning (ML) Fundamentals: Study Notes

Machine Learning is a subset of **Artificial Intelligence** that focuses on building systems that learn from data rather than following static, hard-coded rules.

---

### 1. The Core Concept: Learning from Data

In traditional programming, a human writes the rules (). In **Machine Learning**, the machine creates the rules ().

* **Traditional Learning:** Human-led instruction and experience.
* **Machine Learning:** Pattern recognition within **Historical Data**.

---

### 2. The Timeline of Data

How we use data depends on when it was collected relative to the model's "life":

| Data Phase | Timeline | Purpose |
| --- | --- | --- |
| **Historical Data** | Past to Today | **Training** (learning patterns) and **Testing** (checking accuracy). |
| **Future Data** | Tomorrow onward | **Validation/Production** (real-world performance). |

---

### 3. Primary Types of Machine Learning

Machine Learning tasks are generally divided into three main "jobs":

1. **Regression:** Predicting a specific **quantity** (Continuous values).
* *Example:* Predicting the price of a house or the temperature.


2. **Classification:** Predicting a **label** or category (Discrete values).
* *Example:* Identifying if an image is a "Cat" or "Dog," or if an email is "Spam."


3. **Clustering:** Grouping data based on **hidden similarities** (No labels).
* *Example:* Grouping customers into "Big Spenders" vs. "Bargain Hunters."



---

### 4. The ML Development Pipeline

To build a professional model, data must flow through a structured pipeline:

#### **Step 1: Variable Definition**

* **Independent Variables ():** The input features (e.g., Square footage, location).
* **Dependent Variable ():** The target you want to predict (e.g., House Price).

#### **Step 2: The Train-Test Split**

We never show the machine all our data at once. We hide a piece of it to "quiz" the machine later.

* **Training Set (70–80%):** Used for the machine to study and learn.
* **Testing Set (20–30%):** Used to evaluate the machine's performance on unseen data.

#### **Step 3: Execution**

1. **Train:** Fit the algorithm to .
2. **Test:** Predict outcomes for  and compare them against the real .

---

### 5. Real-World Application: Recommendation Engines

When you use a platform like **Amazon** or **Netflix**:

* **Input:** Your clicks, views, and purchases.
* **Learning:** The model treats your clicks as **Historical Data**.
* **Output:** It predicts what you will like next using **Future Data** (the next time you log in).

### 💡 Pro-Tip

In industry, the **Validation Phase** is where most models fail. A model might be 99% accurate on "Historical Data" but fail on "Future Data" because the world changes. This is why continuous testing is mandatory.
