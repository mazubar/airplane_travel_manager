""" 
Feature: Уведомление об изменении состояния рейса

Scenario: Уведомление о начале регистрации
  Given: В систему занесена информация о рейсе и пользователь включил дефолтные уведомления
  When: Начинается регистрация на рейс
  Then: Приходит уведомление о начале регистрации и нужных стойках регистрации
"""

from model import Account, Flight
from datetime import datetime, timedelta

@given('В систему занесена информация о рейсе и пользователь включил дефолтные уведомления')
def step_impl(context):
    assert Account.notifications = True

@when('Начинается регистрация на рейс')
def step_impl(context):
    assert datetime.strptime(Flight.departure, '%Y%m%d%H%M') > (date - timedelta(seconds=5))

@then('Приходит уведомление о начале регистрации и нужных стойках регистрации')
def step_impl(context, reg_desk):
        print("Регистрация началась! Стойки регистрации:" + reg_desk)
