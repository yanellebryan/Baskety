<div align="center">
  <h1>🛒 Baskety - Mini Mart POS & Inventory System</h1>
  <p>A comprehensive, modern Point-of-Sale and Inventory Management solution built with Django.</p>

  ![Python](https://img.shields.io/badge/Python-3.x-blue.svg?logo=python&logoColor=white)
  ![Django](https://img.shields.io/badge/Django-6.0-092E20.svg?logo=django&logoColor=white)
  ![SQLite](https://img.shields.io/badge/SQLite-Database-003B57.svg?logo=sqlite&logoColor=white)
</div>

---

## 📖 Project Overview

**Baskety** is designed to streamline daily operations for mini-marts and grocery stores. It provides a centralized, user-friendly platform for tracking products, managing stock, and processing fast sales transactions efficiently in a fast-paced retail environment.

## ✨ Key Features

Our system is broken down into dedicated modules for maximum efficiency:

### 🛍️ Point of Sale (POS)
- **Fast Checkout Interface:** A dedicated, modern UI for cashiers to process sales quickly and accurately.
- **Dynamic Cart Management:** Add, edit, and remove items with real-time total calculation.
- **Receipt Generation:** Easily complete transactions and generate customer receipts.

### 📦 Inventory & Product Management
- **Product Tracking:** Add, edit, view, and delete products easily from the system.
- **Stock Control:** Track inventory levels and adjust quantities on the fly.
- **Low Stock Alerts:** Automatically monitor and highlight low-stock items so you never run out of essential supplies.
- **Categorization:** Organize items by categories and suppliers for seamless navigation.

### 📊 Dashboard & Reporting
- **Analytics Dashboard:** Get a bird's-eye view of your business performance with interactive charts and summaries.
- **Sales Reports:** Generate comprehensive reports on daily/monthly sales, profits, and transaction history.
- **Data-Driven Insights:** Make informed business decisions using real-time data metrics.

### 👥 Customer Management
- **Customer Profiles:** Maintain a database of your regular shoppers.
- **Purchase Tracking:** Keep track of customer orders and transaction history.

### 🔐 Security & Accounts
- **Role-Based Access:** Secure authentication system ensuring staff and admins only see what they need to.
- **Data Protection:** Built on Django's robust security framework.

---

## 🛠️ Technology Stack

- **Backend:** Python, Django 6.0
- **Database:** SQLite (Development) / PostgreSQL-ready (Production via dj-database-url)
- **Server/Deployment:** Gunicorn, Whitenoise
- **Image Processing:** Pillow

---

## 🚀 Getting Started

Follow these instructions to set up the project locally on your machine.

### Prerequisites

Ensure you have the following installed:
- [Python 3.x](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

### 1. Clone the Repository

```bash
git clone https://github.com/yanellebryan/Baskety.git
cd Baskety
```

### 2. Set Up a Virtual Environment

It is highly recommended to use a virtual environment to manage project dependencies.

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Navigate into the nested project directory (where `requirements.txt` lives) and install dependencies:
```bash
cd Baskety
pip install -r requirements.txt
```

### 4. Apply Database Migrations & Create Superuser

Initialize your local database and set up your admin account:
```bash
python manage.py migrate
python manage.py createsuperuser
```
Follow the prompts to configure your admin credentials.

### 5. Run the Application

You can start the server in two ways:

**Method 1: Using the automated runner script (from the project root)**
```bash
# Make sure you are in the outer 'Baskety' directory
python run.py
```

**Method 2: Using standard Django manage.py**
```bash
# Make sure you are in the inner 'Baskety' directory
python manage.py runserver
```

Open your web browser and navigate to `http://127.0.0.1:8000/`.

---

## 🤝 Workflow for Collaboration

To keep our codebase clean and organized, please follow this workflow when making contributions:

1. **Always pull the latest changes** from the `main` branch:
   ```bash
   git checkout main
   git pull origin main
   ```
2. **Create a new branch** for your feature or bug fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit your changes** with clear and concise messages:
   ```bash
   git add .
   git commit -m "Add new reporting feature for daily sales"
   ```
4. **Push your branch** to GitHub:
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Open a Pull Request (PR)** and request a review from your groupmates.

---
<div align="center">
  <p>Built with ❤️ by the Baskety Team</p>
</div>
