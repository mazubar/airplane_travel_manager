from behave import *

@given('Пользователь заполняет не все обязательные поля при внесении информации о рейсе')
def step_impl(context):
    for row in context.table:
        model.add_user(flight=row['flight'], departure=row['departure'])

@when('Пользователь нажимает кнопку "сохранить"')
def step_impl(context):
    pass

@then('Система выдает предупреждение о том, что не все обязательные поля заполнены')
def step_impl(context):
    if flight == NULL or departure == NULL:
        print("Не все необходимые поля заполнены!")

@and ('Незаполненные обязательные поля выделяются красным цветом')
def step_impl(context):
    pass
