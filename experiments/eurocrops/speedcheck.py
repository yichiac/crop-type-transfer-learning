"""
Check speed when using Sentinel-2 crops + rasterized EuroCrops crops.
"""
import time

import torch
import tqdm

from torchgeo.datasets import RasterDataset, Sentinel2
from torchgeo.samplers import PreChippedGeoSampler

eurocrops_dir = "/data/favyenb/eurocrops/eurocrops_cropped"
sentinel2_dir = "/data/favyenb/eurocrops/sentinel2_harmonized"

class RasterizedEuroCrops(RasterDataset):
    filename_glob = "*.tif"
    filename_regex = r"""
        ^(?P<date>\d{4})
        _.*$
    """
    date_format = "%Y"
    is_image = False

t0 = time.time()
sentinel2 = Sentinel2(paths=sentinel2_dir, cache=False)
print("loaded sentinel-2 in", time.time() - t0)

t0 = time.time()
eurocrops = RasterizedEuroCrops(paths=eurocrops_dir)
print("loaded eurocrops in", time.time() - t0)

t0 = time.time()
dataset = sentinel2 & eurocrops
print("computed intersection in", time.time() - t0)

t0 = time.time()
sampler = PreChippedGeoSampler(dataset)
loader = torch.utils.data.DataLoader(
    dataset=dataset,
    sampler=sampler,
    num_workers=0,
    batch_size=128,
    collate_fn=lambda x: x,
)
print("sampler+loader in", time.time() - t0)

for i, data in tqdm.tqdm(enumerate(loader), total=len(sampler)):
    pass
