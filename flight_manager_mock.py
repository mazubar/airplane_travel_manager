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
            self.show_result("Пропущено поле number")
            return None
        elif flight.departure == None:
            self.show_result("Пропущено поле departure")
            return None
        elif flight.state == None:
            self.show_result("Пропущено поле state")
        else:
            flight.save()
            self.show_result("Ваш полет сохранен")
            self.offer_setup_notifications(flight)

    def show_result(self, result):
        print(result)

    def offer_setup_notifications(self, flight):
        result = input("Хотите настроить уведомления? [y/n] ")
        if result == 'y':
            self.load_notifications(flight)

    def load_notifications(self, flight):
        NotificationManagerMock(flight)


class NotificationManagerMock:

    def __init__(self, flight):
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
