import redis

#creamos las conexiones
conexionRedis = redis.ConnectionPool(host='localhost', port=6379, db=0,decode_responses=True)
baseDatosRedis = redis.Redis(connection_pool=conexionRedis)

baseDatosRedis.hset('usuario:5', mapping={"nombre": "Ana", "edad": 60})
baseDatosRedis.hset('usuario:6', mapping={"nombre": "Luis", "edad": 45})


resultado = baseDatosRedis.hgetall('usuario:5')
print(resultado)


resultado = baseDatosRedis.hgetall('usuario:6')
print(resultado)

baseDatosRedis.close()