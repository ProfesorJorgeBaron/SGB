import redis
from redis.commands.json.path import Path
from redis.commands.search.field import TextField, NumericField, TagField
from redis.commands.search.index_definition import IndexDefinition, IndexType

#creamos las conexiones
conexionRedis = redis.ConnectionPool(host='localhost', 
                                     port=6379, 
                                     db=0,
                                     decode_responses=True)
baseDatosRedis = redis.Redis(connection_pool=conexionRedis)

esquema = (
    TextField("$.nombre", as_name="nombre"),
    TagField("$.ciudad", as_name="ciudad"),
    NumericField("$.edad", as_name="edad")
)

indexCreated = baseDatosRedis.ft("indice:usuarios").create_index(
    esquema,
    definition=IndexDefinition(
        prefix=["usuarios:"], index_type=IndexType.JSON
    )
)

usuario1 = {
    "nombre": "Jorge Baron",
    "email": "jorge.baron@example.com",
    "edad": 38,
    "ciudad": "Spain"
}

usuario2 = {
    "nombre": "Elena Gómez",
    "email": "elena.gomez@example.com",
    "edad": 29,
    "ciudad": "Mexico"
}

usuario3 = {
    "nombre":"Pepe garcia",
    "email": "pepe.garcia@example.com",
    "ciudad": 33,
    "edad": "Spain"
}

user1Set = baseDatosRedis.json().set("usuarios:1", Path.root_path(), usuario1)
user2Set = baseDatosRedis.json().set("usuarios:2", Path.root_path(), usuario2)
user3Set = baseDatosRedis.json().set("usuarios:3", Path.root_path(), usuario3)

baseDatosRedis.close()
