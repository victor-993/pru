from mongoengine import Document, StringField

class Crop(Document):
    meta = {
        'collection': 'crop'
    }
    ext_id = StringField(max_length=100, unique=True, required=True)
    name = StringField(max_length=150, required=True)
    base_name = StringField(max_length=100)
    app_name = StringField(max_length=150)