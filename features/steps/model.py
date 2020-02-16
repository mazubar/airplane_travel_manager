import datetime
from peewee import *
db_travel = SqliteDatabase('travel.db')
 
class BaseModel(Model):
    class Meta:
        database = db_travel
 
class Account(BaseModel):
    user_id = AutoField()
    login = CharField(unique=True)
    name = CharField()
    password = CharField()
    notifications = BooleanField(default = True)
   
  def add_user(self, login, name, password):
    self.login = login
    self.name = name
    self.password = password
    self.save()
 
class Flight(BaseModel):
    flight_id = AutoField()
    number = CharField()
    departure = DateTimeField()
    state = CharField()
    
  def add_flight(self, number, departure):
    self.number = number
    self.departure = departure
    self.save()
 
class Playlist(BaseModel):
    playlist_id = AutoField()
    title = CharField()
    description = CharField(null=True)
    songs_num = IntegerField()
    
  def add_song(self):
    self.songs_num += self.songs_num
    self.save()
 
class Audio(BaseModel):
    audio_id = AutoField()
    artist = CharField(default = 'Various Artists')
    name = CharField()
    duration = IntegerField() #в секундах
    genre = CharField(null = True)
    playlist = ForeignKeyField(Playlist)
    isLiked = BooleanField(default = False)
    audio_type = CharField()
    
  def like(self):
    self.isLiked = True
    self.save()
 
class ChatBot(BaseModel):
    name = CharField()
    voice = BooleanField()
    language = CharField()
 
class Notification(BaseModel):
    notification_id = AutoField()
    text = TextField()
    created = DateTimeField()
    flight = ForeignKeyField(Flight)
    
  def get_registration_info(self, flight) 
    if Flight['flight_id' == flight].state == 'registraion': 
       self.text = 'Регистрация на рейс ' + Flight.number + ' началась. Стойки регистрации: ' + input('reg_desks')
       self.created = datetime.datetime.now
     #это по идее должно подгружаться из стороннего источника (скажем, с сайта аэропорта)
 
class Card(BaseModel):
    card_id = AutoField()
    text = TextField()
   
   def show_card(self):
    print(self.text)
    
    
from database.model import *
from threading import Timer
from datetime import datetime, timedelta



#функция сохранения рейса
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

#функция отправления уведомления
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
