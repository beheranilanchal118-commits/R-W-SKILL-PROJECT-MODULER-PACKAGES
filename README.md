# 🛠️ Multi-Utility Toolkit

A simple Python-based **Multi-Utility Toolkit** that combines different useful operations into one menu-driven application.

The project is built using **Python Modules and Packages**. Each major operation is separated into its own module, making the project easy to understand, maintain, and extend.

---

## 📌 Features

The Multi-Utility Toolkit provides the following operations:

### 🕒 1. Datetime & Time Operations

- Display current date and time
- Calculate difference between two dates
- Format date into a custom format
- Stopwatch
- Countdown Timer

### 🧮 2. Mathematical Operations

- Calculate factorial
- Calculate compound interest
- Trigonometric calculations
- Calculate area of geometric shapes
  - Rectangle
  - Circle
  - Triangle

### 🎲 3. Random Data Generation

- Generate random numbers
- Generate random lists
- Create random passwords
- Generate 6-digit OTP

### 🔑 4. UUID Generation

- Generate unique UUID4 identifiers

### 📁 5. File Operations

- Create a new file
- Write data to a file
- Read data from a file
- Append data to a file
- Automatically save program outputs to `output.txt`

### 🔍 6. Module Explorer

- Explore Python modules
- Display available module attributes using `dir()`
- Dynamically load modules using `importlib`

---

## 🏗️ Project Structure

```text
MODULE & PACKAGE/
│
├── main.py
├── output.txt
│
└── toolkit/
    │
    ├── __init__.py
    ├── datetime_operations.py
    ├── math_operations.py
    ├── random_operations.py
    ├── uuid_operations.py
    ├── file_operations.py
    └── module_explorer.py
