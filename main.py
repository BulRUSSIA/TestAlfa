# TODO 1)на вход подается формат вывода(консоль,файл) и любая дата(период расчета бонусов)
# TODO 2)все бонусы суммируются между собой
# TODO 3)алгоритм расчета бонусов для сотрудника
from DataStructures.DataCalculationBonus import Bonuses
from DataStructures.DataContracts import Contracts
from DataStructures.DataEmployees import Employees
from Models.Employee import Employee
from Models.Bonus import Bonus
from Models.Contract import Contract

# em = list(map(lambda data_field: Employee(data_field['id'], data_field['employer_full_name'], data_field['in_work'],
#                                           data_field['out_work'],
#                                           data_field['bonus_code'], data_field['base_salary']), Employees))
data_field = Employees[0]
"""Сотрудник под номером 1"""
employee_one = Employee(data_field['id'], data_field['employer_full_name'], data_field['in_work'],
                        data_field['out_work'],
                        data_field['bonus_code'], data_field['base_salary'])
print(employee_one.employer_full_name)
"""Бонусы сотрудника 1"""
print('Бонусы сотрудника', employee_one.bonus_code)
print('устроился на работу', employee_one.in_work)
print('уволился', employee_one.out_work)

EMP_BONUS_ID = employee_one.bonus_code  # Список бонусов сотрудника
EMP_ID = employee_one.id_  # Ищем в контракте id пользователя

for contract in Contracts:  # Достаем из контрактов ,контракты сотрудника
    if contract['employer_code'] == EMP_ID:  # Если в контракте указан id нашего сотрудника
        contract_instance = Contract(contract['id'], contract['employer_code'], contract['data_contract'],
                                     contract['sum_contract'])  # Мапим данные в модель

if len(EMP_BONUS_ID) > 0:  # Если бонусы существуют
    for bonus in Bonuses:  # Идем по списку всех  бонусов
        for code in EMP_BONUS_ID:  # Идем по списку бонусов сотрудника
            if bonus['id'] == code:  # Если есть совпдаения с бонусом сотрудника вывести весь объект бонуса
                bonus_instance = Bonus(bonus['id'], bonus['bonus_percent'])  # создаем экземпляр класса Bonus
