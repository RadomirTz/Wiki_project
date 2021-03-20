from peewee import *

db = SqliteDatabase('wiki.db')

class person(Model):
    
    title = CharField()
    image = CharField()
    text_wiki = TextField(null=True)

    class Meta:
        database = db
        