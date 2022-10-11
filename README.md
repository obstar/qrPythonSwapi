# Overview

Test framework written in python as demo for testing RESTful API of https://swapi.dev/

# How to run tests

## pre-installed on local:

- [allure commandline](https://docs.qameta.io/allure-report/#_installing_a_commandline)
- [python 3.9 or higher](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)

### by script

Run script

```
test.sh
```

### manually:

1. Create virtual env

```
python3 -m venv env
```

2. Activate env

```
source env/bin/activate
```

3. Install required packages

```
pip install -r requirements.txt
```

4. Run pytest

```
pytest --alluredir=./reports/allure_results
```

5. Generate report

```
allure serve ./reports/allure_results
```

## Libraries used by project:

1. Python 3.9 and higher
2. pytest
3. pytest-timeout
4. requests
5. allure-pytest for reports
