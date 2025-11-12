from conectarse import * 

dynamodb = conectarseDynamoDBCliente()

tabla = dynamodb.create_table(
    TableName='ejemplo_tabla_libros',
    AttributeDefinitions=[
        {'AttributeName': 'autor', 'AttributeType': 'S'},   # Partition Key
        {'AttributeName': 'anyo_publicacion', 'AttributeType': 'S'}, # Sort Key tabla principal
        {'AttributeName': 'precio', 'AttributeType': 'N'}  # Sort Key LSI
    ],
    KeySchema=[
        {'AttributeName': 'autor', 'KeyType': 'HASH'}, # Partition Key
        {'AttributeName': 'anyo_publicacion', 'KeyType': 'RANGE'} # Sort Key tabla principal
    ],
    LocalSecondaryIndexes=[
        {
            'IndexName': 'PrecioIndex', # Sort Key LSI
            'KeySchema': [
                {'AttributeName': 'autor', 'KeyType': 'HASH'},
                {'AttributeName': 'precio', 'KeyType': 'RANGE'}
            ],
            'Projection': {
                'ProjectionType': 'ALL' # Puede ser ALL, KEYS_ONLY o INCLUDE
            }
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5, #Numero de lecturas por segundo
        'WriteCapacityUnits': 5 #Numero de escrituras por segundo
    }
)

print(dynamodb.list_tables())