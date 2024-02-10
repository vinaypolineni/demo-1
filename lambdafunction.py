import json

def lambda_handler(event, context):
    # TODO implement
    print ("hello world i'm from vs code")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
