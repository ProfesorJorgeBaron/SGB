import redis

conexionRedis = redis.ConnectionPool(host='localhost', port=6370, db=0,,decode_responses=True)
baseDatosRedis = redis.Redis(connection_pool=conexionRedis)

baseDatosRedis.set('libro_1', 'Quijote')
baseDatosRedis.set('libro_2', 'Hamlet', ex=10)