This contains code and torchgeo experiment configurations related to EuroCrops experiments for crop type transfer learning project.

The steps to setting up the data are:

1. Run eurocrops_harmonize.py on EuroCrops data (can be downloaded through torchgeo).
   This will choose only the crop types we care about.

2. Run find_good_images.py on Sentinel-2 + EuroCrops. This will create an output folder
   containing only the Sentinel-2 images where EuroCrops has one of the crop types we
   actually care about.

3. Run rasterize.py to rasterize both datasets into small crops.

4. Then can run the experiments.

The rasterized data is currently available on `prior-elanding-52.reviz.ai2.in:/data/favyenb/eurocrops/`
(specifically the eurocrops_cropped and sentinel2_cropped subfolders).
