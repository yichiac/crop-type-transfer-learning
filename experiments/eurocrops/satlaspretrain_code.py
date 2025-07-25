
import satlaspretrain_models
import torch
from lightning.pytorch import Trainer

from torchgeo.datamodules import Sentinel2CDLDataModule

batch_size = 128
patch_size = 256
num_workers = 0
max_epochs = 10
fast_dev_run = False

datamodule = Sentinel2CDLDataModule(
    batch_size = batch_size, patch_size = patch_size, num_workers = num_workers,
    cdl_paths = "/data/yichiac/cdl_harmonized_block",
    cdl_years = [2023],
    sentinel2_paths = "/data/yichiac/cdl_2023_small",
    sentinel2_cache =False,
    sentinel2_bands = ["B02", "B03", "B04", "B05", "B06", "B07", "B08", "B11", "B12"]
)

print('finish loading datamodule')

weights_manager = satlaspretrain_models.Weights()



task = SatlasSemanticSegmentationTask(
    num_classes=6,
    freeze_backbone=True,
    model_identifier="Sentinel2_Resnet50_SI_MS",
    pretrained=True,
    fpn=True,
    ignore_index=0,
)


accelerator = "gpu" if torch.cuda.is_available() else "cpu"

trainer = Trainer(
    accelerator=accelerator,
    default_root_dir="/data/piperw/projects/uiuc/torchgeo",
    fast_dev_run=fast_dev_run,
    log_every_n_steps=1,
    min_epochs=1,
    max_epochs=max_epochs,
)

trainer.fit(model=task, datamodule=datamodule)
