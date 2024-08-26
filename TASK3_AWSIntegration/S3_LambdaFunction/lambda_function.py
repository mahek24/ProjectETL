import json
import boto3
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize S3 client
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # Retrieve the S3 bucket name and object key from the event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    
    try:
        # Load the JSON file from S3
        response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
        file_content = response['Body'].read().decode('utf-8')
        
        # Process JSON Lines
        lines = file_content.strip().split('\n')
        data = [json.loads(line) for line in lines]
        
        # Process the JSON data
        age_group_counts = {}
        balance_group_counts = {}
        
        for record in data:
            age_group = record.get('age_group', 'unknown')
            balance_group = record.get('balance_group', 'unknown')
            
            if age_group not in age_group_counts:
                age_group_counts[age_group] = 0
            if balance_group not in balance_group_counts:
                balance_group_counts[balance_group] = 0
                
            age_group_counts[age_group] += 1
            balance_group_counts[balance_group] += 1
        
        # Log the results to CloudWatch
        logger.info(f'Age group counts: {age_group_counts}')
        logger.info(f'Balance group counts: {balance_group_counts}')
        
        return {
            'statusCode': 200,
            'body': json.dumps('Data processed successfully')
        }
    
    except Exception as e:
        logger.error(f'Error: {str(e)}')
        return {
            'statusCode': 500,
            'body': json.dumps('Error processing data')
        }
