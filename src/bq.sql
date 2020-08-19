SELECT
  customer_id,
  first_name,
  last_name,
  email,
  gender,
  account_no,
  currency,
  amount,
  transaction_time,
  street_address,
  city,
  postal_code,
  country_name
FROM `{PROJECT_ID}.customer_account_transactions_ds.cust_acct_txn_table_new`
