import pymysql
import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Database connection details
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')

# Establishing the connection using SQLAlchemy
engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}")

# Queries to fetch data
query_users = "SELECT * FROM users;"
query_bank_accounts = "SELECT * FROM bank_accounts;"

# Load data into Pandas DataFrame
df_users = pd.read_sql(query_users, engine)
df_bank_accounts = pd.read_sql(query_bank_accounts, engine)

# Remove duplicate rows based on all columns
df_users_cleaned = df_users.drop_duplicates()
df_bank_accounts_cleaned = df_bank_accounts.drop_duplicates()

# Handling missing values
df_users_cleaned['email'] = df_users_cleaned['email'].fillna('missing_email@example.com')
df_users_cleaned = df_users_cleaned.dropna(subset=['user_id'])
df_bank_accounts_cleaned = df_bank_accounts_cleaned.dropna(subset=['account_number'])

# Ensure 'signup_date' is in datetime format
df_users_cleaned['signup_date'] = pd.to_datetime(df_users_cleaned['signup_date'])

# Filter users by signup date
df_users_filtered = df_users_cleaned[df_users_cleaned['signup_date'] > pd.to_datetime('2022-01-01')]

# Compute derived columns
df_users_filtered['age_group'] = pd.cut(df_users_filtered['age'], bins=range(0, 101, 5), labels=[f'{i}-{i+4}' for i in range(0, 100, 5)])
df_bank_accounts_cleaned['balance_group'] = pd.cut(df_bank_accounts_cleaned['balance'], bins=range(0, 500001, 50000), labels=[f'{i}-{i+49999}' for i in range(0, 500000, 50000)])

# Data validation checks
valid_email = df_users_filtered['email'].str.contains(r'^[\w\.-]+@[\w\.-]+\.\w+$', na=False)
invalid_emails = df_users_filtered[~valid_email]
if not invalid_emails.empty:
    print("Invalid emails found:")
    print(invalid_emails)

valid_age = df_users_filtered[(df_users_filtered['age'] >= 0) & (df_users_filtered['age'] <= 100)]
invalid_age = df_users_filtered[~df_users_filtered.index.isin(valid_age.index)]
if not invalid_age.empty:
    print("Invalid age records found:")
    print(invalid_age)

# Convert DataFrames to JSON
df_users_filtered.to_json('filtered_users.json', orient='records', lines=True)
df_bank_accounts_cleaned.to_json('transformed_bank_accounts.json', orient='records', lines=True)

print("JSON files created successfully.")

# Alternatively, use the cleaned and transformed data for further processing
print("Users Data Table \n", df_users_filtered.head())
print("\n")
print("Bank Accounts Data Table \n", df_bank_accounts_cleaned.head())
