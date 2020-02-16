from peewee import *

db_travel = SqliteDatabase('travel.db')


class BaseModel(Model):
    class Meta:
            database = db_travel
