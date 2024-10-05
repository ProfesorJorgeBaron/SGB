import redis

#creamos las conexiones
conexionRedis = redis.ConnectionPool(host='localhost', port=6370, db=2,decode_responses=True)
baseDatosRedis = redis.Redis(connection_pool=conexionRedis)

res1 = baseDatosRedis.lpush("usuarios:hobbies", "futbol:1")
res2 = baseDatosRedis.lpush("usuarios:hobbies", "tenis:2")
res2 = baseDatosRedis.lpush("usuarios:hobbies", "rugby:2") 

res3 = baseDatosRedis.lrange("usuarios:hobbies",0,-1)
print(res3)

res4 = baseDatosRedis.rpop("usuarios:hobbies")
print(res4) 

res5 = baseDatosRedis.rpop("usuarios:hobbies")
print(res5)

res6 = baseDatosRedis.lrange("usuarios:hobbies",0,-1)
print(res6)
