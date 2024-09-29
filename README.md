# On the Generalizability of Foundation Models for Crop Type Mapping

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yichiac/crop-type-transfer-learning.git
    cd crop-type-transfer-learning/torchgeo
    ```

2. Create a virtual environment and activate it:
    ```sh
    conda create -n croptype python=3.10
    conda activate croptype
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Download dataset
The dataset is available on the [HuggingFace](https://huggingface.co/datasets/torchgeo/harmonized_global_crops).
```sh
git clone https://huggingface.co/datasets/torchgeo/harmonized_global_crops
```

### Data split
Follow the files in `train-test-splits\` to split the data into training and testing sets.

### Training
Run the training script for CDL with SSL4EO-S12 pre-trained weights:
```sh
python3 -m torchgeo fit --config experiments/sentinel2_cdl_resnet50_ssl4eo_frozen.yaml
```

### Testing
1. Change `cdl_paths` to the path to test files
2. Run the testing script:
```sh
python3 -m torchgeo test --config experiments/sentinel2_cdl_resnet50_ssl4eo_frozen.yaml --ckpt_path=...
```