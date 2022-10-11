python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
pytest --alluredir=./reports/allure_results
allure serve ./reports/allure_results