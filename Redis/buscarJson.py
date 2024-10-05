import redis

#creamos las conexiones
conexionRedis = redis.ConnectionPool(host='localhost', port=6370, db=0,decode_responses=True)
baseDatosRedis = redis.Redis(connection_pool=conexionRedis)

res1 = baseDatosRedis.json().get("usuarios_array", '$[?(@.edad > 50)]')
print(res1)


res2 = baseDatosRedis.json().get("usuarios_array", '$[?(@.nombre == "Pepe")]')
print(res2)