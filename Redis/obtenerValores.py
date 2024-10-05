import redis

#creamos las conexiones
conexionRedis = redis.ConnectionPool(host='localhost', port=6370, db=0)
baseDatosRedis = redis.Redis(connection_pool=conexionRedis)

#Obtener el valor de la clave "libro_1" pero en binario
print(baseDatosRedis.get("libro_1"))

#Obtener el valor de la clave "libro_1" pero en String
print(baseDatosRedis.get("libro_1").decode("utf-8"))

#Obtener el valor de la clave "libro_2" que al tener tiempo de vida estará ya vacía
print(baseDatosRedis.get("libro_2"))