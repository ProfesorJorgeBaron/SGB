import redis

#creamos las conexiones
conexionRedis = redis.ConnectionPool(host='localhost', port=6370, db=0,decode_responses=True)
baseDatosRedis = redis.Redis(connection_pool=conexionRedis)

res1 = baseDatosRedis.json().set("usuario:1", "$", {"nombre": "Jorge", "apellido": "Baron", "edad": 37})
res2 = baseDatosRedis.json().set("usuario:2", "$", {"nombre": "Lucía", "apellido": "Benitez", "edad": 24})
res3 = baseDatosRedis.json().get("usuario:1", "$")
print(res3)
res4 = baseDatosRedis.json().get("usuario:2", "$")
print(res4)


baseDatosRedis.json().set("usuarios_array", "$", [])

res5 = baseDatosRedis.json().arrappend("usuarios_array", "$", {"nombre": "Pepe", "apellido": "Sanchez", "edad": 45})
res6 = baseDatosRedis.json().arrappend("usuarios_array", "$", {"nombre": "Calisto", "apellido": "Melibea", "edad": 67})
res7 = baseDatosRedis.json().get("usuarios_array", "$")
print(res7)
