import os
import glob
from qgis.core import *

#amp_layer = r"/Users/sakdahomhuan/workspace/lab_database_432/data4326/cm_amphoe_32647.shp"
#lyr = iface.addVectorLayer(amp_layer, "", "ogr")
#
#lyr.setSubsetString("AMP_NAM_E LIKE '%K%'")

#buffer
#result = processing.run("native:buffer",{'INPUT':lyr,'DISTANCE':5000,'SEGMENTS':5,'END_CAP_STYLE':0,'JOIN_STYLE':0,'MITER_LIMIT':2,
#'DISSOLVE':False,'OUTPUT':'memory:'})
#
#QgsProject.instance().addMapLayer(result["OUTPUT"])


#result = processing.run("native:centroids", { 'INPUT': lyr, 'ALL_PARTS': True, 'OUTPUT':'memory:' })
#QgsProject.instance().addMapLayer(result["OUTPUT"])
#outVertex = r"/Users/sakdahomhuan/workspace/a23032021/output/strm_sub_vtex50.shp"
strm = r"/Users/sakdahomhuan/workspace/a23032021/output/strm_sub.shp"

strm_vertex = r"/Users/sakdahomhuan/workspace/a23032021/output/strm_sub_v.shp"

strm_layer = iface.addVectorLayer(strm, "", "ogr")
result = processing.run("native:densifygeometriesgivenaninterval", {
    'INPUT': strm_layer,
    'INTERVAL': 100.0,
    'OUTPUT': 'memory:'
    })
QgsProject.instance().addMapLayer(result["OUTPUT"])

result = processing.run("native:transect", {
    'INPUT': result["OUTPUT"],
    'LENGTH': 100,
    'ANGLE': 90,
    'SIDE': 2,
    'OUTPUT': 'memory:'
    })
QgsProject.instance().addMapLayer(result["OUTPUT"])

