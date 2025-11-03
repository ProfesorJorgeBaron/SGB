import redis

#creamos las conexiones
conexionRedis = redis.ConnectionPool(host='localhost', port=6379, db=0,decode_responses=True)
baseDatosRedis = redis.Redis(connection_pool=conexionRedis)

baseDatosRedis.set("libro_1","Quijote")
baseDatosRedis.set("libro_2","Hamlet")
baseDatosRedis.set("libro_3","Otelo")
baseDatosRedis.set("comic_1","Mortadelo y Filemón")
baseDatosRedis.set("comic_2","Superman")

print("Los primeros:")
for clave in baseDatosRedis.scan_iter('*[_1]'):
    print(clave)
    
print("Los Comics:")    
for clave in baseDatosRedis.scan_iter('comic*'):
    print(clave)
    
baseDatosRedis.close()