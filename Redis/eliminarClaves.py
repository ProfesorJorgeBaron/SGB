import redis

#creamos las conexiones
conexionRedis = redis.ConnectionPool(host='localhost', port=6370, db=0)
baseDatosRedis = redis.Redis(connection_pool=conexionRedis)

baseDatosRedis.delete("libro_1")
baseDatosRedis.delete("libro_2")