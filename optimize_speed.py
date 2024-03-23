# COG
'''
$ gdal_translate -of COG input.tif output.tif
$ gdal_translate -of COG 2023_30m_cdls.tif 2023_30m_cdls_COG.tif

# for large file
gdal_translate -of COG -co BIGTIFF=YES cdl_10m/2023_30m_cdls.tif cdl_10m_COG_3857/2023_30m_cdls.tif
'''
# https://mapscaping.com/complete-guide-to-cloud-optimized-geotiffs/#:~:text=To%20convert%20a%20TIFF%20file,can%20use%20the%20gdal_translate%20command.&text=This%20command%20will%20create%20a,which%20is%20a%20regular%20TIFF.


# reproject to epsg:3857
from osgeo import gdal

filename = r"C:\path\to\input\raster"
input_raster = gdal.Open(filename)
output_raster = r"C:\path\to\output\raster"
warp = gdal.Warp(output_raster,input_raster,dstSRS='EPSG:4326')
warp = None # Closes the files
# https://gis.stackexchange.com/questions/233589/re-project-raster-in-python-using-gdal
# because delta hasn't installed gdal, I used gdalwarp instead:
'''
$ gdalwarp -t_srs EPSG:3857 -co BIGTIFF=YES /scratch/bcnh/data/cdl_10m_COG/2023_30m_cdls.tif /scratch/bcnh/data/cdl_10m_COG_3857/2023_30m_cdls.tif
'''


# reproject to 10m
# I used QGIS, but the code is similar to this:
'''
$ gdalwarp -overwrite -tr 10.0 10.0 -r near -of GTiff /scratch/bcnh/data/cdl/2023_30m_cdls.tif /scratch/bcnh/data/cdl_10m/2023_30m_cdls.tif
'''