import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv()

def create_bd(endpoint):

    # Configura la conexión a MySQL
    config = {
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "host": endpoint
    }

    DB_NAME = os.getenv("DB_NAME")

    # Definición de las tablas
    TABLES = {}
    TABLES['autores'] = (
        "CREATE TABLE IF NOT EXISTS autores ("
        " id INT AUTO_INCREMENT PRIMARY KEY,"
        " nombre VARCHAR(100) NOT NULL,"
        " nacionalidad VARCHAR(100),"
        " fecha_nacimiento DATE)"
    )

    TABLES['categorias'] = (
        "CREATE TABLE IF NOT EXISTS categorias ("
        " id INT AUTO_INCREMENT PRIMARY KEY,"
        " nombre VARCHAR(100) NOT NULL)"
    )

    TABLES['libros'] = (
        "CREATE TABLE IF NOT EXISTS libros ("
        " id INT AUTO_INCREMENT PRIMARY KEY,"
        " titulo VARCHAR(200) NOT NULL,"
        " id_autor INT,"
        " id_categoria INT,"
        " anio_publicacion INT,"
        " isbn VARCHAR(20),"
        " FOREIGN KEY (id_autor) REFERENCES autores(id),"
        " FOREIGN KEY (id_categoria) REFERENCES categorias(id))"
    )

    TABLES['usuarios'] = (
        "CREATE TABLE IF NOT EXISTS usuarios ("
        " id INT AUTO_INCREMENT PRIMARY KEY,"
        " nombre VARCHAR(100),"
        " email VARCHAR(100),"
        " telefono VARCHAR(20))"
    )

    TABLES['direcciones'] = (
        "CREATE TABLE IF NOT EXISTS direcciones ("
        " id INT AUTO_INCREMENT PRIMARY KEY,"
        " id_usuario INT,"
        " calle VARCHAR(200),"
        " ciudad VARCHAR(100),"
        " codigo_postal VARCHAR(10),"
        " FOREIGN KEY (id_usuario) REFERENCES usuarios(id))"
    )

    TABLES['prestamos'] = (
        "CREATE TABLE IF NOT EXISTS prestamos ("
        " id INT AUTO_INCREMENT PRIMARY KEY,"
        " id_usuario INT,"
        " id_libro INT,"
        " fecha_prestamo DATE,"
        " fecha_devolucion DATE,"
        " FOREIGN KEY (id_usuario) REFERENCES usuarios(id),"
        " FOREIGN KEY (id_libro) REFERENCES libros(id))"
    )

    TABLES['editoriales'] = (
        "CREATE TABLE IF NOT EXISTS editoriales ("
        " id INT AUTO_INCREMENT PRIMARY KEY,"
        " nombre VARCHAR(100) NOT NULL,"
        " pais VARCHAR(100))"
    )

    TABLES['libros_editoriales'] = (
        "CREATE TABLE IF NOT EXISTS libros_editoriales ("
        " id_libro INT,"
        " id_editorial INT,"
        " PRIMARY KEY (id_libro, id_editorial),"
        " FOREIGN KEY (id_libro) REFERENCES libros(id),"
        " FOREIGN KEY (id_editorial) REFERENCES editoriales(id))"
    )

    TABLES['resenas'] = (
        "CREATE TABLE IF NOT EXISTS resenas ("
        " id INT AUTO_INCREMENT PRIMARY KEY,"
        " id_libro INT,"
        " id_usuario INT,"
        " puntuacion INT,"
        " comentario TEXT,"
        " FOREIGN KEY (id_libro) REFERENCES libros(id),"
        " FOREIGN KEY (id_usuario) REFERENCES usuarios(id))"
    )

    TABLES['empleados'] = (
        "CREATE TABLE IF NOT EXISTS empleados ("
        " id INT AUTO_INCREMENT PRIMARY KEY,"
        " nombre VARCHAR(100),"
        " puesto VARCHAR(100))"
    )

    # Conexión y creación
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    cursor.execute(f"USE {DB_NAME}")

    for name, ddl in TABLES.items():
        print(f"Creando tabla {name}...")
        cursor.execute(ddl)

    print("Base de datos y tablas creadas correctamente.")

    cursor.close()
    cnx.close()