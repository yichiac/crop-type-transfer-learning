import matplotlib.pyplot as plt
import segmentation_models_pytorch as smp
import torch

from torchgeo.datamodules import Sentinel2NCCMDataModule

device = torch.device("cuda")

model = smp.Unet(encoder_name="resnet50", in_channels=13, classes=6)
model.to(device)

# sentinel2_bands=["B01","B02","B03","B04","B05","B06","B07","B08","B8A","B09","B10","B11","B12"]
sentinel2_bands=["B01","B04","B03","B02","B05","B06","B07","B08","B09","B10","B11","B12","B8A"]
# sentinel2_bands=["B02","B03","B04","B05","B06","B07","B08","B09","B10","B11","B12","B8A","B01"]

datamodule = Sentinel2NCCMDataModule(
    crs="epsg:3857",
    batch_size=1,
    patch_size=256,
    nccm_paths="/data/yichiac/nccm_harmonized_block",
    sentinel2_paths="/data/yichiac/nccm_2019_tiny",
    sentinel2_bands=sentinel2_bands,
)

datamodule.setup("fit")

for batch in datamodule.train_dataloader():
    image = batch["image"]
    mask = batch["mask"]
    image.to(device)

for i in range(13):
    print(sentinel2_bands[i])
    print(image[0][i][0][100:105])
