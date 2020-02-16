from database.model import *
from threading import Timer
from datetime import datetime, timedelta


class FlightManagerMock:

    def show_flights_list(self):
        flights = self.select_flights_list()
        for flight in flights:
            print('number: ' + flight.number, 'departure: ' + str(flight.departure), 'state: ' + flight.state)

    def select_flights_list(self):
        return Flight.select()

    def create_flight(self, number=None, departure=None, state=None):
        return Flight(number=number, departure=departure, state=state)

    def press_save_button(self, flight):
        if flight.number == None:
            print("Пропущено поле number")
            return None
        elif flight.departure == None:
            print("Пропущено поле departure")
            return None
        elif flight.state == None:
            print("Пропущено поле state")
        else:
            flight.save()
            print("Ваш полет сохранен")
            result = input("Хотите настроить уведомления? [y/n] ")
            NotificationManagerMock(flight, result)


class NotificationManagerMock:

    def __init__(self, flight, result):
        if result == 'y':
            self.flight = flight
            self.create_notifications()

    def create_notifications(self):
        t = Timer(1, self.check_time)
        t.start()

    def check_time(self):
        date = datetime.now()
        datetime_object = datetime.strptime(self.flight.departure, '%Y%m%d%H%M')
        if datetime_object > (date - timedelta(seconds=5)):
            print('Время бежать на регистрацию')
        if (datetime_object > date) & (datetime_object < date + timedelta(seconds=5)):
            print('Время идти на посадку')
        if date > datetime_object + timedelta(seconds=5):
            print('Вы прилетели')
            return None
        self.create_notifications()
