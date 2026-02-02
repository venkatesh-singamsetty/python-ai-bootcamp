# Python Basics Notes

This README covers **import statements**, **input with eval usage**, and **NumPy basics** in a simple and concise manner.

---

## 1. Import Details

```python
import numpy as np
import sys
```

- `import` is used to include external modules in a program
- `numpy` → numerical and array operations
- `sys` → system-level operations (like command-line arguments)
- `as np` → alias for shorter usage

---

## 2. Input and `eval()` Function

### `input()`

```python
x = input("Enter value: ")
```

- Always returns **string** type

```python
x = int(input("Enter number: "))
```

- Explicit type conversion is required

### `eval()` Usage

```python
x = eval(input("Enter value: "))
```

- Automatically converts input into Python data types
- Can accept:
  - Numbers → `10`
  - List → `[1, 2, 3]`
  - Tuple → `(1, 2)`

⚠️ **Warning:** `eval()` executes expressions, so avoid using it with untrusted input

---

## Summary

- `import` → load modules
- `input()` → string input
- `eval()` → automatic type conversion (use carefully)

# 🔢 Logic, Operators & Number Systems

This section covers the mathematical and logical engines that power Python's decision-making capabilities.

---

## ⚖️ Comparison & Logical Operators

To compare variables and control the flow of our ML models, we use:

### 1. Relational Operators
Used to compare two variables (e.g., `a > b`, `a == b`, `a != b`).

### 2. Logical Operators
Used to combine multiple conditions:
* **and**: Returns True if **both** statements are true.
* **or**: Returns True if **one** of the statements is true.
* **not**: Reverses the result (True becomes False).

---

## 🔢 The Number System
Python allows you to work across different numerical bases. Understanding these is the "gatekeeper" to mastering Bitwise operators.

| System | Base | Python Prefix | Range / Notes |
| :--- | :--- | :--- | :--- |
| **Binary** | 2 | `0b` | 0, 1 |
| **Octal** | 8 | `0o` | 0 - 7 |
| **Decimal** | 10 | *None* | 0 - 9 (Standard) |
| **Hexadecimal** | 16 | `0x` | 0-9 and **a-f** (a=10, b=11, c=12, d=13, e=14, f=15) |

---

## ⚡ Bitwise Operators
While logical operators work on whole values, **Bitwise operators** work at the binary level (converting numbers to bits).



* **Bitwise AND (`&`)**: Sets each bit to 1 if both bits are 1.
* **Bitwise OR (`|`)**: Sets each bit to 1 if one of two bits is 1.
* **Bitwise XOR (`^`)**: Sets each bit to 1 if **only one** of two bits is 1.

> **Crucial Concept:** To understand Bitwise logic, you must be able to convert a standard Number $\rightarrow$ Binary and Binary $\rightarrow$ Number.

---

## 🛠️ Summary of Conversions
* **Number to Binary:** `bin(10)` $\rightarrow$ `'0b1010'`
* **Number to Hex:** `hex(10)` $\rightarrow$ `'0xa'`
* **Number to Octal:** `oct(10)` $\rightarrow$ `'0o12'`

---

## 📈 Model Accuracy & System Logic
The efficiency of our algorithms like **KNN (95%)** and **SVM (95%)** often relies on how the computer processes these bits in the background. Mastering these "low-level" concepts makes you a stronger AI developer, not just a coder.

---

### 🚀 Final Reminders for the Program
* **Revision:** Spend 1 hour today converting Decimal numbers to Binary by hand.
* **Mindset:** If you don't understand the Binary system, Bitwise operators will remain a mystery. Take the time to learn the base!


