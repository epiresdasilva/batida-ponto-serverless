import json
import logging
import psycopg2
import rds_config


def main(event, context):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # rds settings
    rds_host = rds_config.db_host
    name = rds_config.db_username
    password = rds_config.db_password
    db_name = rds_config.db_name

    connection = psycopg2.connect(
        database=db_name,
        user=name,
        password=password,
        host=rds_host,
        port='5432'
    )
    cursor = connection.cursor()

    try:
        for record in event["Records"]:
            body = record["body"]
            body = json.loads(body)
            cursor.execute(f"""
                            insert into batida(usuario_id, ponto) 
                            values ({body["usuarioId"]}, '{body["ponto"]}')
                            """)

        connection.commit()
    except psycopg2.Error as e:
        connection.rollback()
        logger.error("Error while inserting", e)

    body = {
        "quantidadePontos": len(event["Records"]),
        "payload": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
