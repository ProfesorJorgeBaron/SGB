import redis

#creamos las conexiones
conexionRedis = redis.ConnectionPool(host='localhost', port=6379, db=0,decode_responses=True)
baseDatosRedis = redis.Redis(connection_pool=conexionRedis)

# Obtiene todas las claves
claves = baseDatosRedis.keys()
print(claves)
# Mostramos la clave y su valor
for clave in claves:
  print(clave)
  tipo = baseDatosRedis.type(clave)
  print(tipo)
  if tipo == "hash":
    valor = baseDatosRedis.hgetall(clave)
  elif tipo == "ReJSON-RL" or ":" in clave:
    valor = baseDatosRedis.json().get(clave)
  else:
    valor = baseDatosRedis.get(clave)
  print('Clave:', clave , ' y Valor: ', valor)
  
baseDatosRedis.close()