This project was created in order to resolve test task which includes 3 parts:
1. develop automation tests to validate the functionality of the Gmail login form
2. develop test cases that cover various login scenarios as much as you can
3. describe an issue you were facing; How did you investigate\troubleshoot that? What were the steps you took to fix it?

Part 1:
    
    Instructions to execute automation tests:
    
    
     - clone the repository
     
     - create virtual env:
    [here are instructions how to ](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
    
    
     - install dependencies: `pip install -r requirements.txt`
    
    
     - Install drivers for browsers: `playwright install`
    
    
     - Run the tests using command: `pytest -v -m login_form -n 2 --html=report.html --capture=tee-sys` 
     
     Note: Ideally the user data in the `UserData` class shouldn't be in the Git repository. At least it should be be hidden in GithubActions, but this is
     a separated task in case if tests planning to be executed on CI
 

Part 2: Test documentation with a test cases presented on google sheets [here](https://docs.google.com/spreadsheets/d/1TLxMGXF_u3CYIETWo7lGWcCAio0AK81mu5KI-ywF73k/edit?usp=sharing)

Part 3: Describe in google docs [here](https://docs.google.com/document/d/1Sz9AKEGogqrO2aBFMcBUSJIVC6RrAHMSymgMbWyCz5s/edit?usp=sharing)






 
