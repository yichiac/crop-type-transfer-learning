import ee

ee.Initialize()

fenqu = ee.FeatureCollection("users/nanshany1993/cropNE/vectors/NE84-fenqu")

task = ee.batch.Export.table.toDrive(
    collection=fenqu,
    description='fenqu_to_shapefile',
    folder='Northeastern_China_boundary',  # Optional: specify a folder in your Google Drive
    fileNamePrefix='fenqu_shapefile',
    fileFormat='SHP'  # Shapefile format
)

# Start the export task
task.start()

# fenqu.getDownloadURL()

# id = 1
# bands = ee.List(['red2','swir1','swir2','NDVI','EVI','LSWI','NDSVI','NDTI','RENDVI','REP'])
# aoi = fenqu.filter(ee.Filter.eq('Id', id))
# year = 2019
# startDay = ee.Date.fromYMD(year, 1, 1)
# endDay = ee.Date.fromYMD(year + 1, 1, 1)
