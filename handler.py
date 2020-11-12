import json
import logging
import psycopg2


def main(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.info("teste do evandro: " + event["Records"][0]["body"])

    # rds settings
    # rds_host = "rds-instance-endpoint"
    # name = rds_config.db_username
    # password = rds_config.db_password
    # db_name = rds_config.db_name

    connection = psycopg2.connect(
        database="pontodb",
        user="ponto",
        password="p0nt0#2020",
        host="ponto-cluster.cluster-cgawhvnggplu.us-east-1.rds.amazonaws.com",
        port='5432'
    )
    cursor = connection.cursor()

    for record in event["Records"]:
        try:
            cursor.execute("insert into batida(usuario_id, ponto) values (123, '2020-11-11 16:00')")
            connection.commit()
        except psycopg2.Error as e:
            connection.rollback()
            logger.error("Error while inserting", e)

    logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")

    return response
