---

**Python Variables:**  
- Syntax: `variable_name = value`  
- Rules:  
  1. Case-sensitive  
  2. Cannot start with digit  
  3. Only `_` allowed as special character  
  4. Cannot use keywords  

**Functions:**  
- Called with `()`  
- Example: `family1(d, m)`  

**Data Types Covered:**  
- int, float, bool, complex, string  

**String Indexing & Slicing:**  
- Forward: starts at 0  
- Backward: starts at -1  
- Slice syntax: `start:end` (end-1)  

**Python Type Casting & print() Method:**  
- Convert between compatible types  
- Print with format or f-string  

# Python Fundamentals & Modern AI Infrastructure

This section establishes the "ground rules" for writing Python code and explains why high-end hardware is necessary for today’s AI models.

---

## 📦 Python Variables (Identifiers)
In Python, a variable is essentially a name (identifier) given to an object/value. 

**Syntax:** `variable_name = value`

### Rules for Defining Variables
1.  **Case Sensitivity:** `nit = 5` is different from `NIT = 5`.
2.  **No Leading Digits:** A variable cannot start with a number (e.g., `1name` is invalid), but it can end with one (`name1` is valid).
3.  **Special Characters:** No special characters allowed (e.g., `@`, `$`, `%`) **except** for the underscore `_`.
4.  **Keywords:** Reserved words (like `if`, `else`, `while`) cannot be used as variable names. Think of these as "Reserved Hotel Rooms"—you cannot check into them.

---

## ⚙️ Python Functions
Functions are the "actions" we perform in code.
* **Identification:** Functions always end with parentheses `()`. 
    * *Example:* `id()` or `print()`.
* **Methods:** In Python, we often call functions attached to objects using the dot `.` notation.
* **Arguments/Parameters:** These are the inputs you pass into a function.
    * `family1(d, m)` → Function with **2 parameters**.
    * `family2(d, m, s, d)` → Function with **4 parameters**.

---

## 🖥️ Hardware for AI: CPU vs. GPU
Training modern AI models (like ChatGPT) involves billions of parameters. 

* **CPU (Central Processing Unit):** Standard machines are often too slow for training large models.
* **GPU (Graphics Processing Unit):** Required for parallel processing of billions of parameters.
    * *Tool Tip:* Use **Google Colab** to access free GPU resources for training your models.

---

## 🚀 Final Workflow Reminder
1.  **Define Variables:** Follow the naming rules.
2.  **Use Functions:** Call them with `()` and pass the correct parameters.
3.  **Train Models:** Use GPUs for high-parameter models.
4.  **Save/Deploy:** Use `pickle` to save your work for production.