from decimal import Decimal

test_cases_data = {
    "test_single_record": {
        "record": [
            {
                "customer_id": 101,
                "first_name": "Stevie",
                "last_name": "Dailly",
                "email": "sdailly0@1688.com",
                "gender": "Male",
                "street_address": "10 Hanson Pass",
                "city": "Shaoguan",
                "postal_code": 303169,
                "country_name": "China",
                "account_no": 3567970665369130,
                "currency": "CNY",
                "amount": 135.5,
                "transaction_time": "11/05/19"
            }
        ],
        "expected_result": [
            {
                "customer": {
                    "customer_id": 101,
                    "first_name": "Stevie",
                    "last_name": "Dailly",
                    "email": "sdailly0@1688.com",
                    "gender": "Male",
                    "street_address": "10 Hanson Pass",
                    "city": "Shaoguan",
                    "postal_code": 303169,
                    "country_name": "China"
                },
                "account": {
                    "account_no": 3567970665369130
                },
                "transactions": [
                    {
                        "currency": "CNY",
                        "amount": 135.5,
                        "transaction_time": "11/05/19"
                    }
                ]
            }
        ]
    },
    "test_two_records": {
        "record": [
            {
                "customer_id": 101,
                "first_name": "Stevie",
                "last_name": "Dailly",
                "email": "sdailly0@1688.com",
                "gender": "Male",
                "street_address": "10 Hanson Pass",
                "city": "Shaoguan",
                "postal_code": 303169,
                "country_name": "China",
                "account_no": 3567970665369130,
                "currency": "CNY",
                "amount": 135.5,
                "transaction_time": "11/05/19"
            },
            {
                "customer_id": 201,
                "first_name": "Stevie2",
                "last_name": "Dailly2",
                "email": "sdailly0@1688.com2",
                "gender": "Male2",
                "street_address": "10 Hanson Pass2",
                "city": "Shaoguan2",
                "postal_code": 3031692,
                "country_name": "China2",
                "account_no": 35679706653691302,
                "currency": "CNY2",
                "amount": 135.52,
                "transaction_time": "11/05/19"
            }
        ],
        "expected_result": [
            {
                "customer": {
                    "customer_id": 101,
                    "first_name": "Stevie",
                    "last_name": "Dailly",
                    "email": "sdailly0@1688.com",
                    "gender": "Male",
                    "street_address": "10 Hanson Pass",
                    "city": "Shaoguan",
                    "postal_code": 303169,
                    "country_name": "China"
                },
                "account": {
                    "account_no": 3567970665369130
                },
                "transactions": [
                    {
                        "currency": "CNY",
                        "amount": 135.5,
                        "transaction_time": "11/05/19"
                    }
                ]
            },
            {
                "customer": {
                    "customer_id": 201,
                    "first_name": "Stevie2",
                    "last_name": "Dailly2",
                    "email": "sdailly0@1688.com2",
                    "gender": "Male2",
                    "street_address": "10 Hanson Pass2",
                    "city": "Shaoguan2",
                    "postal_code": 3031692,
                    "country_name": "China2"
                },
                "account": {
                    "account_no": 35679706653691302
                },
                "transactions": [
                    {
                        "currency": "CNY2",
                        "amount": 135.52,
                        "transaction_time": "11/05/19"
                    }
                ]
            }
        ]
    },
    "test_two_records_same_customer_diff_txn": {
        "record": [
            {
                "customer_id": 101,
                "first_name": "Stevie",
                "last_name": "Dailly",
                "email": "sdailly0@1688.com",
                "gender": "Male",
                "street_address": "10 Hanson Pass",
                "city": "Shaoguan",
                "postal_code": 303169,
                "country_name": "China",
                "account_no": 3567970665369130,
                "currency": "CNY",
                "amount": 135.5,
                "transaction_time": "11/05/19"
            },
            {
                "customer_id": 101,
                "first_name": "Stevie",
                "last_name": "Dailly",
                "email": "sdailly0@1688.com",
                "gender": "Male",
                "street_address": "10 Hanson Pass",
                "city": "Shaoguan",
                "postal_code": 303169,
                "country_name": "China",
                "account_no": 3567970665369130,
                "currency": "CNY",
                "amount": 10.41,
                "transaction_time": "12/05/19"
            }
        ],
        "expected_result": [
            {
                "customer": {
                    "customer_id": 101,
                    "first_name": "Stevie",
                    "last_name": "Dailly",
                    "email": "sdailly0@1688.com",
                    "gender": "Male",
                    "street_address": "10 Hanson Pass",
                    "city": "Shaoguan",
                    "postal_code": 303169,
                    "country_name": "China"
                },
                "account": {
                    "account_no": 3567970665369130
                },
                "transactions": [
                    {
                        "currency": "CNY",
                        "amount": 135.5,
                        "transaction_time": "11/05/19"
                    },
                    {
                        "currency": "CNY",
                        "amount": 10.41,
                        "transaction_time": "12/05/19"
                    }
                ]
            }
        ]
    },
    "test_decimal_encoding_with_decimals": {
        "customer_id": 101,
        "first_name": "Stevie",
        "last_name": "Dailly",
        "email": "sdailly0@1688.com",
        "gender": "Male",
        "street_address": "10 Hanson Pass",
        "city": "Shaoguan",
        "postal_code": 303169,
        "country_name": "China",
        "account_no": 3567970665369130,
        "currency": "CNY",
        "amount": Decimal(10.41),
        "transaction_time": "12/05/19"
    }
}