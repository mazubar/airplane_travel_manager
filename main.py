from database.model import *
from flight_manager_mock import FlightManagerMock

db_travel.connect()

db_travel.create_tables([
    Account, Flight, Playlist, Audio, ChatBot, Notification, Card
])
flight_manager = FlightManagerMock()

# Пользователь неправильно вносит информацию о рейсе
first_flight = flight_manager.create_flight(number=1021)
# Пользователь нажимает на кнопку сохранить
flight_manager.press_save_button(first_flight)
# Выводим какие поля не были заполнены (вывод в консоль)
# -> Проущено поле departure

# Если все поля зполнены, то сохраняем рейс и предлагаем настроить уведосления о рейсе
second_flight = flight_manager.create_flight(number=1021, departure='202002172350', state='SP')
flight_manager.press_save_button(second_flight)
# -> Ваш полет сохранен
# -> Хотите настроить уведомления? [y/n]
# Если пользователь соглашется настроить уведомления, то выводим информацию о статусе рейса
# -> Время бежать на регистрацию
# -> Время идти на посадку
# -> Вы прилетели
