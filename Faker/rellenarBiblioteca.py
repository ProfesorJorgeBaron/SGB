import mysql.connector
from faker import Faker
import random

fake = Faker('es_ES')

config = {
    "user": "root",
    "password": "mi_password",
    "host": "localhost",
    "database": "biblioteca"
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

# Inserta datos falsos
def insertar_autores(n=20):
    for _ in range(n):
        cursor.execute(
            "INSERT INTO autores (nombre, nacionalidad, fecha_nacimiento) VALUES (%s, %s, %s)",
            (fake.name(), fake.country(), fake.date_of_birth(minimum_age=25, maximum_age=90))
        )

def insertar_categorias():
    categorias = ["Novela", "Ciencia", "Historia", "Infantil", "Terror", "Romántica"]
    for c in categorias:
        cursor.execute("INSERT INTO categorias (nombre) VALUES (%s)", (c,))

def insertar_editoriales(n=10):
    for _ in range(n):
        cursor.execute(
            "INSERT INTO editoriales (nombre, pais) VALUES (%s, %s)",
            (fake.company(), fake.country())
        )

def insertar_usuarios(n=30):
    for _ in range(n):
        cursor.execute(
            "INSERT INTO usuarios (nombre, email, telefono) VALUES (%s, %s, %s)",
            (fake.name(), fake.email(), fake.phone_number())
        )

def insertar_direcciones():
    cursor.execute("SELECT id FROM usuarios")
    usuarios = [row[0] for row in cursor.fetchall()]
    for uid in usuarios:
        cursor.execute(
            "INSERT INTO direcciones (id_usuario, calle, ciudad, codigo_postal) VALUES (%s, %s, %s, %s)",
            (uid, fake.street_address(), fake.city(), fake.postcode())
        )

def insertar_libros(n=50):
    cursor.execute("SELECT id FROM autores")
    autores = [a[0] for a in cursor.fetchall()]
    cursor.execute("SELECT id FROM categorias")
    categorias = [c[0] for c in cursor.fetchall()]
    for _ in range(n):
        cursor.execute(
            "INSERT INTO libros (titulo, id_autor, id_categoria, anio_publicacion, isbn) VALUES (%s, %s, %s, %s, %s)",
            (fake.sentence(nb_words=3), random.choice(autores), random.choice(categorias), random.randint(1950, 2024), fake.isbn13())
        )

def insertar_libros_editoriales():
    cursor.execute("SELECT id FROM libros")
    libros = [l[0] for l in cursor.fetchall()]
    cursor.execute("SELECT id FROM editoriales")
    editoriales = [e[0] for e in cursor.fetchall()]
    for libro in libros:
        cursor.execute(
            "INSERT INTO libros_editoriales (id_libro, id_editorial) VALUES (%s, %s)",
            (libro, random.choice(editoriales))
        )

def insertar_prestamos(n=40):
    cursor.execute("SELECT id FROM usuarios")
    usuarios = [u[0] for u in cursor.fetchall()]
    cursor.execute("SELECT id FROM libros")
    libros = [l[0] for l in cursor.fetchall()]
    for _ in range(n):
        f1 = fake.date_this_year()
        f2 = fake.date_between(start_date=f1)
        cursor.execute(
            "INSERT INTO prestamos (id_usuario, id_libro, fecha_prestamo, fecha_devolucion) VALUES (%s, %s, %s, %s)",
            (random.choice(usuarios), random.choice(libros), f1, f2)
        )

def insertar_resenas(n=50):
    cursor.execute("SELECT id FROM usuarios")
    usuarios = [u[0] for u in cursor.fetchall()]
    cursor.execute("SELECT id FROM libros")
    libros = [l[0] for l in cursor.fetchall()]
    for _ in range(n):
        cursor.execute(
            "INSERT INTO resenas (id_libro, id_usuario, puntuacion, comentario) VALUES (%s, %s, %s, %s)",
            (random.choice(libros), random.choice(usuarios), random.randint(1, 5), fake.sentence(nb_words=10))
        )

def insertar_empleados(n=10):
    puestos = ["Bibliotecario", "Archivista", "Administrador", "Auxiliar"]
    for _ in range(n):
        cursor.execute(
            "INSERT INTO empleados (nombre, puesto) VALUES (%s, %s)",
            (fake.name(), random.choice(puestos))
        )

# Orden lógico de inserción
insertar_autores()
insertar_categorias()
insertar_editoriales()
insertar_usuarios()
insertar_direcciones()
insertar_libros()
insertar_libros_editoriales()
insertar_prestamos()
insertar_resenas()
insertar_empleados()

cnx.commit()
print("Tablas rellenadas con datos falsos correctamente.")

cursor.close()
cnx.close()
