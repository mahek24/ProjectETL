# ETL Project

Here's a basic `README.md` template you can use for your project:

## Overview
The project involves creating a small ETL pipeline using Python, AWS services, and an SQL database, with a focus on implementing object-oriented principles and security measures.


### Prerequisites
- Python 3.12
- AWS account with access to necessary services
- MySQL database setup
- Virtual environment (optional, but recommended)

### Installation
1. **Clone the repository:**

   git clone https://github.com/mahek24/ProjectETL


2. **Set up environment variables:**
   - Create a `.env` file in the root directory with the following variables:
    
     - DB_HOST=your-database-host
     - DB_USER=your-database-user
     - DB_PASSWORD=your-database-password
     - DB_NAME=your-database-name
     - AWS_ACCESS_KEY_ID=your-aws-access-key-id
     - AWS_SECRET_ACCESS_KEY=your-aws-secret-access-key


### Running the Project

. **Expected Output:**
   - The script will connect to the MySQL database, perform data transformations, and store the results in the specified S3 bucket.

### Troubleshooting
- **Database Connection Issues:**
  - Ensure that your `.env` file is correctly configured with the right credentials.
  
- **AWS Permissions:**
  - Ensure that your IAM role has the necessary permissions to perform the required AWS operations.

## Additional Information
- **Security:** The project follows best practices for securing AWS resources and database connections.
- **Assumptions:** The project assumes that all AWS resources and MySQL database are correctly configured and accessible.

## Contact
For any questions or clarifications, please contact me at mahekrjain2401@gmail.com.
