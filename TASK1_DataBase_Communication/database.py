import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Step 1: Connect to the MySQL database
conn = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_NAME')
)

cursor = conn.cursor()

# Step 2: Create the 'users' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    age INT,
    signup_date DATE
)
''')

# Step 3: Create the 'bank_accounts' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS bank_accounts (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    account_number VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    address VARCHAR(255),
    balance DECIMAL(15, 2),
    debt DECIMAL(15, 2),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
)
''')

# Step 4: Commit the changes to save the tables
conn.commit()

# Step 5: Close the connection
cursor.close()
conn.close()

print("Database and tables created successfully.")
