Assumptions: 
    1. Top level employee will not have manager (CEO or High level). 
    2. Input file is a Json
    3. Some employees may not have managers (temporarily). atleast one employee do not have a manager (CEO or High level). 

Sample file structure: 
[
    {
        "name":"Jeff",             --> Top level employee
        "salary": 10000.00      
    },
    {
        "name":"Sam",              --> Can be employee and manager
        "salary": 6000.00,
        "manager": "Jeff"
    }
]

Running the application:
    1. Keep the Json file in input folder. Sample files are present under input folder.
    2. Update the file name in .env file
    3. run app.py
    4. Output will be displayed on console

Tests: 
    1. Tests are under test folder. Tests are written using unittest