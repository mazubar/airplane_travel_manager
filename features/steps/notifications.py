""" 
Feature: Уведомление об изменении состояния рейса

Scenario: Уведомление о начале регистрации
  Given: В систему занесена информация о рейсе и пользователь включил дефолтные уведомления
  When: Начинается регистрация на рейс
  Then: Приходит уведомление о начале регистрации и нужных стойках регистрации
"""

