from Database.base import db_travel

from peewee import *
 
class Account(Model):
    user_id = AutoField()
    login = CharField(unique=True)
    name = CharField()
    password = CharField()

    class Meta:
        database = db_travel
        table_name = "account"
 
class Flight(Model):
    flight_id = AutoField()
    number = CharField()
    date = DateField()
    departure_time = TimeField()

    class Meta:
        database = db_travel
        table_name = "flight"
 
class Playlist(Model):
    playlist_id = AutoField()
    title = CharField()
    description = CharField(null=True)
    songs_num = IntegerField()

    class Meta:
        database = db_travel
        table_name = "playlist"
 
class Audio(Model):
    audio_id = AutoField()
    artist = CharField(default = 'Various Artists')
    name = CharField()
    duration = IntegerField() #в секундах
    genre = CharField(null = True)
    playlist = ForeignKeyField(Playlist)
    isLiked = BooleanField(default = False)
    audio_type = CharField()

    class Meta:
        database = db_travel
        table_name = "audio"
 
class ChatBot(Model):
    name = CharField()
    voice = BooleanField()
    language = CharField()

    class Meta:
        database = db_travel
        table_name = "chat_bot"
 
class Notification(Model):
    notification_id = AutoField()
    text = TextField()
    created = DateTimeField()

    class Meta:
        database = db_travel
        table_name = "notification"
 
class Card(Model):
    card_id = AutoField()
    text = TextField()

    class Meta:
        database = db_travel
        table_name = "card"
