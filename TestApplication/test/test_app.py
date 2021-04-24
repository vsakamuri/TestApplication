import unittest
from src import app
from unittest.mock import Mock, patch, mock_open
import json

class TestApp(unittest.TestCase):

    def test_read_input(self):
        #valid json input
        test_data = json.dumps([{
                "name":"Jeff",
                "salary": 10000.00}])
        with patch("builtins.open", mock_open(read_data=test_data)):
            data = app.read_input()
        
        self.assertEqual(data,json.loads(test_data))
        
        # empty input
        test_data = ""
        with patch("builtins.open", mock_open(read_data=test_data)):
            data = app.read_input()
        
        self.assertEqual(data,[])
     
    @patch('src.app.print_org_structure')    
    def test_print_employee_info_with_empty_employee(self, mock_print):
        top_level_employees = []
        employees_under_managers = [{"Jeff": ["Dave"]}] 
        total_salary = 2000.00
        app.print_employee_info(top_level_employees, employees_under_managers, total_salary)
        mock_print.assert_not_called()
        
    @patch('src.app.print_org_structure')    
    def test_print_employee_info_with_employee(self, mock_print):
        top_level_employees = ["Jeff"]
        employees_under_managers = [{"Jeff": ["Dave"]}] 
        total_salary = 2000.00
        app.print_employee_info(top_level_employees, employees_under_managers, total_salary)
        mock_print.assert_called_with("Jeff", employees_under_managers)
                
    #def test_main(self):   

if __name__ == '__main__':
    unittest.main()