# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

"""AgriFieldNet India Challenge dataset."""

from torchgeo.datasets import RasterDataset
import os
from collections.abc import Callable, Iterable
from typing import Any
from matplotlib.figure import Figure


class AgriFieldNetMask(RasterDataset):
    """AgriFieldNetMask India Challenge dataset."""
    is_image = False

    def plot(
        self,
        sample: dict[str, Any],
        show_titles: bool = True,
        suptitle: str | None = None,
        mask_filename: str | None = None,
        pred_filename: str | None = None,
    ) -> Figure:
        """Plot a sample from the dataset.

        Args:
            sample: a sample returned by :meth:`RasterDataset.__getitem__`
            show_titles: flag indicating whether to show titles above each panel
            suptitle: optional string to use as a suptitle

        Returns:
            a matplotlib Figure with the rendered sample

        .. versionchanged:: 0.3
           Method now takes a sample dict, not a Tensor. Additionally, possible to
           show subplot titles and/or use a custom suptitle.
        """
        import numpy as np
        from PIL import Image
        import os

        mask = sample['mask'].squeeze()

        showing_predictions = 'prediction' in sample
        if showing_predictions:
            pred = sample['prediction'].squeeze()

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

        mask = mask.numpy().astype(np.uint8)
        mask = mapping[mask]
        img = Image.fromarray(mask)
        img.save(os.path.join("agrifieldnet_figures", mask_filename))

        pred = mapping[pred]
        pred_img = Image.fromarray(pred)
        pred_img.save(os.path.join("agrifieldnet_figures", pred_filename))

        return
