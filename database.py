
from peewee import *

db = SqliteDatabase('artworks.sqlite')


class BaseModel(Model):
    class Meta:
        database = db


class Artist(BaseModel):

    artist_name = CharField(unique=True)
    email = CharField()


class Artwork(BaseModel):

    artwork_name = CharField(unique=True)
    price = DecimalField()
    available = BooleanField(default=True)
    artist = ForeignKeyField(Artist, backref='artworks')

    class Meta:
        database = db


db.connect()
db.create_tables([Artist, Artwork])