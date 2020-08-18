import sys
import os
import logging
from unittest.mock import patch
from src.constants import URL
from src.utils import validate_env_var, get_bq_data, json_dump
from src.exceptions import InvalidEnvironmentVariable, RestApiException


logging.basicConfig(
    stream=sys.stdout,
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


class CustomerAccountTransactions:
    @patch.dict('os.environ', {'ENV': 'DEV'})
    def __init__(self):
        self.data = []
        self.success_records = 0
        self.URL = URL.format(os.environ["ENV"])

    def add_to_data(self, res):
        """
        Adds row to self.data list with transactions for each account
        :param res: BigQuery RowIterator : Record for each customer & account along with all transactions
        :return: None
        """
        found = False
        if len(self.data) > 0:
            for element in self.data:
                if element["account"]["account_no"] == res.account_no:
                    element["transactions"].append(
                        {
                            "currency": res.currency,
                            "amount": res.amount,
                            "transaction_time": res.transaction_time
                        }
                    )
                    found = True
                    self.success_records += 1
                    break
        if not found:
            self.data.append(
                {
                    "customer": {
                        "customer_id": res.customer_id,
                        "first_name": res.first_name,
                        "last_name": res.last_name,
                        "email": res.email,
                        "gender": res.gender,
                        "street_address": res.street_address,
                        "city": res.city,
                        "postal_code": res.postal_code,
                        "country_name": res.country_name
                    },
                    "account": {
                        "account_no": res.account_no
                    },
                    "transactions": [
                        {
                            "currency": res.currency,
                            "amount": res.amount,
                            "transaction_time": res.transaction_time
                        }
                    ]
                }
            )
            self.success_records += 1

    def rest_api_call(self):
        """Calls an api /v1/updatetransactions"""
        json_dump(self.data)

    def summary(self):
        """
        Logs success and failure record counts
        :return:
        """
        logging.info("Approx Success Records are : {}".format(self.success_records))


def main():
    try:
        logging.info("Starting validate_env_var..")
        validate_env_var()

        cat = CustomerAccountTransactions()

        logging.info("Starting get_bq_data method..")
        results = get_bq_data()

        logging.info("Starting add_to_data method..")
        for result in results:
            cat.add_to_data(result)

        logging.info("Starting rest api call method..")
        cat.rest_api_call()

        logging.info("Starting summary method call..")
        cat.summary()

    except InvalidEnvironmentVariable as e:
        logging.exception("Following error occurred : {}".format(str(e)))
    except RestApiException as e:
        logging.exception("Following error occurred : {}".format(str(e)))
    except Exception as e:
        logging.exception("Following error occurred : {}".format(str(e)))
    finally:
        logging.info("Job completed..")


if __name__ == '__main__':
    main()
