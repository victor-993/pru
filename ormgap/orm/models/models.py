from mongoengine import Document, StringField, ReferenceField, FloatField

class Country(Document):
    ISO_2 = StringField(max_length=2, unique=True, required=True)
    name = StringField(max_length=150, required=True)

class Crop(Document):
    ext_id = StringField(max_length=100, unique=True, required=True)
    name = StringField(max_length=150, required=True)
    base_name = StringField(max_length=100)
    app_name = StringField(max_length=150)

class Group(Document):
    group_name = StringField(max_length=255, required=True)
    crop = ReferenceField(Crop, required=True)
    ext_id = StringField(max_length=100)

class Accession(Document):
    species_name = StringField(max_length=150, required=True)
    crop = ReferenceField(Crop, required=True)
    landrace_group = ReferenceField(Group, required=True)
    institution_name = StringField(max_length=255)
    source_database = StringField(max_length=255)
    latitude = FloatField()
    longitude = FloatField()
    accession_id = StringField(max_length=255)
    other_attributes = StringField()