"""
Filter the 256x256 Sentinel-2 images for ones that have at least one pixel that is labeled 1-4
(one of the crop type categories of interest).
"""
import os
import shutil
from datetime import datetime

import torch
import tqdm

from torchgeo.datasets import EuroCrops, Sentinel2
from torchgeo.samplers import PreChippedGeoSampler

src_dir = "/data/favyenb/eurocrops/sentinel2"
eurocrops_dir = "/data/favyenb/eurocrops/eurocrops_harmonized"
dst_dir = "/data/favyenb/eurocrops/sentinel2_harmonized"

sentinel2 = Sentinel2(paths=src_dir, cache=False)
eurocrops = EuroCrops(paths=eurocrops_dir, classes=["0000000001", "0000000002", "0000000003", "0000000004", "0000000005"])
dataset = sentinel2 & eurocrops
sampler = PreChippedGeoSampler(dataset)

loader = torch.utils.data.DataLoader(
    dataset=dataset,
    sampler=sampler,
    num_workers=64,
    batch_size=None,
)

for i, data in tqdm.tqdm(enumerate(loader)):
    if torch.count_nonzero((data["mask"] > 0) & (data["mask"] < 5)) == 0:
        continue

    year = datetime.fromtimestamp(data["bbox"].mint).year
    col = int(data["bbox"].minx) // 2560
    row = int(data["bbox"].maxy) // -2560
    scene_name = f"{year}_{col}_{row}"
    print(scene_name)
    if os.path.exists(os.path.join(dst_dir, scene_name)):
        print("exists")
        continue
    shutil.copytree(
        os.path.join(src_dir, scene_name),
        os.path.join(dst_dir, scene_name),
    )
