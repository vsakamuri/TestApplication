import json
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get file name from env variables
file_name = os.getenv("FILE_NAME")

file_path = "./input/" + file_name

def read_input():
    '''
    Reads file from specified path and returns Json
    Params: None
    Returns: None
    '''
    with open(file_path) as input_file:
        try:
            data = json.load(input_file)
            if len(data) == 0:
                print("No employees in the organization")
                print("Total Salary: 0.00")
            return data
        except Exception:
            print("invalid input. Input file should contain valid Json")
            return []

def print_org_structure(employee, employees_under_managers,tab):   
    '''
    if employee is in employees_under_managers means employee has reporties
    else employee does not have any reporties and No furthur processing is required
    
    This function is recursively called until employee does not reporties
    Params: 
        employee : manager name
        employees_under_managers (Dict) - managers as key and employees under the manager as list value
        tab (int) - count of tabs
    Returns: None
    '''               
      
    if employee in employees_under_managers:
        
        employees_list = employees_under_managers.get(employee)
        employees_list.sort()
        
        tab += 1
        for name in employees_list:
            print(tab*"\t"+"|_ "+name)
            print_org_structure(name, employees_under_managers, tab)

def print_employee_info(top_level_employees, employees_under_managers, total_salary):
    '''
    if more than one top level employee found, print the employee org structure one ofter other
    assumption is that some employees may not have manager, if manager left the company. 
    if that is not true then we can modify the code to have only one top level employee (CEO/Higher)
    Params: 
        top_level_employees (list) - employees who do not have managers
        employees_under_managers (Dict) - managers as key and employees under the manager as list value
        total_salary - salary of entire organization.
    Return: None
    '''
    if len(top_level_employees) == 0: 
        print ("atleast one employee should not have manager")
    else:
        top_level_employees.sort()
        for top_level_employee in top_level_employees:
            print(top_level_employee)
            tab = 0
            print_org_structure(top_level_employee, employees_under_managers, tab)  
            print("")
    
        print("Total Salary: ${:0,}".format(total_salary))

def main():
    '''
    1. Reads the employee file
    2. If not empty employee json list
        a. calculate total salary
        b. identify top level employee
        c. creates manager to employee dictonary
        d. call print employee org structure & salary function
    
    Params: None
    Return: None
    '''
    employee_list = read_input()

    if len(employee_list) > 0: 
        employees_under_managers = {}
        top_level_employees = []
        total_salary = 0.00
    
        for employee in employee_list:
            total_salary +=  employee.get('salary',0.00)

            if employee.get('manager'):
                # if manager is already present then append employee to the list
                if employee.get('manager') in employees_under_managers:
                    employees_under_managers[employee.get('manager')].append(employee.get('name'))
                else:
                    employees_under_managers[employee.get('manager')] = [employee.get('name')]
            else: 
                # no manager means then employee is top level employee
                top_level_employees.append(employee.get('name'))

        print_employee_info(top_level_employees, employees_under_managers, total_salary)
                
if __name__ == '__main__':
    main()