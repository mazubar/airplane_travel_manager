from database.base import *
from database.base import db_travel

db_travel.connect()

db_travel.create_tables([
    Account, Flight, Playlist, Audio, ChatBot, Notification, Card
])