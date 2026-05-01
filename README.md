# 🔐 Login Monitoring & Alert System

## 📌 Description

This Python project is a simple login monitoring system that uses a MySQL database to store user credentials and the Telegram Bot API to send alerts. It verifies user login, sends IP and location details on successful login, and alerts + logs unauthorized access attempts.

---

## 🚀 Features

* MySQL database connectivity
* Login verification system
* IP & location tracking (via ipinfo.io)
* Telegram alerts for:

  * Successful login ✅
  * Unauthorized attempts ⚠️
* Logging suspicious activity in database

---

## 🛠️ Installation & Setup

### 1. Install Python

Download and install Python (3.8+)

```bash
python --version
```

---

### 2. Install MySQL Server

* Install MySQL Server
* Start MySQL service
* Verify:

```sql
SHOW DATABASES;
```

---

### 3. Install Required Libraries

```bash
pip install mysql-connector-python python-telegram-bot requests
```

---

### 4. Configure MySQL Connection

Update credentials in code:

```python
host="localhost"
user="root"
password="12345"
```

---

### 5. Create Telegram Bot

* Open Telegram
* Search **@BotFather**
* Create a bot and copy the token

Replace in code:

```python
bot = Bot(token="YOUR_BOT_TOKEN")
```

---

### 6. Get Chat ID

* Send a message to your bot
* Use `getUpdates` to find your chat_id

Replace in code:

```python
chat_id="YOUR_CHAT_ID"
```

---

### 7. Run the Program

```bash
python filename.py
```

---

## 🧪 How It Works

* Prompts user to enter password
* Compares with stored database password
* If correct:

  * Sends login success message + IP details
* If incorrect:

  * Sends alert message
  * Stores attempt details in database

---

## ⚠️ Limitations

* Password stored in plain text (not secure)
* Credentials and tokens are hardcoded
* Basic authentication (no username check)

---

## 💡 Future Improvements

* Use hashed passwords (bcrypt)
* Add username/email login
* Store secrets using `.env`
* Improve UI/UX

---

## 📂 Tech Stack

* Python
* MySQL
* Telegram Bot API
* Requests (API calls)

---

## 👨‍💻 Author

Shankar D
