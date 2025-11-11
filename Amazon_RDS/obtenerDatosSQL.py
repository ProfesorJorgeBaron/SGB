import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv()

import decimal
import json

def ejecutar_consultas(endpoint):
    
     # Configura la conexión a MySQL
    config = {
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "host": endpoint
        
    }
    DB_NAME = os.getenv("DB_NAME")
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(f"USE {DB_NAME}")
    resultados = {}

    # 1. Listar todos los libros con su autor y categoría
    #    Muestra el título, autor, categoría y año de publicación.
    cursor.execute("""
        SELECT l.id, l.titulo, a.nombre AS autor, c.nombre AS categoria, l.anio_publicacion
        FROM libros l
        JOIN autores a ON l.id_autor = a.id
        JOIN categorias c ON l.id_categoria = c.id
        ORDER BY l.titulo;
    """)
    resultados["libros_con_autor_categoria"] = cursor.fetchall()

    # 2. Contar cuántos libros tiene cada autor
    cursor.execute("""
        SELECT a.nombre AS autor, COUNT(l.id) AS cantidad_libros
        FROM autores a
        LEFT JOIN libros l ON a.id = l.id_autor
        GROUP BY a.id
        ORDER BY cantidad_libros DESC;
    """)
    resultados["libros_por_autor"] = cursor.fetchall()

    # 3. Libros publicados después del año 2000 con su categoría
    cursor.execute("""
        SELECT l.titulo, l.anio_publicacion, c.nombre AS categoria
        FROM libros l
        JOIN categorias c ON l.id_categoria = c.id
        WHERE l.anio_publicacion > 2000
        ORDER BY l.anio_publicacion;
    """)
    resultados["libros_recientes"] = cursor.fetchall()

    # 4. Top 5 autores con más préstamos
    cursor.execute("""
        SELECT a.nombre AS autor, COUNT(p.id) AS total_prestamos
        FROM autores a
        JOIN libros l ON a.id = l.id_autor
        JOIN prestamos p ON p.id_libro = l.id
        GROUP BY a.id
        ORDER BY total_prestamos DESC
        LIMIT 5;
    """)
    resultados["autores_mas_prestados"] = cursor.fetchall()

    # 5. Libros que nunca han sido prestados
    cursor.execute("""
        SELECT l.titulo, a.nombre AS autor
        FROM libros l
        JOIN autores a ON a.id = l.id_autor
        LEFT JOIN prestamos p ON p.id_libro = l.id
        WHERE p.id IS NULL;
    """)
    resultados["libros_nunca_prestados"] = cursor.fetchall()

    # 6. Número total de préstamos por año
    cursor.execute("""
        SELECT YEAR(fecha_prestamo) AS anio, COUNT(*) AS total_prestamos
        FROM prestamos
        GROUP BY YEAR(fecha_prestamo)
        ORDER BY anio;
    """)
    resultados["prestamos_por_anio"] = cursor.fetchall()

    # 7. Promedio de libros por categoría
    cursor.execute("""
        SELECT ROUND(AVG(cantidad), 2) AS promedio_libros_por_categoria
        FROM (
            SELECT COUNT(*) AS cantidad
            FROM libros
            GROUP BY id_categoria
        ) sub;
    """)
    resultados["promedio_libros_categoria"] = cursor.fetchall()

    # 8. Libros con más de una reseña y su puntuación media
    cursor.execute("""
        SELECT l.titulo, COUNT(r.id) AS num_resenas, ROUND(AVG(r.puntuacion), 2) AS media_puntuacion
        FROM libros l
        JOIN resenas r ON l.id = r.id_libro
        GROUP BY l.id
        HAVING COUNT(r.id) > 1
        ORDER BY media_puntuacion DESC;
    """)
    resultados["libros_con_multiples_resenas"] = cursor.fetchall()

    # 9. Usuarios con más préstamos y su ciudad
    cursor.execute("""
        SELECT u.nombre AS usuario, d.ciudad, COUNT(p.id) AS total_prestamos
        FROM usuarios u
        JOIN prestamos p ON u.id = p.id_usuario
        LEFT JOIN direcciones d ON u.id = d.id_usuario
        GROUP BY u.id
        ORDER BY total_prestamos DESC
        LIMIT 10;
    """)
    resultados["usuarios_mas_prestamos"] = cursor.fetchall()

    # 10. Editoriales con más libros publicados
    cursor.execute("""
        SELECT e.nombre AS editorial, COUNT(le.id_libro) AS cantidad_libros
        FROM editoriales e
        JOIN libros_editoriales le ON e.id = le.id_editorial
        GROUP BY e.id
        ORDER BY cantidad_libros DESC
        LIMIT 5;
    """)
    resultados["editoriales_con_mas_libros"] = cursor.fetchall()
    guardar_resultados(resultados)
    cnx.close()
    return resultados

# --------------------------------------------------
# GUARDAR RESULTADOS EN JSON INDIVIDUALES
# --------------------------------------------------
def guardar_resultados(resultados):
    """Guarda cada consulta en un archivo JSON separado dentro de la carpeta 'resultados'."""
    carpeta = "resultados"
    os.makedirs(carpeta, exist_ok=True)

    for nombre, datos in resultados.items():
        ruta = os.path.join(carpeta, f"{nombre}.json")

        # Convertir Decimals a float
        datos_convertidos = []
        for fila in datos:
            fila_conv = {k: (float(v) if isinstance(v, decimal.Decimal) else v) for k, v in fila.items()}
            datos_convertidos.append(fila_conv)

        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(datos_convertidos, f, indent=4, ensure_ascii=False)

        print(f"Archivo guardado: {ruta} ({len(datos_convertidos)} filas)")
