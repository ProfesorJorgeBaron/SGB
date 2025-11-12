from conectarse import * 


dynamodb = conectarseDynamoDBCliente()

tabla = dynamodb.create_table(
    TableName='ejemplo_tabla_libros',
    AttributeDefinitions=[
        {'AttributeName': 'autor', 'AttributeType': 'S'},   # Partition Key
        {'AttributeName': 'anyo_publicacion', 'AttributeType': 'S'}     # Sort Key
    ],
    KeySchema=[
        {'AttributeName': 'autor', 'KeyType': 'HASH'},  # Partition Key
        {'AttributeName': 'anyo_publicacion', 'KeyType': 'RANGE'}   # Sort Key
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5, #Numero de lecturas por segundo
        'WriteCapacityUnits': 5 #Numero de escrituras por segundo
    }
)

print(dynamodb.list_tables())