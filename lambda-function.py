import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('serverless-web-application-on-aws')

def lambda_handler(event, context):
    # Get item from DynamoDB table
    response = table.get_item(Key={'id': '0'})
    item = response.get('Item', {})
    
    # Increment views count
    views = item.get('views', 0) + 1
    
    # Update item in DynamoDB table
    table.put_item(Item={'id': '0', 'views': views})
    
    return {
        'statusCode': 200,
        'body': json.dumps({'views': views})
    }
