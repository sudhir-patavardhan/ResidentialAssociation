import json

def handler(event, context):
    # Log the event argument for debugging and for use in local development.
    print(json.dumps(event))
    plotNumber = event['pathParameters']['plotNumber']

    return {
        'statusCode': 200,
        'body': json.dumps({
            'plotNumber': plotNumber
        })
    }