import json

def lambda_handler(event, context):
    # Print "Hello" to the CloudWatch Logs
    print("Two")
    
    # Return a response
    return {
        'statusCode': 200,
        'body': json.dumps('Two')
    }

