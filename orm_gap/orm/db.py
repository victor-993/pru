from mongoengine import connect
from models.country import Country

connect(host='mongodb://root:s3cr3t@localhost:27017/dbgap?authSource=admin')

country = Country(iso_2='Cp', name='Colombia').save()
