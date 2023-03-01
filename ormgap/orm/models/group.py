from mongoengine import Document, StringField, ReferenceField
from .crop import Crop

class Group(Document):
    meta = {
        'collection': 'group'
    }
    group_name = StringField(max_length=255, required=True)
    crop = ReferenceField(Crop, required=True)
    ext_id = StringField(max_length=100)