import redis

#creamos las conexiones
conexionRedis = redis.ConnectionPool(host='localhost', port=6370, db=0,decode_responses=True)
baseDatosRedis = redis.Redis(connection_pool=conexionRedis)

# Obtiene todas las claves
claves = baseDatosRedis.keys()

# Mostramos la clave y su valor
for clave in claves:
  print('Clave:', clave , ' y Valor: ', baseDatosRedis.get(clave))