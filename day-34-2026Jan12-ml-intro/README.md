# Machine Learning (ML) Basics

Machine Learning (ML) is a field of Artificial Intelligence (AI) where **machines learn from historical data** to make predictions or decisions without being explicitly programmed.

---

## 1. What is Machine Learning?

Machine Learning is the process of **teaching machines to learn patterns from historical data** and apply this learning to make decisions on new, unseen data.

- Example: Amazon.com shows different products based on your previous visits and purchases. The system **learns from historical user behavior** to recommend items.

---

## 2. What is Traditional Learning?

Traditional learning refers to **human learning**, where we learn concepts, patterns, or skills from experience or instructions.

- Example: A student studies textbooks and practices problems to learn math.

---

## 3. Types of Data in Machine Learning

Machine learning uses two main types of data:

### 3.1 Historical Data
Data collected **up to today**, used to **train and test** ML models.  

- **Training Phase:** The model learns patterns from this data.  
- **Testing Phase:** The model is evaluated on unseen portions of historical data to check its performance.

### 3.2 Future Data
Data that will be generated **from tomorrow onward**, used in the **validation phase** to see how well the model performs in real-world scenarios.  

---

## 4. Types of Machine Learning

Machine learning can be broadly categorized into:

1. **Regression** – Predicts continuous values.  
   - Example: Predicting house prices.
2. **Classification** – Predicts discrete categories.  
   - Example: Email spam detection.
3. **Clustering** – Groups similar data points without labels.  
   - Example: Customer segmentation for marketing.

---

## 5. ML Workflow / Data Preprocessing Pipeline

Machine learning follows a step-by-step workflow to process data and train models:

### Step 1: Dataset
Collect historical data.  

### Step 2: Independent & Dependent Variables
- **Independent Variable (X):** Features used for prediction.  
- **Dependent Variable (Y):** Target value to predict.

### Step 3: Split Dataset
- **X → X_train & X_test**  
- **Y → Y_train & Y_test**  

### Step 4: Train-Test Split Ratio
Common ratios for splitting the data:  
- 80% train – 20% test  
- 70% train – 30% test  
- 75% train – 25% test  

### Step 5: Train the Model
- Feed **training data** to the ML algorithm to learn patterns.  

### Step 6: Test the Model
- Evaluate the model using **testing data** to check accuracy and performance.

---

## 6. Example: Amazon.com Recommendation

1. **First Visit:** Select an item → The system records this as historical data.  
2. **Re-login:** Same item is reflected → Machine has learned your preferences from historical data.

> Machines improve recommendations over time by learning from **historical user interactions**.

---

## Summary

- Machine Learning = Machines learning from historical data.  
- Historical data = Training + Testing.  
- Future data = Validation.  
- ML types = Regression, Classification, Clustering.  
- ML workflow = Dataset → Train-Test Split → Train → Test → Validate.
