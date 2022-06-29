from main import *

if __name__ == '__main__':
    employess1 = get_employees('Костя', 'Сисадмин')
    salary1 = calculate_salary(3.2, 18)
    print(f'{date.today()}: {employess1} ----> {salary1} EURO')


