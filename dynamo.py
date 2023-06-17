import boto3

dynamodb = boto3.client('dynamodb', region_name='YOUR_REGION_NAME')

# Create the RealEstateListings table
response = dynamodb.create_table(
    TableName='RealEstateListings',
    AttributeDefinitions=[
        {
            'AttributeName': 'listing_id',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'price',
            'AttributeType':'S'
        }
    ],
    KeySchema=[
        {
            'AttributeName': 'listing_id',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'price',
            'KeyType': 'RANGE'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    },
    AttributeDefinitions=[
        {
            'AttributeName': 'location',
            'AttributeType': 'S'
        }
    ],
    GlobalSecondaryIndexes=[
        {
            'IndexName': 'LocationIndex',
            'KeySchema': [
                {
                    'AttributeName': 'location',
                    'KeyType': 'HASH'
                }
            ],
            'Projection': {
                'ProjectionType': 'ALL'
            },
            'ProvisionedThroughput': {
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        }
    ]
)

print("RealEstateListings table created successfully.")
