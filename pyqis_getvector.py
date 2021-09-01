import os
import glob
from qgis.core import *

amp_layer = r"/Users/sakdahomhuan/workspace/lab_database_432/data4326/cm_amphoe_4326.shp"
lyr = iface.addVectorLayer(amp_layer, "", "ogr")

#iface.showAttributeTable(lyr)

for f in lyr.fields():
    print(f.name())

lyr.setSubsetString("AMP_NAM_E LIKE '%K%'")

## loop data
#fld = os.chdir(r"/Users/sakdahomhuan/workspace/lab_database_432/data4326") 
#shp = glob.glob("*.shp")
#
#for s in shp:
#    print(s)
#    iface.addVectorLayer(s, "", "ogr")
    
    
    
    