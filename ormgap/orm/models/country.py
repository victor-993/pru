from mongoengine import Document, StringField

class Country(Document):
    meta = {
        'collection': 'country'
    }
    iso_2 = StringField(max_length=2, unique=True, required=True)
    name = StringField(max_length=150, required=True)