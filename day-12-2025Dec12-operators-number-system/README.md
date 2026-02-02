## Python Operators & Number Systems: Study Notes

### 🔢 1. Python Operators

Operators allow you to manipulate data, perform calculations, and manage logic.

#### **Arithmetic Operators (Math)**

* **Standard:** `+`, `-`, `*`, `/`
* **Modulus (`%`):** Returns the **remainder** (e.g., `10 % 3 = 1`).
* **Floor Division (`//`):** Divides and rounds **down** to the nearest whole number.
* **Exponentiation (`**`):** Calculates power (e.g., `2 ** 3 = 8`).

#### **Relational & Logical Operators (Conditions)**

* **Relational:** `==`, `!=`, `>`, `<`, `>=`, `<=` (Always returns a Boolean).
* **Logical:**
* `and`: True only if **both** sides are True.
* `or`: True if at least **one** side is True.
* `not`: Inverts the logic (True becomes False).



#### **Assignment & Swapping**

* **Short-hand:** `a += 5` is equivalent to `a = a + 5`.
* **Pythonic Swap:** You can swap values without a temporary variable:
`a, b = b, a`

---

### 🖥️ 2. Bitwise Operators

These operate at the binary level (0s and 1s).

| Operator | Description | Calculation Logic |
| --- | --- | --- |
| **`&` (AND)** | Binary AND | 1 if both bits are 1 |
| **` | ` (OR)** | Binary OR |
| **`^` (XOR)** | Binary XOR | 1 if bits are different |
| **`~`** | Complement | Inverts all bits |
| **`<<`** | Left Shift | Multiply by  |
| **`>>`** | Right Shift | Floor divide by  |

---

### 🔢 3. Python Number Systems

Python supports four bases for representing integers. You can identify them by their specific prefixes.

| System | Base | Prefix | Example |
| --- | --- | --- | --- |
| **Binary** | 2 | `0b` | `0b1010` (Decimal 10) |
| **Octal** | 8 | `0o` | `0o12` (Decimal 10) |
| **Decimal** | 10 | *None* | `10` |
| **Hexadecimal** | 16 | `0x` | `0xA` (Decimal 10) |

> **Note:** Regardless of the input format (Binary, Octal, or Hex), if you `print()` the variable, Python displays it in **Decimal** by default.

### 3.1 Decimal (Base 10)
```python
a = 10
```

### 3.2 Binary (Base 2)
Prefix: 0b
```python
a = 0b1010
print(a)
```

### 3.3 Octal (Base 8)
Prefix: 0o
```python
a = 0o12
print(a)
```

### 3.4 Hexadecimal (Base 16)
Prefix: 0x
```python
a = 0xA
print(a)
```

---

### 💡 Key Takeaway

Bitwise operations and different number systems are essential for low-level data processing, cryptography, and optimizing performance in complex Machine Learning algorithms.

Would you like me to show you how to use Python's built-in functions like `bin()`, `oct()`, and `hex()` to convert between these systems?
