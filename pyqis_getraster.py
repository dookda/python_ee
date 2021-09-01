import os
import glob
from qgis.core import *

fname = r"/Users/sakdahomhuan/workspace/lab_database_432/data4326/cm_dem32647.ovr"

iface.addRasterLayer(fname, "dem")

