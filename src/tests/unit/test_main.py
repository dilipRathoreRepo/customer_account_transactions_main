import unittest
from unittest.mock import patch
import os
import json
from collections import namedtuple
from main import CustomerAccountTransactions
from exceptions import InvalidEnvironmentVariable, RestApiException
from .test_data import test_cases_data
from utils import validate_env_var, get_bq_data, decimal_default


class TestCustomerAccountTransactions(unittest.TestCase):
    @staticmethod
    @patch('google.cloud.bigquery.Client')
    @patch.dict('os.environ', {'ENV': 'sit'})
    @patch.dict('os.environ', {'GOOGLE_APPLICATION_CREDENTIALS': 'dummy.json'})
    @patch.dict('os.environ', {'BQ_PROJECT_ID': 'rising-minutia-254502'})
    def _set_custom_fields(test_case_name,  mock_get):
        records = test_cases_data[test_case_name]["record"]
        expected_result = test_cases_data[test_case_name]["expected_result"]

        list_bq_data = []

        for record in records:
            bq_data = namedtuple('bq_data', [
                'customer_id', 'first_name', 'last_name', 'email', 'gender', 'account_no', 'currency', 'amount',
                'transaction_time', 'street_address', 'city', 'postal_code', 'country_name'
            ])
            bq_data.customer_id = record["customer_id"]
            bq_data.first_name = record["first_name"]
            bq_data.last_name = record["last_name"]
            bq_data.email = record["email"]
            bq_data.gender = record["gender"]
            bq_data.account_no = record["account_no"]
            bq_data.currency = record["currency"]
            bq_data.amount = record["amount"]
            bq_data.transaction_time = record["transaction_time"]
            bq_data.street_address = record["street_address"]
            bq_data.city = record["city"]
            bq_data.postal_code = record["postal_code"]
            bq_data.country_name = record["country_name"]

            list_bq_data.append(bq_data)

        validate_env_var()

        mock_get.return_value.query.return_value.result.return_value = list_bq_data

        cat = CustomerAccountTransactions()
        results = get_bq_data()

        for result in results:
            cat.add_to_data(result)
        return expected_result, cat.data

    @patch.dict('os.environ', {'ENV': 'DEV9'})
    def test_validate_env_var_pass(self):
        with self.assertRaises(InvalidEnvironmentVariable):
            validate_env_var()

    def test_single_record(self):
        """
        Test Payload is generating correctly for single transaction
        :return:
        """
        exp_res, final_res = TestCustomerAccountTransactions._set_custom_fields("test_single_record")
        self.assertEqual(exp_res, final_res)

    def test_two_records(self):
        """
        Two customers with one txn each
        :return:
        """
        exp_res, final_res = TestCustomerAccountTransactions._set_custom_fields("test_two_records")
        self.assertEqual(exp_res, final_res)

    def test_two_records_same_customer_diff_txn(self):
        """
        One customer has one account. The account has two different txns
        Expected output: One payload (since one account). Txns are grouped in a list
        :return:
        """
        exp_res, final_res = TestCustomerAccountTransactions.\
            _set_custom_fields("test_two_records_same_customer_diff_txn")
        self.assertEqual(exp_res, final_res)

    def test_decimal_encoding_without_decimal_encoding(self):
        record = test_cases_data["test_decimal_encoding_with_decimals"]
        with self.assertRaises(TypeError):
            json.dumps(record)
