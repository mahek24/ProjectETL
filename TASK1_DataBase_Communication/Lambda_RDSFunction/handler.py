import json
import pymysql
import os

def lambda_handler(event, context):
    # Retrieve database connection parameters from environment variables
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_name = os.getenv('DB_NAME')

    
    try:
        # Connect to the RDS instance
        connection = pymysql.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )
        
        with connection.cursor() as cursor:
            # Query the database
            cursor.execute("SELECT * FROM users")
            result = cursor.fetchall()

            # Prepare the response
            users = [dict(zip([column[0] for column in cursor.description], row)) for row in result]

            return {
                'statusCode': 200,
                'body': json.dumps(users, default=str)
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
    finally:
        connection.close()
