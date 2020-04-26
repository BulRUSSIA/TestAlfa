# TODO 1)на вход подается формат вывода(консоль,файл) и любая дата(период расчета бонусов)
# TODO 2)все бонусы суммируются между собой
# TODO 3)алгоритм расчета бонусов для сотрудника
from Models.LocalData import LocalData
import datetime

in_date = datetime.date(2015, 2, 1)  # период расчета бонусов
out_date = datetime.datetime(2016, 3, 4)  # период расчета бонусов
local = LocalData()
for employ in local.employees:  # парсим сотрудников
    print('----------------------------------------------')
    print("Фио сотрудника:", employ.employer_full_name)
    print("Бонусы сотрудника:", employ.bonus_code)
    print("Дата устройства на работу:", employ.in_work)
    print("Дата увольнения:", employ.out_work)

    """Парсим бонусы для сотрудника"""
    for bonus_id in employ.bonus_code:
        for bonus_obj in local.bonuses:
            if bonus_obj.id_ == bonus_id:
                print("Объект бонус для конкретного сотрудника:", bonus_obj)

    """Парсим контракты для сотрудника"""
    for contract in local.contracts:
        if contract.employer_code == employ.id_:
            print("Контракт сотрудника:", contract)
