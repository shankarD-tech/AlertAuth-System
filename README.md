🔹 Step 1: Install Python
Download and install Python (3.8 or above)
Verify installation:
python --version
🔹 Step 2: Install MySQL Server
Install MySQL Server on your system
Start the MySQL service
Open MySQL and verify:
SHOW DATABASES;
🔹 Step 3: Install Required Python Packages

Run this command in terminal:

pip install mysql-connector-python python-telegram-bot requests
🔹 Step 4: Setup MySQL Connectivity
Ensure your credentials match:
host="localhost"
user="root"
password="12345"
Your code will automatically:
Create database alert
Create required tables
🔹 Step 5: Create Telegram Bot
Open Telegram
Search for @BotFather
Create a bot and copy the Bot Token
Replace in code:
bot = Bot(token="YOUR_TOKEN")
🔹 Step 6: Get Chat ID
Message your bot
Use tools like getUpdates or a bot to find your chat_id
Replace in code:
chat_id="YOUR_CHAT_ID"
🔹 Step 7: Run the Program
python filename.py
🔹 Step 8: Test
Enter correct password → ✅ success message on Telegram
Enter wrong password → ⚠️ alert + stored in database
