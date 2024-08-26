import boto3
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# AWS S3 configuration
s3_bucket = os.getenv('S3_BUCKET')
s3_key_users = os.getenv('S3_KEY_USERS')
s3_key_bank_accounts = os.getenv('S3_KEY_BANK_ACCOUNTS')


# Initialize S3 client
s3_client = boto3.client('s3')

# Upload the JSON files
s3_client.upload_file(r'C:\Users\LENOVO\source\repos\VepoLink_Assessment\TASK3_AWSIntegration\filtered_users.json', s3_bucket, s3_key_users)
s3_client.upload_file(r'C:\Users\LENOVO\source\repos\VepoLink_Assessment\TASK3_AWSIntegration\transformed_bank_accounts.json', s3_bucket, s3_key_bank_accounts)

print("Files uploaded successfully to S3.")
