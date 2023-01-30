from applicaton.db.people import get_employees as employees
from applicaton.salaty import calculate_salary as salary
from datetime import date
from emoji import emojize

def hello():
    print(f'Сегодня: {date.today()}')
    print(emojize('Python это :thumbs_up:'))

if __name__ == '__main__':
    employees()
    salary()
    hello()

