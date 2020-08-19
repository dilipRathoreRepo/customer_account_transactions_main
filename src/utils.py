import json
import os
import time
import logging
from decimal import Decimal
from datetime import date
from datetime import datetime
from google.cloud import bigquery
from exceptions import InvalidEnvironmentVariable
from constants import valid_env, SQL_FILE, BQ_LOCATION


def validate_env_var():
    """
    Validates environemnt variables e.g. Project environments i.e. DEV, TEST, PROD etc. Valid values are passed via
    constants.py file's variable "valid_env". Also, validates that BigQuery project ID is passed or not.
    :return:
    """
    if os.environ["ENV"].upper() not in valid_env:
        raise InvalidEnvironmentVariable("Incorrect environment variable {}".format(os.environ["ENV"]))

    if not os.environ["BQ_PROJECT_ID"]:
        raise InvalidEnvironmentVariable("Environment variable not set for BQ_PROJECT_ID")


def get_bq_data():
    """
    Returns the data from BigQuery table.
    :return: BigQuery Row Iterator Object
    """
    sql_file_abs_path = get_abs_path(SQL_FILE)
    query_string = get_bq_sql(sql_file_abs_path).format(PROJECT_ID=os.environ["BQ_PROJECT_ID"])
    return query_tables(query_string)


def get_abs_path(p):
    """
    Standard method used to get the absolute path of any file.
    :param p: File Name
    :return: Absolute path of the passed file name
    """
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), p)


def get_bq_sql(sql_file):
    """
    Returns File object for the SQL fle
    :param sql_file:
    :return: File Object
    """
    try:
        return open(sql_file, "r").read()
    except FileNotFoundError as e:
        logging.exception("BQ SQL file not found {}".format(str(e)))
        raise
    except Exception as e:
        logging.exception("Exception occurred {}".format(str(e)))


def query_tables(query_string):
    """
    Reads customer and account data from BigQuery and returns result
    :param query_string: str
    :return: BigQuery Row Iterator Object
    """
    try:
        client = bigquery.Client(project=os.environ["BQ_PROJECT_ID"], location=BQ_LOCATION)
        query_job = client.query(query_string)
        return query_job.result()
    except Exception as e:
        logging.exception("Failed to read records from bq: {}".format(str(e)))
        raise


def decimal_default(obj):
    """
    JSON encoder class for datetime.date and Decimal data type
    :param obj: Decimal or datetime.date object
    :return: str
    """
    if isinstance(obj, datetime):
        return obj.isoformat()
    elif isinstance(obj, date):
        return obj.isoformat()
    elif isinstance(obj, Decimal):
        return str(obj)
    raise TypeError


def json_dump(data):
    """
    Outputs data in a local file
    :param data: Dictionary
    :return: None
    """
    with open("payload.json", "a") as file:
        json.dump(data, file, default=decimal_default, indent=4)


def wait():
    """
    Waits for the POD to be delted on successful completion
    :return: None
    """
    while True:
        time.sleep(30)
