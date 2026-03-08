# 📚 Bookstore Inventory & Sales Management System

> A Python-based modular bookstore simulation demonstrating JSON API communication, input validation, and secure coding practices.

Built as part of **BIT1323 Integrated System Technology** — SEGi University (Jan–Apr 2026)

---

## 🖥️ Demo

```
==================================================
        📚 BOOKSTORE INTEGRATED SYSTEM
==================================================

Options:
  1. Place an order
  2. View current inventory
  3. Exit

Enter choice (1/2/3): 2

====================================================================
                   📚 CURRENT INVENTORY STATUS
====================================================================
ISBN       Title                     Unit Price (RM)    Stock
--------------------------------------------------------------------
ISBN001    The Hobbit                          45.00       44
ISBN002    Harry Potter                        55.00       33
ISBN003    Clean Code                          80.00       12
ISBN004    Python Crash Course                 65.00       15
====================================================================
```

---

## 📁 Project Structure

```
bookstore_system/
├── database/
│   └── inventory.json          # Flat-file JSON database
├── modules/
│   ├── inventory_module.py     # Receives orders, updates stock
│   └── sales_module.py         # Validates input, builds orders
├── utils/
│   └── validator.py            # All input validation logic
├── main.py                     # Entry point — interactive menu
└── task4_test.py               # API simulation & security demo
```

---

## ⚙️ How It Works

The system simulates two software modules communicating via JSON — just like real-world APIs.

```
Customer Input
      │
      ▼
 Sales Module  ──── json.dumps() ────►  Inventory Module
      │                                        │
      │         ◄─── json.loads() ────  Response JSON
      ▼
 Purchase Receipt
```

### Module Responsibilities

| Module | Role |
|--------|------|
| `sales_module.py` | Validates input, masks email, serialises order to JSON |
| `inventory_module.py` | Deserialises JSON, deducts stock, triggers low stock alert |
| `validator.py` | ISBN check, quantity check, stock check, email regex |

---

## 🔒 Security Features

| Feature | Implementation |
|---------|---------------|
| Email masking | `alice@mail.com` → `a***@mail.com` before JSON transmission |
| Input validation | Blocks invalid ISBN, negative qty, excess stock, bad email |
| Safe database writes | Validation runs **before** any file write — no corrupt data |
| No crashes | All invalid inputs return error messages, never exceptions |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- No external libraries needed — uses only Python standard library

### Installation

```bash
# Clone the repository
git clone https://github.com/takrimnoorhamim/bookstore-integrated-system.git
cd bookstore-integrated-system
```

### Run the interactive system

```bash
python main.py
```

### Run the Task 4 API & Security demonstration

```bash
python task4_test.py
```

---

## 📦 Sample Data

The system comes pre-loaded with 4 books in `database/inventory.json`:

| ISBN | Title | Price (RM) | Stock |
|------|-------|-----------|-------|
| ISBN001 | The Hobbit | 45.00 | 44 |
| ISBN002 | Harry Potter | 55.00 | 33 |
| ISBN003 | Clean Code | 80.00 | 12 |
| ISBN004 | Python Crash Course | 65.00 | 15 |

---

## 🧪 Validation Test Cases

`task4_test.py` runs 6 test cases to prove secure coding:

| Test | Input | Expected Result |
|------|-------|----------------|
| ✅ Valid order | ISBN001, qty=3, valid email | Order proceeds |
| ❌ Invalid ISBN | ISBN999 | Error: ISBN not found |
| ❌ Excess stock | ISBN001, qty=999 | Error: Insufficient Stock |
| ❌ Negative qty | qty=-5 | Error: Quantity must be > 0 |
| ❌ Zero qty | qty=0 | Error: Quantity must be > 0 |
| ❌ Bad email | `not-an-email` | Error: Invalid email format |

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-Data_Format-black?style=flat&logo=json)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

- **Language:** Python 3
- **Data Storage:** JSON flat-file database
- **Architecture:** Modular (separation of concerns)
- **Concepts:** API simulation, input validation, PII masking, secure coding

---

## 📖 Key Learning Outcomes

- **JSON as API transport** — `json.dumps()` serialises Python dicts to strings for inter-module communication; `json.loads()` deserialises them back
- **Secure coding** — validating all inputs before processing prevents crashes, negative stock, and data corruption
- **PII protection** — customer emails are masked before being included in any JSON payload or receipt
- **Modular design** — each module has a single responsibility, making the system easy to test and extend

---

## 👤 Author

**Takrim Noor Hamim**
Student ID: SUKD2501817
SEGi University — BIT1323 Integrated System Technology

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
