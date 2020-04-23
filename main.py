from DataStructures.DataEmployees import Employees
from Models.Employee import Employee

em = list(map(lambda data_field: Employee(data_field['id'], data_field['employer_full_name'], data_field['in_work'],
                                          data_field['out_work'],
                                          data_field['bonus_code'], data_field['base_salary']), Employees))

