import boto3

def handler(event, context):
    # Extract plot details from the event
    plot_details = {
        'plotNumber': event['plotNumber'],
        'ownerName': event['ownerName'],
        'dimensions': event['dimensions'],
        'area': event['area'],
        'ownershipStartDate': event['ownershipStartDate'],
        'releaseStatus': event['releaseStatus']
    }

    # Insert plot details into DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('SMVRL-plot-LJC9WGC4FCR')
    table.put_item(Item=plot_details)

    return {
        'statusCode': 200,
        'body': 'Plot details inserted successfully'
    }