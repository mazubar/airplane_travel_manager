"""
Feature: Внесение информации о предстоящем рейсе

Scenario: Незаполненные обязательные поля
   Given: Пользователь заполняет поля
     | number    | departure        |
     | 220A      | 21/11/06 16:30   |      
     | 107B      | NULL             |
     | NULL      | 21/11/06 16:30   |
   When: Пользователь нажимает кнопку "сохранить"
   Then: Система выдает предупреждение о том, что не все обязательные поля заполнены
   And: Незаполненные обязательные поля выделяются красным цветом
"""

from behave import *
from model import Flight

@given('Пользователь заполняет {все/не все} поля при внесении информации о рейсе')
def step_impl(context):
    for row in context.table:
        model.add_user(flight=row['flight'], departure=row['departure'])

@when('Пользователь нажимает кнопку "сохранить"')
def step_impl(context):
    pass

@then('Система выдает {уведомление о сохранении/предупреждение о том, что не все обязательные поля заполнены}')
def step_impl(context):
    if flight == NULL or departure == NULL:
        print("Не все необходимые поля заполнены!")
    else:
        Flight.add_flight(flight, departure)
        print("Сохранено!")

@and ('Незаполненные обязательные поля выделяются красным цветом')
def step_impl(context):
    pass
