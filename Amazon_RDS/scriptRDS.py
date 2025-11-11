from crearRDS import create_rds_instance
from crearBD import create_bd
from rellenarDatos import rellenar_datos
from obtenerDatosSQL import ejecutar_consultas

print("Iniciando proceso")
endpoint = create_rds_instance()
create_bd(endpoint)
#rellenar_datos(endpoint)
ejecutar_consultas(endpoint)
print("Proceso finalizado")
