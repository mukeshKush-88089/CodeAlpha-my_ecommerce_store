# My E-Commerce Store

A full-featured E-Commerce web application built using the Django framework.

---

## 🛠️ Tech Stack

* **Backend:** Python, Django
* **Database:** SQLite (Default)
* **Frontend:** HTML, CSS, JavaScript (Django Templates)

---

## 📂 Project Structure

Based on the project structure, here is how the directory layout is organized:

```text
my_ecommerce_store/
│
├── ecommerce/             # Main project configuration directory
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py        # Project configurations & settings
│   ├── urls.py            # Main URL routing
│   └── wsgi.py
│
├── store/                 # Main application directory (Products, Cart, Checkout)
├── venv/                  # Python Virtual Environment
├── db.sqlite3             # Local Development Database
├── manage.py              # Django management command-line utility
└── .gitignore             # Files to ignore in Git version control