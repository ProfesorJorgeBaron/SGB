import redis

#creamos las conexiones
conexionRedis = redis.ConnectionPool(host='localhost', 
                                     port=6379, db=0,
                                     decode_responses=True)

baseDatosRedis = redis.Redis(connection_pool=conexionRedis)

pipe = baseDatosRedis.pipeline()
pipe.set('libro_3', "Los pilares de la tierra")
pipe.set('libro_4', "La larga marcha")
pipe.set('libro_5', "El señor de los anillos")
pipe.execute()