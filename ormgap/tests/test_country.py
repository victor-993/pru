import unittest
from mongoengine import connect
from orm.models.country import Country

class TestCountry(unittest.TestCase):

    def setUp(self):
        connect('test_gap_analysis', host='mongomock://localhost')
        self.country = Country(
            iso_2='US',
            name='United States of America'
        )

    def test_create_country(self):
        # Crea un nuevo country
        self.country.save()
        self.assertIsNotNone(self.country.id)

        # Verifica que el country haya sido creado exitosamente
        country = Country.objects(id=self.country.id).first()
        self.assertEqual(country.iso_2, 'US')
        self.assertEqual(country.name, 'United States of America')
    
    
    def tearDown(self):
        Country.objects.delete()

if __name__ == '__main__':
    unittest.main()