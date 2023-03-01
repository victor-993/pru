from mongoengine import Document, StringField, ReferenceField, FloatField
from .crop import Crop
from .group import Group

class Accession(Document):
    meta = {
        'collection': 'accession'
    }
    species_name = StringField(max_length=150, required=True)
    crop = ReferenceField(Crop, required=True)
    landrace_group = ReferenceField(Group, required=True)
    institution_name = StringField(max_length=255)
    source_database = StringField(max_length=255)
    latitude = FloatField()
    longitude = FloatField()
    accession_id = StringField(max_length=255)
    other_attributes = StringField()