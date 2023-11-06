import ee

ee.Initialize()

id = 1
fenqu = ee.FeatureCollection("users/nanshany1993/cropNE/vectors/NE84-fenqu")
bands = ee.List(['red2','swir1','swir2','NDVI','EVI','LSWI','NDSVI','NDTI','RENDVI','REP'])
aoi = fenqu.filter(ee.Filter.eq('Id', id))
region = aoi.geometry().buffer(2000)
year = 2019
startDay = ee.Date.fromYMD(year, 1, 1)
endDay = ee.Date.fromYMD(year + 1, 1, 1)

def cloudMask(toa):
    def rescale(img, thresholds):
        return img.subtract(thresholds[0]).divide(thresholds[1] - thresholds[0])

    # Compute several indicators of cloudiness and take the minimum of them.
    score = ee.Image(1)

    # Clouds are reasonably bright in the blue band.
    score = score.min(rescale(toa.select(['blue']), [0.1, 0.5]))
    score = score.min(rescale(toa.select(['aerosol']), [0.1, 0.3]))
    score = score.min(rescale(toa.select(['aerosol']).add(toa.select(['cirrus'])), [0.15, 0.2]))
    score = score.min(rescale(toa.select(['red']).add(toa.select(['green'])).add(toa.select('blue')), [0.2, 0.8]))

    # Clouds are moist (using the Normalized Difference Moisture Index).
    ndmi = toa.normalizedDifference(['red4','swir1'])
    score = score.min(rescale(ndmi, [-0.1, 0.1]))

    # However, clouds are not snow (using the Normalized Difference Snow Index).
    ndsi = toa.normalizedDifference(['green', 'swir1'])
    score = score.min(rescale(ndsi, [0.8, 0.6]))

    # Apply a (somewhat arbitrary) threshold to identify clouds.
    cloudScoreThreshold = 0.2
    cloud = score.gt(cloudScoreThreshold)

    # Invert the cloud mask and update the image mask.
    mask = cloud.eq(0)
    return toa.updateMask(mask)

def addVariables(image):
    DOY = ee.Date(image.date()).getRelative('day', 'year')
    year = ee.Date(image.date()).get('year')

    # Add a NDVI band.
    ndvi = image.normalizedDifference(['nir', 'red']).toDouble().rename('NDVI')
    # Add a EVI band.
    evi = image.expression(
        '2.5*((nir-red)/(nir+6*red-7.5*blue+1))', {
            'nir': image.select('nir'),
            'red': image.select('red'),
            'blue': image.select('blue')
        }).toDouble().rename('EVI')
    # Add a GCVI band.
    gcvi = image.expression(
        'nir/green-1', {
            'nir': image.select('nir'),
            'green': image.select('green'),
        }).toDouble().rename('GCVI')
    # Add a MSAVI2 band.
    msavi2 = image.expression(
        '1/2 * (2*nir + 1 - ((2*nir+1)**2 - 8*(nir-red))**(1/2))', {
            'nir': image.select('nir'),
            'red': image.select('red'),
        }).toDouble().rename('MSAVI2')

    # Continue adding the rest of the indices similarly...
    lswi = image.normalizedDifference(['nir', 'swir1']).toDouble().rename('LSWI')
    ndwi = image.normalizedDifference(['green', 'nir']).toDouble().rename('NDWI')
    ndsi = image.normalizedDifference(['green', 'swir1']).toDouble().rename('NDSI')
    ndsvi = image.normalizedDifference(['swir1', 'red']).toDouble().rename('NDSVI')
    ndti = image.normalizedDifference(['swir1', 'swir2']).toDouble().rename('NDTI')
    rendvi = image.normalizedDifference(['nir', 'red2']).toDouble().rename('RENDVI')

    # ... Add expressions for REP, PSRI, and CRE ...
    rep = image.expression(
        '(705+35*(0.5*(red3+red)-red1)/(red2-red1))/1000', {
            'red3': image.select('red3'),
            'red2': image.select('red2'),
            'red1': image.select('red1'),
            'red': image.select('red'),
        }).toDouble().rename('REP')
    psri = image.expression(
        '(red-blue)/red1', {
            'red': image.select('red'),
            'red1': image.select('red1'),
            'blue': image.select('blue'),
        }).toDouble().rename('PSRI')
    cre = image.expression(
        'red1/nir', {
            'red1': image.select('red1'),
            'nir': image.select('nir'),
        }).toDouble().rename('CRE')

    # Add DOY and year bands
    doy_band = ee.Image(DOY).rename('DOY').toDouble()
    year_band = ee.Image(year).rename('Year').toDouble()

    # Combine everything into one image and set properties.
    return image.addBands([ndvi, evi, gcvi, msavi2, lswi, ndwi, ndsi, ndsvi, ndti, rendvi, rep, psri, cre, doy_band, year_band]).set('DOY', DOY)



s2 = (ee.ImageCollection("COPERNICUS/S2")
      .filterBounds(region)
      .filterDate(startDay, endDay)
      .map(cloudMask)
    #   .map(sentinel2toa)
      .map(addVariables))
s2filtered = s2.select(bands)

print(s2filtered.size().getInfo())
