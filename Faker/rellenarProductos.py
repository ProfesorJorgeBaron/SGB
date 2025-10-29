import mysql.connector
from faker import Faker

# Configuración de MySQL
config = {
    "user": "root",
    "password": "mi_password",
    "host": "localhost",
    "database": "prueba"
}

# Conectar a la base de datos
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

# Inicializar Faker
fake = Faker('es_ES')

# Número de productos que quieres generar
NUM_PRODUCTOS = 20

for _ in range(NUM_PRODUCTOS):
    nombre = fake.word().capitalize()  # Nombre aleatorio de producto
    stock = fake.random_int(min=0, max=1000)   # Stock aleatorio entre 0 y 1000

    cursor.execute(
        "INSERT INTO productos (nombre, stock) VALUES (%s, %s)",
        (nombre, stock)
    )

# Guardar los cambios
cnx.commit()
print(f"Se han insertado {NUM_PRODUCTOS} productos en la tabla 'productos'.")

# Cerrar conexión
cursor.close()
cnx.close()
