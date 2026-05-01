# 🛒 Amazon Price Tracker with Automated Email Alerts

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Active-success)
![Automation](https://img.shields.io/badge/Type-Automation-orange)
![Maintained](https://img.shields.io/badge/Maintained-Yes-brightgreen)
![PRs](https://img.shields.io/badge/PRs-Welcome-blue)
![Made By](https://img.shields.io/badge/Made%20By-Qusai%20Kagalwala-blueviolet)

---

## 📌 Overview

This project is a Python-based automation script that tracks the price of an Amazon product and sends an email notification when the price drops below a defined target.

It eliminates the need to manually check prices and ensures you never miss a deal.

---

## 🚀 Features

* 🔍 Real-time Amazon price scraping
* 💰 Accurate price extraction with currency support
* 📧 Automated email alerts via SMTP
* 🛡️ CAPTCHA detection to avoid blocked requests
* 🔐 Secure credential management using `.env`
* ⚙️ Modular and clean Python code structure

---

## 🧠 How It Works

1. Sends an HTTP request to the Amazon product page
2. Parses HTML using BeautifulSoup
3. Extracts product title and price
4. Compares price with user-defined target
5. Sends an email if the price drops

---

## 🧰 Tech Stack

* Python
* BeautifulSoup4
* Requests
* smtplib (SMTP)
* python-dotenv

---

## 📂 Project Structure

```bash
Amazon Price Tracker with Automated Email Alerts/
│
├── main.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/qusai-Kagal/DevVault.git
cd DevVault/scripts/Amazon\ Price\ Tracker\ with\ Automated\ Email\ Alerts
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install requests beautifulsoup4 python-dotenv
```

---

### 3️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

```env
SMTP_ADDRESS=smtp.gmail.com
EMAIL_ADDRESS=your-email@gmail.com
EMAIL_PASSWORD=your-app-password
```

> ⚠️ Use an App Password instead of your actual Gmail password.

---

### 4️⃣ Update Configuration

Inside `main.py`:

```python
PRODUCT_URL = "your-amazon-product-url"
TARGET_PRICE = 2000.0
```

---

### 5️⃣ Run the Script

```bash
python main.py
```

---

## 📸 Sample Output

```
Product: Concept Kart Headphones with Mic
Current Price: ₹2199.0
Price is still above target.
```

OR

```
Price dropped! Sending email...
```

---

## 🔒 Security Notes

* Do NOT upload your `.env` file to GitHub
* Always use `.gitignore` to protect credentials
* Use App Passwords for email authentication

---

## ⚠️ Disclaimer

* Amazon frequently changes its HTML structure, which may break scraping
* Too many requests may trigger CAPTCHA or IP blocking
* This project is for educational purposes only

---

## 🚀 Future Improvements

* ⏱️ Scheduled execution (cron jobs / task scheduler)
* 📊 Price history tracking with database
* 🤖 Telegram / Discord notifications
* 🌐 Web dashboard (Flask / MERN)
* 📦 Multi-product tracking support

---

## 👨‍💻 Author

**Qusai Kagalwala**

* GitHub: https://github.com/qusai-Kagalwala
* LinkedIn: https://www.linkedin.com/in/qusai-kagalwala/

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
