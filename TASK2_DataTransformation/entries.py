import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Database connection details from environment variables
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')

# Establish a database connection
connection = pymysql.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

try:
    with connection.cursor() as cursor:
        # Insert into 'users' table
        insert_user_query = """
        INSERT INTO users (user_id, name, email, age, signup_date)
        VALUES (%s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            name = VALUES(name),
            email = VALUES(email),
            age = VALUES(age),
            signup_date = VALUES(signup_date)
        """
        users_data = [
            (1, 'John Doe', 'john.doe@example.com', 28, '2023-01-15'),
            (2, 'Jane Smith', 'jane.smith@example.com', 34, '2023-02-20'),
            (3, 'Alice Johnson', 'alice.johnson@example.com', 22, '2023-03-10'),
            (4, 'Alice Smith', 'alice.smith@example.com', 30, '2024-01-15'),
            (5, 'Bob Johnson', 'bob.johnson@example.com', 45, '2024-02-20'),
            (6, 'Charlie Brown', 'charlie.brown@example.com', 25, '2024-03-10')
        ]
        cursor.executemany(insert_user_query, users_data)

        # Insert into 'bank_accounts' table
        insert_bank_account_query = """
        INSERT INTO bank_accounts (id, user_id, account_number, email, address, balance, debt)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            account_number = VALUES(account_number),
            email = VALUES(email),
            address = VALUES(address),
            balance = VALUES(balance),
            debt = VALUES(debt)
        """
        bank_accounts_data = [
            (1, 1, '1234567890', 'alice.smith@example.com', '123 Elm St, Springfield', 50000.00, 1500.00),
            (2, 2, '2345678901', 'bob.johnson@example.com', '456 Oak St, Springfield', 75000.00, 2500.00),
            (3, 3, '3456789012', 'charlie.brown@example.com', '789 Pine St, Springfield', 30000.00, 500.00),
            (4, 4, '1234567890', 'john.doe@example.com', '123 Main St', 100000.00, 0.00),
            (5, 5, '0987654321', 'jane.smith@example.com', '456 Oak St', 75000.00, 5000.00),
            (6, 6, '1122334455', 'alice.johnson@example.com', '789 Pine St', 50000.00, 10000.00)
        ]
        cursor.executemany(insert_bank_account_query, bank_accounts_data)

        # Commit the transaction
        connection.commit()

        print("Entries added successfully!")

finally:
    # Close the database connection
    connection.close()
