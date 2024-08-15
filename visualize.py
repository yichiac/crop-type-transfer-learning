"""Usage: python3 visualize.py <path to images> <path to masks> <path to checkpoint>."""

import os
import sys

import numpy as np
import segmentation_models_pytorch as smp
import torch
from PIL import Image
from torch.utils.data import DataLoader
from torchgeo.datasets import RasterDataset, stack_samples, unbind_samples
from torchgeo.samplers import PreChippedGeoSampler


class ImageDataset(RasterDataset):
    is_image = True

    all_bands = [
        "B01",
        "B02",
        "B03",
        "B04",
        "B05",
        "B06",
        "B07",
        "B08",
        "B09",
        "B10",
        "B11",
        "B12",
        "B8A",
    ]

    def plot(self, image, filename):
        image = image[[3, 2, 1]].permute(1, 2, 0).numpy()
        minv = 1300
        maxv = 3500
        image = (image - minv) / (maxv - minv)
        image = np.clip(image, 0, 1)
        image *= 255
        image = image.astype(np.uint8)
        img = Image.fromarray(image)
        img.save(os.path.join("figures", filename))


class MaskDataset(RasterDataset):
    is_image = False
    cmap = {
        0: (0, 0, 0, 255),
        1: (255, 211, 0, 255),
        2: (37, 111, 0, 255),
        3: (0, 168, 226, 255),
        4: (137, 96, 83, 255),
        5: (128, 128, 128, 255),
    }
    mapping = np.zeros((max(cmap) + 1, 4), dtype=np.uint8)
    for key, value in cmap.items():
        mapping[key] = value

    def plot(self, mask, filename):
        mask = mask.numpy().astype(np.uint8)
        mask = self.mapping[mask]
        img = Image.fromarray(mask)
        img.save(os.path.join("figures", filename))


if __name__ == "__main__":
    os.makedirs("figures", exist_ok=True)

    # Datasets
    bands = [
        "B01",
        "B02",
        "B03",
        "B04",
        "B05",
        "B06",
        "B07",
        "B08",
        "B8A",
        "B09",
        "B10",
        "B11",
        "B12",
    ]
    image_dataset = ImageDataset(
        sys.argv[1],
    )
    mask_dataset = MaskDataset(sys.argv[2])
    dataset = image_dataset & mask_dataset

    # Samplers
    sampler = PreChippedGeoSampler(image_dataset)

    # Data Loaders
    dataloader = DataLoader(
        dataset,
        batch_size=100,
        sampler=sampler,
        collate_fn=stack_samples,
        num_workers=10,
    )

    # Model
    device = torch.device("mps")
    model = smp.Unet(encoder_name="resnet50", in_channels=13, classes=6)
    model = model.to(device)

    # Load checkpoint
    state_dict = torch.load(sys.argv[3], map_location=device, weights_only=True)[
        "state_dict"
    ]
    state_dict = {key.replace("model.", ""): value for key, value in state_dict.items()}
    model.load_state_dict(state_dict, strict=True)

    model.eval()
    with torch.no_grad():
        for batch in dataloader:
            image = batch["image"].to(device) / 10000
            mask = batch["mask"]

            # Make a prediction
            prediction = model(image)
            prediction = prediction.argmax(dim=1)
            prediction = prediction.detach().to("cpu")
            batch["prediction"] = prediction

            for i, sample in enumerate(unbind_samples(batch)):
                image = sample["image"]
                mask = sample["mask"][0]
                prediction = sample["prediction"]

                # Skip nodata pixels
                if 0 in mask:
                    continue

                # Skip boring images
                if len(mask.unique()) < 3:
                    continue

                # Plotting
                image_dataset.plot(image, f"cdl_{i:02}_image.png")
                mask_dataset.plot(mask, f"cdl_{i:02}_mask.png")
                mask_dataset.plot(prediction, f"cdl_{i:02}_prediction.png")
