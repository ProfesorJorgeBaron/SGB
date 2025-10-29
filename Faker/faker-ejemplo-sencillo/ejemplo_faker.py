from faker import Faker
import psycopg2
import mysql.connector

faker = Faker('es_ES')  # Para nombres y DNIs en español

# Conexión a PostgreSQL
pg_conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="basededatos_pg",
    user="usuario_pg",
    password="pass_pg"
)
pg_cursor = pg_conn.cursor()

# Crear tabla usuario si no existe
pg_cursor.execute("""
CREATE TABLE IF NOT EXISTS usuario (
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    edad INT,
    dni VARCHAR(20) PRIMARY KEY
);
""")
pg_conn.commit()

# Conexión a MySQL
mysql_conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="basededatos_mysql",
    user="usuario_mysql",
    password="pass_mysql"
)
mysql_cursor = mysql_conn.cursor()

# Crear tabla datosUsuario si no existe
mysql_cursor.execute("""
CREATE TABLE IF NOT EXISTS datosUsuario (
    dni VARCHAR(20) PRIMARY KEY,
    telefono VARCHAR(20),
    email VARCHAR(100)
);
""")
mysql_conn.commit()

# Generar e insertar datos
for _ in range(10):
    nombre = faker.first_name()
    apellido = faker.last_name()
    edad = faker.random_int(min=18, max=80)
    dni = faker.unique.nif()
    telefono = faker.phone_number()
    email = faker.email()

    # Insertar en PostgreSQL
    pg_cursor.execute("""
        INSERT INTO usuario (nombre, apellido, edad, dni)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (dni) DO NOTHING;
    """, (nombre, apellido, edad, dni))

    # Insertar en MySQL
    mysql_cursor.execute("""
        INSERT IGNORE INTO datosUsuario (dni, telefono, email)
        VALUES (%s, %s, %s);
    """, (dni, telefono, email))

# Confirmar cambios y cerrar conexiones
pg_conn.commit()
mysql_conn.commit()
pg_cursor.close()
pg_conn.close()
mysql_cursor.close()
mysql_conn.close()

print("Datos insertados con éxito en PostgreSQL y MySQL 🎉")
