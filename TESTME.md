# Libraries used by project:

1. Python 3.9 and higher
2. Pytest
3. Requests
4. Allure Framework for reports

## How to run tests manually:

1. python3 -m venv env
2. source env/bin/activate
3. pip install -r requirements.txt
4. pytest --alluredir=./reports/allure_results

## Generating report

pre:
[allure commandline](https://docs.qameta.io/allure-report/#_installing_a_commandline) need to be installed on local

```
allure serve ./reports/allure_results
```
