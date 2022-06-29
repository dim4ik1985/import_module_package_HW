from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import date

if __name__ == '__main__':
    employess1 = get_employees('Петя', 'Продажи')
    employess2 = get_employees('Маша', 'Оператор')

    salary1 = calculate_salary(1.2, 50)
    salary2 = calculate_salary(2, 32)
    data = date.today()
    print(f'{data}: {employess1} получил {salary2} $')
