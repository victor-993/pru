import unittest
from mongoengine import connect
from orm.models.group import Group
from orm.models.crop import Crop

class TestGroup(unittest.TestCase):
    def setUpClass(cls):
        connect('test_gap_analysis', host='mongomock://localhost')

    def setUp(self):
        self.crop = Crop(name='Test Crop', base_name='Test Crop Base', app_name='Test Crop App').save()
        self.group = Group(
            group_name='Landraces of corn',
            crop=self.crop,
            ext_id='1234'
        )
    def test_create_group(self):
        self.group.save()
        self.assertIsNotNone(self.group.id)

        group = Group.objects(id=self.crop.id).first()
        self.assertEqual(group.group_name,'Landraces of corn')
        self.assertEqual(group.crop, self.crop)        
        self.assertEqual(group.ext_id,'1234')

    def tearDown(self):
        self.crop.delete()
        Group.objects.delete()