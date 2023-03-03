import sys
import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
orm_dir_path = os.path.abspath(os.path.join(dir_path, '..'))
sys.path.append(orm_dir_path)


# A continuación, importar todos los módulos que necesites para las pruebas
from orm.models.accession import Accession
from orm.models.crop import Crop
from orm.models.country import Country
from orm.models.group import Group