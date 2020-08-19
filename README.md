# Customer-Account-Transactions

Customer-Account-Transactions is a Python project for processing and analyzing customer's transactions records and generate meaning ful insights.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements using below command.

```bash
pip install -r requirements.txt
```

## Usage

```python
python src/main.py
```
**Note**: The code requires environment variables to be available at run time which are passed via Cloud Build Trigger -> Kubernetes Manifest File -> Python main.py. Pls run unit test cases on local system or patch the environment variables in main.py and utils.py to run locally.

## Project Structure

```
.
|-- Dockerfile
|-- README.md
|-- k8s
|   `-- kubepod.yaml
|-- requirements.txt
`-- src
    |-- __main__.py
    |-- __pycache__
    |   |-- constants.cpython-37.pyc
    |   |-- exceptions.cpython-37.pyc
    |   |-- main.cpython-37.pyc
    |   `-- utils.cpython-37.pyc
    |-- bq.sql
    |-- constants.py
    |-- exceptions.py
    |-- main.py
    |-- payload.json
    |-- tests
    |   |-- __init__.py
    |   |-- __pycache__
    |   |   `-- __init__.cpython-37.pyc
    |   |-- sit
    |   |   `-- __init__.py
    |   `-- unit
    |       |-- __init__.py
    |       |-- __pycache__
    |       |   |-- __init__.cpython-37.pyc
    |       |   |-- test_data.cpython-37-pytest-5.3.5.pyc
    |       |   `-- test_main.cpython-37-pytest-5.3.5.pyc
    |       |-- test_data.py
    |       `-- test_main.py
    `-- utils.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.