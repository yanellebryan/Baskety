<div align="center">
  <h1>🛒 Baskety</h1>
  <p><em>A modern, comprehensive Point-of-Sale (POS) and Inventory Management System built with Django.</em></p>
  
  [![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
  [![Django](https://img.shields.io/badge/Django-Web_Framework-092E20.svg?logo=django)](https://www.djangoproject.com/)
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
</div>

---

Welcome to **Baskety**, a powerful and intuitive Point-of-Sale (POS) and inventory management system designed specifically for mini-marts, grocery stores, and small retail shops. Baskety streamlines your daily operations, from tracking stock levels to processing lightning-fast checkout transactions.

## ✨ Key Features

- 📊 **Interactive Dashboard**: Get a bird's-eye view of your business with real-time analytics, sales summaries, and inventory alerts.
- 📦 **Smart Inventory Control**: Monitor stock levels, track low-stock items automatically, and never run out of your best-sellers.
- 🏷️ **Comprehensive Product Management**: Easily add, categorize, edit, and organize your products and suppliers.
- 💻 **Modern Point of Sale (POS)**: A clean, user-friendly interface tailored for fast-paced retail environments. Designed for rapid scanning and seamless checkout.
- 📈 **Detailed Reporting**: Generate insightful reports on daily sales, revenue trends, and inventory status to make data-driven decisions.
- 🔐 **Role-Based Access Control**: Secure authentication with specific roles (Admin, Manager, Cashier) to protect sensitive business data.

## 🛠️ Technology Stack

- **Backend:** Python, Django
- **Database:** SQLite (Development) / PostgreSQL (Production Ready)
- **Frontend:** HTML5, CSS3, JavaScript, TailwindCSS

---

## 🚀 Getting Started

Follow these instructions to set up Baskety on your local machine for development and testing.

### Prerequisites

Ensure you have the following installed on your system:
- [Python 3.8+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

### Installation Guide

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yanellebryan/Baskety.git
   cd Baskety
   ```

2. **Set up a virtual environment:**
   - **Windows:**
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install dependencies:**
   ```bash
   pip install -r Baskety/requirements.txt
   ```
   *(Note: Navigate to the inner `Baskety` directory if that is where `requirements.txt` is located.)*

4. **Apply database migrations:**
   ```bash
   cd Baskety
   python manage.py migrate
   ```

5. **Create a superuser account:**
   ```bash
   python manage.py createsuperuser
   ```
   *(Follow the prompts to set up your admin credentials.)*

6. **Start the development server:**
   ```bash
   python manage.py runserver
   ```
   *Navigate to `http://127.0.0.1:8000/` in your browser to see Baskety in action!*

---

## 🤝 Contributing

We welcome contributions! To keep our codebase clean and organized, please follow this collaborative workflow:

1. **Pull the latest changes** from the `main` branch before starting:
   ```bash
   git checkout main
   git pull origin main
   ```
2. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-awesome-feature
   ```
3. **Commit your changes** with clear and descriptive messages:
   ```bash
   git commit -m "Add new daily sales reporting chart"
   ```
4. **Push your branch:**
   ```bash
   git push origin feature/your-awesome-feature
   ```
5. **Open a Pull Request (PR)** on GitHub and request a review from the team.

---

<div align="center">
  <p>Built with ❤️ by the Baskety Team. Let's build something great together!</p>
</div>
