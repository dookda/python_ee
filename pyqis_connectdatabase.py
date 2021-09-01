import os
import glob
from qgis.core import *

uri = QgsDataSourceUri()
uri.setConnection("localhost", "5432", "pydb", "postgres", "1234")
uri.setDataSource("public", "cm_tambon_4326", "geom", "gid>=0", "gid")

#vlayer = QgsVectorLayer(uri.uri(False), "", "postgres")
iface.addVectorLayer(uri.uri(False), "tambon", "postgres")
