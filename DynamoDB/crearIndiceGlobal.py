from conectarse import * 

dynamodb = conectarseDynamoDBCliente()

dynamodb.update_table(
    TableName='ejemplo_tabla_libros',
    AttributeDefinitions=[
        {'AttributeName': 'genero', 'AttributeType': 'S'},
        {'AttributeName': 'titulo', 'AttributeType': 'S'}
    ],
    GlobalSecondaryIndexUpdates=[
        {
            'Create': {
                'IndexName': 'GeneroTituloIndex',
                'KeySchema': [
                    {'AttributeName': 'genero', 'KeyType': 'HASH'},
                    {'AttributeName': 'titulo', 'KeyType': 'RANGE'}
                ],
                'Projection': {
                    'ProjectionType': 'ALL'
                },
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5
                }
            }
        }
    ]
)
print(dynamodb.list_tables())