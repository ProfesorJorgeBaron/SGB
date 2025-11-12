from conectarse import * 

dynamodb = conectarseDynamoDBCliente()

tabla = "ejemplo_tabla_libros"

dynamodb.delete_table(TableName=tabla)

waiter = dynamodb.get_waiter('table_not_exists')
waiter.wait(TableName=tabla)

print(dynamodb.list_tables())