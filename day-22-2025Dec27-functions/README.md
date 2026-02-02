## Functions: The Architecture of Data Science & AI

In Python, **Functions** are the building blocks of every project. Whether you are performing **EDA (Exploratory Data Analysis)**—which is the foundation of Machine Learning—or integrating data cleaning scripts into **LLMs**, functions allow you to write reusable, efficient code.

---

### 🧱 Function Categories

Every function in Python is followed by parentheses `()` and requires a 4-space indentation (tab) for its body.

#### **1. Built-in Functions**

Pre-defined tools that come with Python or libraries like Pandas.

* **Examples:** `print()`, `len()`, `max()`, `min()`, `df.head()`, `df.tail()`.

#### **2. User-Defined Functions**

Created by the developer using the `def` keyword.

* **Syntax:**
```python
def function_name():
    print("Hello Team")

# To execute:
function_name() 
```

---

### 📥 Understanding Arguments

Arguments are the data you pass into a function to make it dynamic.

1. **Formal Arguments:** The placeholders defined during the function **definition**.
2. **Actual Arguments:** The real values passed when the function is **called**.

#### **Types of Actual Arguments:**

* **Positional:** Arguments passed in the correct positional order.
* **Keyword:** Arguments identified by the parameter name (e.g., `func(name="NIT")`).
* **Default:** Arguments that take a pre-set value if none is provided.
* **Variable Length (`*args`):** Allows a function to accept any number of positional arguments.
* **Keyword Variable Length (`**kwargs`):** Allows a function to accept any number of keyword-value pairs.

---

### 🧬 Advanced Logic: Polymorphism

The concepts you learn in function arguments apply directly to **Polymorphism** ("Many Forms").

* **Operator Overloading:** A key part of polymorphism where the same operator (like `+`) behaves differently depending on the data type (e.g., adding numbers vs. merging strings).
* **Project Integration:** In your **IPL Analytics Project**, you might use polymorphism to create a single function that can process either "Team Stats" or "Player Stats" based on the input type.

---

### 💡 Pro-Developer Habits

* **Avoid Excessive `print()`:** Within professional functions, try to use `return` values instead of printing every line. This makes your function "clean" and usable by other parts of your AI model.
* **EDA Foundation:** Use functions to automate your data cleaning. If you have 10 different IPL datasets, one clean function can process them all, saving hours of manual work.
