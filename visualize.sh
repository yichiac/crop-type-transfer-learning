#!/usr/bin/env python3

python3 visualize.py data/sentinel2_subsample_100/sentinel2_agrifieldnet_2021_subsampled data/agrifieldnet_harmonized data/benchmark_new_test/36z91e5k/checkpoints/epoch=99-step=700.ckpt agrifieldnet
python3 visualize.py data/sentinel2_subsample_100/sentinel2_cdl_2023_subsampled data/cdl_harmonized_block data/benchmark_new_test/mmnyvm68/checkpoints/epoch=99-step=700.ckpt cdl
python3 visualize.py data/sentinel2_subsample_100/sentinel2_eurocrops_subsampled data/eurocrops_cropped_subsampled data/benchmark_new_test/3f914jov/checkpoints/epoch=99-step=700.ckpt eurocrops
python3 visualize.py data/sentinel2_subsample_100/sentinel2_nccm_2019_subsampled data/nccm_harmonized_block data/benchmark_new_test/3f914jov/checkpoints/epoch=99-step=700.ckpt nccm
python3 visualize.py data/sentinel2_subsample_100/sentinel2_sact_2017_subsampled data/sact_harmonized data/benchmark_new_test/21zll6uu/checkpoints/epoch=99-step=700.ckpt sact
python3 visualize.py data/sentinel2_subsample_100/sentinel2_sas_2021_subsampled data/sas_harmonized data/benchmark_new_test/gssgj5g1/checkpoints/epoch=99-step=700.ckpt sas
