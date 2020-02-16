from peewee import Model
from playhouse.postgres_ext import PostgresqlExtDatabase

db = PostgresqlExtDatabase('di_app', user='app', password='app',
host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
            database = db
