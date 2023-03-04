import sys
import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
orm_dir_path = os.path.abspath(os.path.join(dir_path, '..'))
sys.path.append(orm_dir_path)


# A continuación, importar todos los módulos que necesites para las pruebas
from ormgap.models.accession import Accession
from ormgap.models.crop import Crop
from ormgap.models.country import Country
from ormgap.models.group import Group