import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv
import os

load_dotenv()

# -------------------------------
# PARAMETROS DE CONFIGURACION
# -------------------------------
DB_INSTANCE_ID = os.getenv("DB_INSTANCE_ID")
DB_INSTANCE_CLASS = "db.t4g.micro"
DB_ENGINE = "mariadb"
DB_ALLOCATED_STORAGE = 20

# -------------------------------
# CREAR RDS (MariaDB)
# -------------------------------

session = boto3.session.Session( 
    aws_access_key_id=os.getenv("ACCESS_KEY"),
    aws_secret_access_key=os.getenv("SECRET_KEY"),
    aws_session_token=os.getenv("SESSION_TOKEN"),
    region_name=os.getenv("REGION"))

rds = session.client('rds')

def create_rds_instance():
    
    try:
        print("Comprobando si la instancia RDS ya existe...")
        info = rds.describe_db_instances(DBInstanceIdentifier=DB_INSTANCE_ID)
        print(f"La instancia '{DB_INSTANCE_ID}' ya existe.")
    except ClientError as e:
        print("Creando instancia RDS...")

        rds.create_db_instance(
            DBInstanceIdentifier=DB_INSTANCE_ID,
            AllocatedStorage=DB_ALLOCATED_STORAGE,
            DBInstanceClass=DB_INSTANCE_CLASS,
            Engine=DB_ENGINE,
            MasterUsername=os.getenv("DB_USER"),
            MasterUserPassword=os.getenv("DB_PASSWORD"),
            PubliclyAccessible=True
        )


    print("Usamos los waiters para esperar a que la instancia esté disponible")
    waiter = rds.get_waiter('db_instance_available')
    waiter.wait(DBInstanceIdentifier=DB_INSTANCE_ID)
    print("La instancia RDS está disponible")

    info = rds.describe_db_instances(DBInstanceIdentifier=DB_INSTANCE_ID)
    endpoint = info['DBInstances'][0]['Endpoint']['Address']
    return endpoint