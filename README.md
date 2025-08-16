**Instructions to execute automation tests:**


 - Clone the repository
 
 - create virtual env:
https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/


 - install dependencies: `pip install -r requirements.txt`


 - Install drivers for browsers: `playwright install`


 - Run the tests using command: `pytest -v -m login_form --hmtl=/report/report.html --capture=tree-sys`