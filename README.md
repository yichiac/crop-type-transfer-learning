# On the Generalizability of Foundation Models for Crop Type Mapping

[![arXiv](https://img.shields.io/badge/arXiv-Paper-red?logo=arxiv)](https://arxiv.org/abs/2409.09451)
[![Hugging Face](https://img.shields.io/badge/HuggingFace-TorchGeo-yellow?logo=huggingface&logoColor=yellow)](https://huggingface.co/torchgeo)
[![GitHub](https://img.shields.io/badge/GitHub-TorchGeo-4CB05B?logo=github&logoColor=white)](https://github.com/microsoft/torchgeo)

This is the official repository for the paper "_On the Generalizability of Foundation Models for Crop Type Mapping_", acctped at [IEEE IGARSS 2025](https://www.2025.ieeeigarss.org/).

Authors: [Yi-Chia Chang](https://yichiac.github.io/), [Adam J. Stewart](https://github.com/adamjstewart), [Favyen Bastani](https://favyen.com/), [Piper Wolters](https://piperwolters.com/), Shreya Kannan, George R. Huber, Jingtong Wang, [Arindam Banerjee](https://arindam.cs.illinois.edu/index.html).


## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yichiac/crop-type-transfer-learning.git
    cd crop-type-transfer-learning
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv env
    source env/bin/activate
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Download Dataset
The dataset is available on the [HuggingFace](https://huggingface.co/datasets/torchgeo/harmonized_global_crops).
Login to download the crop type datasets.
```sh
huggingface-cli login
```
You can run the following Python script to download the dataset:
```python
from huggingface_hub import snapshot_download
snapshot_download(repo_id="torchgeo/harmonized_global_crops", repo_type="dataset", local_dir="harmonized_global_crops")
```

### Sentinel-2 Download Pipeline
Sentinel-2 donwload pipeline can be found in [Ai2 rslearn_projects](https://github.com/allenai/rslearn_projects/tree/master/one_off_projects/crop_type).


### Data Split
Follow the files in `train-test-splits/` to split the dataset into training and testing sets. For demo, you can run the following command to create train/test data for a CDL OOD experiment:
```sh
python3 train-test-splits/create_splits.py
```


### Training
Run the training script for CDL with SSL4EO-S12 pre-trained weights:
```sh
python3 -m torchgeo fit --config experiments/fewshot/cdl_100_ood_ssl4eo.yaml --seed_everything 0
```

### Testing
After completing training, you can use the checkpoints to test on the data.
```sh
python3 -m torchgeo test --config experiments/fewshot/cdl_100_ood_ssl4eo.yaml --seed_everything 0 --data.sentinel2_paths ./harmonized_global_crops/sentinel2_subsample_test --ckpt_path=...
```

### Reference
If you find this code useful, please cite the following paper:
```
@misc{chang2025generalizabilityfoundationmodelscrop,
      title={On the Generalizability of Foundation Models for Crop Type Mapping},
      author={Yi-Chia Chang and Adam J. Stewart and Favyen Bastani and Piper Wolters and Shreya Kannan and George R. Huber and Jingtong Wang and Arindam Banerjee},
      year={2025},
      eprint={2409.09451},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2409.09451},
}
```