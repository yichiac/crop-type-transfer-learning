"""
Rasterize the EuroCrops data.
"""
import os
from datetime import datetime

import affine
import numpy as np
import rasterio
import torch
import tqdm

from torchgeo.datasets import EuroCrops, Sentinel2
from torchgeo.samplers import PreChippedGeoSampler

eurocrops_in_dir = "/data/favyenb/eurocrops/eurocrops_harmonized"
sentinel2_in_dir = "/data/favyenb/eurocrops/sentinel2_harmonized"
eurocrops_out_dir = "/data/favyenb/eurocrops/eurocrops_cropped"
sentinel2_out_dir = "/data/favyenb/eurocrops/sentinel2_cropped"

sentinel2 = Sentinel2(paths=sentinel2_in_dir, cache=False)
eurocrops = EuroCrops(paths=eurocrops_in_dir, classes=["0000000001", "0000000002", "0000000003", "0000000004", "0000000005"])
dataset = sentinel2 & eurocrops
sampler = PreChippedGeoSampler(dataset)

loader = torch.utils.data.DataLoader(
    dataset=dataset,
    sampler=sampler,
    num_workers=128,
    batch_size=None,
)

for i, data in tqdm.tqdm(enumerate(loader)):
    year = datetime.fromtimestamp(data["bbox"].mint).year
    col = int(data["bbox"].minx) // 2560
    row = int(data["bbox"].maxy) // -2560
    eurocrops_out_fname = os.path.join(eurocrops_out_dir, f"{year}_{col}_{row}.tif")
    sentinel2_out_fname = os.path.join(sentinel2_out_dir, f"{year}_{col}_{row}.tif")
    if os.path.exists(eurocrops_out_fname) and os.path.exists(sentinel2_out_fname):
        continue

    resolution = 10
    transform = affine.Affine(
        resolution,
        0,
        data["bbox"].minx,
        0,
        -resolution,
        data["bbox"].maxy,
    )
    mask = data["mask"].numpy()[None, :, :].astype(np.uint8)
    profile = {
        "driver": "GTiff",
        "compress": "lzw",
        "width": mask.shape[2],
        "height": mask.shape[1],
        "count": mask.shape[0],
        "dtype": mask.dtype.name,
        "crs": data["crs"],
        "transform": transform,
    }
    with rasterio.open(eurocrops_out_fname, "w", **profile) as dst:
        dst.write(mask)

    image = data["image"].numpy().astype(np.uint16)
    profile = {
        "driver": "GTiff",
        "compress": "lzw",
        "width": image.shape[2],
        "height": image.shape[1],
        "count": image.shape[0],
        "dtype": image.dtype.name,
        "crs": data["crs"],
        "transform": transform,
    }
    with rasterio.open(sentinel2_out_fname, "w", **profile) as dst:
        dst.write(image)
