import ee

ee.Authenticate()
# 4/1AX4XfWj7Nn-1ZJTDy58cDhnYKwTMOtQCYHzkgZEoamZLNfjgs2GPUpO-jXk
ee.Initialize()
# Load a Landsat image.
img = ee.Image('LANDSAT/LT05/C01/T1_SR/LT05_034033_20000913')

# Print image object WITHOUT call to getInfo(); prints serialized request instructions.
print(img)

# Print image object WITH call to getInfo(); prints image metadata.
print(img.getInfo())
