import json
import os
import logging
from decimal import Decimal
from datetime import date
from datetime import datetime
from unittest.mock import patch
from google.cloud import bigquery
from exceptions import InvalidEnvironmentVariable
from constants import valid_env, SQL_FILE, BQ_LOCATION


# @patch.dict('os.environ', {'ENV': 'DEV'})
# @patch.dict('os.environ', {'BQ_PROJECT_ID': 'rising-minutia-254502'})
def validate_env_var():
    if os.environ["ENV"].upper() not in valid_env:
        raise InvalidEnvironmentVariable("Incorrect environment variable {}".format(os.environ["ENV"]))

    if not os.environ["BQ_PROJECT_ID"]:
        raise InvalidEnvironmentVariable("Environment variable not set for BQ_PROJECT_ID")


# @patch.dict('os.environ', {'BQ_PROJECT_ID': 'rising-minutia-254502'})
def get_bq_data():
    sql_file_abs_path = get_abs_path(SQL_FILE)
    query_string = get_bq_sql(sql_file_abs_path).format(PROJECT_ID=os.environ["BQ_PROJECT_ID"])
    return query_tables(query_string)


def get_abs_path(p):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), p)


def get_bq_sql(sql_file):
    try:
        return open(sql_file, "r").read()
    except FileNotFoundError as e:
        logging.exception("BQ SQL file not found {}".format(str(e)))
        raise
    except Exception as e:
        logging.exception("Exception occurred {}".format(str(e)))


# @patch.dict('os.environ', {'BQ_PROJECT_ID': 'rising-minutia-254502'})
def query_tables(query_string):
    """
    Reads customer and account data from BigQuery and returns result
    :param query_string:
    :return:
    """
    try:
        client = bigquery.Client(project=os.environ["BQ_PROJECT_ID"], location=BQ_LOCATION)
        query_job = client.query(query_string)
        return query_job.result()
    except Exception as e:
        logging.exception("Failed to read records from bq: {}".format(str(e)))
        raise


def decimal_default(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    elif isinstance(obj, date):
        return obj.isoformat()
    elif isinstance(obj, Decimal):
        return str(obj)
    raise TypeError


def json_dump(data):
    with open("payload.json", "a") as file:
        json.dump(data, file, default=decimal_default, indent=4)
