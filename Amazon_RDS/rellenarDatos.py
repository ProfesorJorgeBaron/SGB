import mysql.connector
from faker import Faker
import random
from dotenv import load_dotenv
import os
load_dotenv()

def rellenar_datos(endpoint):
    fake = Faker('es_ES')

    config = {
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "host": endpoint,
        "database": os.getenv("DB_NAME")
    }

    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    

    for _ in range(20):
        try:
            cursor.execute(
                "INSERT INTO autores (nombre, nacionalidad, fecha_nacimiento) VALUES (%s, %s, %s)",
                (fake.name(), fake.country(), fake.date_of_birth(minimum_age=25, maximum_age=90))
            )
        except mysql.connector.Error as err:
            print(f"Error al insertar autor: {err}")
            

    categorias = ["Novela", "Ciencia", "Historia", "Infantil", "Terror", "Romántica"]
    for c in categorias:
        try:
            cursor.execute("INSERT INTO categorias (nombre) VALUES (%s)", (c,))
        except mysql.connector.Error as err:
            print(f"Error al insertar categorias: {err}")

    for _ in range(10):
        try:
            cursor.execute(
                "INSERT INTO editoriales (nombre, pais) VALUES (%s, %s)",
                (fake.company(), fake.country())
            )
        except mysql.connector.Error as err:
            print(f"Error al insertar editoriales: {err}")

    for _ in range(30):
        try:
            cursor.execute(
                "INSERT INTO usuarios (nombre, email, telefono) VALUES (%s, %s, %s)",
                (fake.name(), fake.email(), fake.phone_number())
            )
        except mysql.connector.Error as err:
            print(f"Error al insertar usuarios: {err}")

    cursor.execute("SELECT id FROM usuarios")
    usuarios = [row[0] for row in cursor.fetchall()]
    for uid in usuarios:
        try:
            cursor.execute(
                "INSERT INTO direcciones (id_usuario, calle, ciudad, codigo_postal) VALUES (%s, %s, %s, %s)",
                (uid, fake.street_address(), fake.city(), fake.postcode())
            )
        except mysql.connector.Error as err:
            print(f"Error al insertar direcciones: {err}")


    cursor.execute("SELECT id FROM autores")
    autores = [a[0] for a in cursor.fetchall()]
    cursor.execute("SELECT id FROM categorias")
    categorias = [c[0] for c in cursor.fetchall()]
    for _ in range(50):
        try:
            cursor.execute(
                "INSERT INTO libros (titulo, id_autor, id_categoria, anio_publicacion, isbn) VALUES (%s, %s, %s, %s, %s)",
                (fake.sentence(nb_words=3), random.choice(autores), random.choice(categorias), random.randint(1950, 2024), fake.isbn13())
            )
        except mysql.connector.Error as err:
            print(f"Error al insertar libros: {err}")

    cursor.execute("SELECT id FROM libros")
    libros = [l[0] for l in cursor.fetchall()]
    cursor.execute("SELECT id FROM editoriales")
    editoriales = [e[0] for e in cursor.fetchall()]
    for libro in libros:
        try:
            cursor.execute(
                "INSERT INTO libros_editoriales (id_libro, id_editorial) VALUES (%s, %s)",
                (libro, random.choice(editoriales))
            )
        except mysql.connector.Error as err:
            print(f"Error al insertar libros_editoriales: {err}")

    cursor.execute("SELECT id FROM usuarios")
    usuarios = [u[0] for u in cursor.fetchall()]
    cursor.execute("SELECT id FROM libros")
    libros = [l[0] for l in cursor.fetchall()]
    for _ in range(40):
        f1 = fake.date_this_year()
        f2 = fake.date_between(start_date=f1)
        try:
            cursor.execute(
                "INSERT INTO prestamos (id_usuario, id_libro, fecha_prestamo, fecha_devolucion) VALUES (%s, %s, %s, %s)",
                (random.choice(usuarios), random.choice(libros), f1, f2)
            )
        except mysql.connector.Error as err:
            print(f"Error al insertar prestamos: {err}")

    cursor.execute("SELECT id FROM usuarios")
    usuarios = [u[0] for u in cursor.fetchall()]
    cursor.execute("SELECT id FROM libros")
    libros = [l[0] for l in cursor.fetchall()]
    for _ in range(50):
        try:
            cursor.execute(
                "INSERT INTO resenas (id_libro, id_usuario, puntuacion, comentario) VALUES (%s, %s, %s, %s)",
                (random.choice(libros), random.choice(usuarios), random.randint(1, 5), fake.sentence(nb_words=10))
            )
        except mysql.connector.Error as err:
            print(f"Error al insertar resenas: {err}")

    puestos = ["Bibliotecario", "Archivista", "Administrador", "Auxiliar"]
    for _ in range(10):
        try:
            cursor.execute(
                "INSERT INTO empleados (nombre, puesto) VALUES (%s, %s)",
                (fake.name(), random.choice(puestos))
            )
        except mysql.connector.Error as err:
            print(f"Error al insertar empleados: {err}")


    cnx.commit()
    print("Tablas rellenadas con datos falsos correctamente.")

    cursor.close()
    cnx.close()