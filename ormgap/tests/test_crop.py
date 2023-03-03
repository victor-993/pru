import unittest
from mongoengine import connect
from orm.models.crop import Crop

class TestCrop(unittest.TestCase):
    def setUpClass(cls):
        connect('test_gap_analysis', host='mongomock://localhost')

    def setUp(self):
        self.crop = Crop(
            ext_id='1234',
            name='corn',
            base_name='zea_mays',
            app_name='Corn'
        )

    def test_create_crop(self):
        # Crea un nuevo crop
        
        self.crop.save()
        self.assertIsNotNone(self.crop.id)

        # Verifica que el crop haya sido creado exitosamente
        crop = Crop.objects(id=self.crop.id).first()
        self.assertEqual(crop.ext_id, '1234')
        self.assertEqual(crop.name, 'corn')
        self.assertEqual(crop.base_name, 'zea_mays')
        self.assertEqual(crop.app_name, 'Corn')

    def tearDown(self):
        Crop.objects.delete()