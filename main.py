import datetime
import csv
from Models.LocalData import LocalData
from Logic.CalculateBonuses import Bonus_1, Bonus_2, Bonus_3, Bonus_4
from tabulate import tabulate
EMPLOYEES_LIST = []


class EmployeesPr:
    contract = None
    max_bonus_two = 100000  # максимальный бонус по 2 коду бонуса
    """сумма по 1,2,3,4"""
    total_bonus_1 = 0
    total_bonus_2 = 0
    total_bonus_3 = 0
    total_bonus_4 = 0
    total_bonus_sum = 0
    csv_write = False

    """Переводим в формат datetime"""
    def date_in(self, date):
        try:
            year, month, day = map(int, date.split('-'))
            full_date = datetime.date(year, month, day)
            return full_date
        except ValueError:
            print('Не верный формат даты,введите заново!')
            self.main()

    """Работал ли сотрудник в указанный период"""
    @staticmethod
    def date_intersection(t1, t2):
        t1start, t1end = t1[0], t1[1]
        t2start, t2end = t2[0], t2[1]
        if t1end < t2start:return False
        if t1end == t2start:return True
        if t1start == t2start:return True
        if t1start < t2start < t1end:return True
        if t1start > t2start and t1end < t2end:return True
        if t1start < t2start and t1end > t2end:return True
        if t1start < t2end < t1end: return True
        if t2start < t1start < t2end: return True
        if t1start == t2end:return True
        if t1end == t2end:return True
        if t1start > t2end:return False

    def main(self):
        local = LocalData()  # получаем списки сущностей при обращении к полям класса
        method_read = int(input('Выберите способ для вывода отчета (1)-консоль, (2)-csv файл,в ответ укажите число:'))
        if method_read == 2:
            self.csv_write = True
        date_entry = input('Введите начало периода в формате YYYY-MM-DD:')
        date_end = input('Введите конец периода в формате YYYY-MM-DD:')
        in_date = self.date_in(date_entry)  # период расчета бонусов
        out_date = self.date_in(date_end)  # период расчета бонусов
        for employee in local.employees:  # парсим сотрудников
            if employee.out_work is None:
                employee.out_work = out_date + datetime.timedelta(
                    days=1)  # Если сотрудник не был уволен (дата конца периода + 1)
            if self.date_intersection((in_date, out_date),
                                      (employee.in_work, employee.out_work)):  # принимает кортеж с 2 периодами
                """Если сотрудники работали в заданный интервал"""
                for contract in local.contracts:  # Идем по контрактам
                    if contract.employee_code == employee.id_:  # Если в контрактах находим текущий ид сотрудника
                        self.contract = contract  # записываем контракт

                        """Парсим бонусы для сотрудника"""
                        for bonus_id in employee.bonus_code:  # идем по бонусам сотрудника

                            """Ищем подходящий код бонуса"""
                            if bonus_id == 1:
                                self.total_bonus_1 = self.total_bonus_1 + Bonus_1(self.contract.sum_contract).bonus_sum

                            if bonus_id == 2:
                                """Начисления не > 100 000 ( по усл.) """
                                if self.total_bonus_2 > self.max_bonus_two:
                                    self.total_bonus_2 = self.max_bonus_two
                                self.total_bonus_2 = self.total_bonus_2 + Bonus_2(self.contract.sum_contract).bonus_sum

                            if bonus_id == 3:
                                self.total_bonus_3 = self.total_bonus_3 + Bonus_3(self.contract.sum_contract,
                                                                                  self.contract.data_contract,
                                                                                  in_date).bonus_sum
                            if bonus_id == 4:
                                if employee.out_work is not None:
                                    self.total_bonus_4 = self.total_bonus_4 + Bonus_4(employee.base_salary, in_date,
                                                                                      out_date,
                                                                                      employee.in_work,
                                                                                      employee.out_work).bonus_sum
                                else:
                                    self.total_bonus_4 = self.total_bonus_4 + Bonus_4(employee.base_salary, in_date,
                                                                                      out_date,
                                                                                      employee.in_work,
                                                                                      out_date).bonus_sum

                            self.total_bonus_sum = self.total_bonus_1 + self.total_bonus_2 + self.total_bonus_3 \
                                                   + self.total_bonus_4
                self.write_employees_bonuses(employee.id_, employee.employee_full_name)

    """Записываем в csv файл или выводим в консоль"""
    def write_employees_bonuses(self, employee_id, full_name):
        data_view = {"код": employee_id, "ФИО": full_name, "сумма бонусов": self.total_bonus_sum}
        EMPLOYEES_LIST.append(data_view)
        if not self.csv_write:
            print(tabulate(data_view.items(),  tablefmt="grid"))
        else:
            EMPLOYEES_LIST.append(data_view)
            with open('Отчет.csv', 'w', encoding='utf-8') as f:
                writer = csv.DictWriter(
                    f, fieldnames=list(EMPLOYEES_LIST[0].keys()), quoting=csv.QUOTE_NONNUMERIC)
                writer.writeheader()
                for employer in EMPLOYEES_LIST:
                    writer.writerow(employer)


if __name__ == '__main__':
    emp = EmployeesPr()
    emp.main()
