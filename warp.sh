gdalwarp -t_srs EPSG:3857 -overwrite -tr 10.0 10.0 -r near -of GTiff -co BIGTIFF=YES -co BLOCKXSIZE=256 -co BLOCKYSIZE=256 -dstnodata 0 -tap /Users/yc/Datasets/NCCM_harmonized_class/CDL2019_clip.tif /Users/yc/Datasets/NCCM_harmonized_class_tap_block/CDL2019_clip.tif

gdal_translate -of COG -co BIGTIFF=YES -co BLOCKXSIZE=256 /Users/yc/Datasets/NCCM_harmonized_class_tap_block/CDL2019_clip.tif /Users/yc/Datasets/NCCM_harmonized_block/CDL2019_clip.tif

gdalwarp -t_srs EPSG:3857 -overwrite -tr 10.0 10.0 -r near -of GTiff -co BIGTIFF=YES -tap /scratch/bcnh/data/cdl/2023_30m_cdls.tif /scratch/bcnh/data/cdl_tap/2023_30m_cdls.tif

gdal_translate -of COG -co BIGTIFF=YES /scratch/bcnh/data/cdl_tap/2023_30m_cdls.tif /scratch/bcnh/data/cdl_tap_COG/2023_30m_cdls.tif

gdalwarp  -tr 10.0 10.0 -r near -of GTiff -tap T00AAA_20230701T000000_B01.tif -- -31_-17_2023_10m/T00AAA_20230701T000000_B01.tif

gdal_translate -of COG -co BIGTIFF=YES 31_-17_2023_tap/T00AAA_20230701T000000_B01.tif 31_-17_2023_tap_COG/T00AAA_20230701T000000_B01.tif


python3 -m torchgeo fit --config experiments/torchgeo/conf/sentinel2_cdl.yaml
