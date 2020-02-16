from Database.base import *
from Database.base import db_travel

db_travel.connect()

db_travel.create_tables([
    Account, Flight, Playlist, Audio, ChatBot, Notification, Card
])