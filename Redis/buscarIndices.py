import redis
from redis.commands.search.query import Query
import redis.commands.search.aggregation as aggregations
import redis.commands.search.reducers as reducers

conexionRedis = redis.ConnectionPool(host='localhost', 
                                     port=6379, 
                                     db=1,
                                     decode_responses=True)
baseDatosRedis = redis.Redis(connection_pool=conexionRedis)

resultados = baseDatosRedis.ft("indice:usuarios").search(
    Query("Jorge @edad:[30 40]")
)

print(resultados)

groupby = aggregations.AggregateRequest("*").group_by(
    '@ciudad', reducers.count().alias('count')
)

resultado = baseDatosRedis.ft("indice:usuarios").aggregate(groupby).rows
print(resultado)

indices = baseDatosRedis.execute_command('FT._LIST')
print("Índices creados:", indices)

baseDatosRedis.close()