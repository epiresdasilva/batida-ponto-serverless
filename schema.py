import json
import logging
import psycopg2


def main(event, context):
    # rds settings
    # rds_host = "rds-instance-endpoint"
    # name = rds_config.db_username
    # password = rds_config.db_password
    # db_name = rds_config.db_name

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    connection = psycopg2.connect(
        database="pontodb",
        user="ponto",
        password="p0nt0#2020",
        host="ponto-cluster.cluster-cgawhvnggplu.us-east-1.rds.amazonaws.com",
        port='5432'
    )
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE batida(
    id SERIAL PRIMARY KEY,
    usuario_id integer,
    ponto timestamp)""")

    connection.commit()

    logger.info("SUCCESS: tabela criada")

    body = {
        "message": "Tabela criada"
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response

