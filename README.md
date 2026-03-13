# 🐍 Python Fundamentals

A hands-on collection of Python fundamentals—syntax, control flow, functions, and core concepts—with runnable examples for learning and reference.

---

## 📋 Overview

This repository contains clear, minimal examples covering the core building blocks of Python. Use it to learn the basics, brush up before interviews, or as a quick reference while coding.

---

## ✨ Topics Covered

| Topic | Description |
|-------|-------------|
| **Variables & Types** | Numbers, strings, booleans, and type basics |
| **Functions** | Defining, calling, parameters, return values, and scope |
| **Control Flow** | `if`/`elif`/`else`, `for` and `while` loops |
| **Data Structures** | Lists, tuples, dictionaries, sets |
| **File I/O** | Reading and writing files |
| **Error Handling** | `try`/`except` and raising exceptions |
| **Modules & Imports** | Organizing code and reusing modules |

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.8+**  
  Check your version:
  ```bash
  python --version
  ```

### Clone & Run

```bash
# Clone the repository
git clone https://github.com/your-username/python-fundamentals.git
cd python-fundamentals

# Run an example (e.g. functions)
python function.py
```

### Using a Virtual Environment (recommended)

```bash
# Create and activate a virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

# Run scripts
python function.py
```

---

## 📁 Project Structure

```
python-fundamentals/
├── README.md          # This file
├── function.py        # Function basics (defining, calling, parameters)
└── ...                # More examples as you add them
```

---

## 📖 Example: Functions

`function.py` shows a simple function definition and call:

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("John"))  # Hello, John!
```

Run it:

```bash
python function.py
```

---

## 🤝 Contributing

Contributions are welcome. To add a new fundamentals example:

1. Fork the repo and create a branch (`git checkout -b topic/short-name`).
2. Add your script (e.g. `loops.py`, `lists.py`) with clear comments.
3. Update this README with a short description and usage.
4. Open a Pull Request.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🔗 Resources

- [Official Python Documentation](https://docs.python.org/3/)
- [Python Tutorial (docs.python.org)](https://docs.python.org/3/tutorial/)
- [PEP 8 – Style Guide](https://peps.python.org/pep-0008/)

---

*Happy coding!*
