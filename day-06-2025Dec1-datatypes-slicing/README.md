## Python Data Ecosystem: Study Notes

### ⚠️ Common Python Errors

* **NameError:** Referencing a variable that hasn't been defined.
* **SyntaxError:** Incorrect Python syntax (e.g., missing colons or parentheses).
* **ZeroDivisionError:** Attempting to divide a number by zero.
* **IndexError:** Accessing an index that is out of range.
* **TypeError:** Performing an operation on an incompatible data type.
* **ValueError:** Passing an argument with the right type but inappropriate value.

---

### 🛠️ Environment Setup

* **Compression:** Install **WinRAR** or **WinZip** for dataset management.
* **Platforms:** Use **Google Colab** for cloud GPU access or a **local Python installation**.

---

### 📊 Fundamental Data Types

In Python, variables are identifiers pointing to objects of specific types:

| Type | Description | Example |
| --- | --- | --- |
| **int** | Integers / Whole numbers. | `5` |
| **float** | Decimal numbers (supports scientific notation). | `10.67` |
| **bool** | Boolean logic: `True` (1) or `False` (0). | `True` |
| **complex** | Numbers with real and imaginary parts (). | `10 + 20j` |
| **None** | Represents "null" or the absence of a value. | `None` |
| **str** | Text sequences (Strings). | `"Hello"` |

> **Technical Note:** For complex numbers,  represents the imaginary unit .

---

### ✂️ Indexing and Slicing

Slicing is a fundamental skill for handling strings, lists, arrays, and ML datasets.

#### **Indexing Logic**

* **Forward:** `0` to `n-1` (Left to Right).
* **Backward:** `-1`, `-2`, etc. (Right to Left).

#### **Slicing Syntax: `[start : stop]**`

Python uses the **n-1 formula** for the stop index (the stop value is excluded).

* `[:]` : The entire sequence.
* `[start:]` : From the start index to the very end.
* `[:stop]` : From the beginning up to (but not including) the stop index.
* `[start:stop]` : From the start index up to `stop-1`.

---

### 🚀 Core Concepts Summary

* **Variable Syntax:** `identifier = object` (Assigning values).
* **Typecasting:** The process of converting one data type to another (e.g., `int("10")`).
* **Output:** Using the `print()` function to display data.

