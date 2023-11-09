#!/usr/bin/env bash

#SBATCH --time=12:00:00
#SBATCH --mem=32G
#SBATCH --job-name=china
#SBATCH --partition=dali
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=32
#SBATCH --mail-type=END
#SBATCH --mail-user=yichia3@illinois.edu
#SBATCH --mail-type=FAIL
#SBATCH --output=%x-%j.out

. /projects/dali/spack/share/spack/setup-env.sh
spack env activate dali

python3 download_china.py \
    --save-path ./data \
    --collection COPERNICUS/S2 \
    --meta-cloud-name CLOUDY_PIXEL_PERCENTAGE \
    --cloud-pct 20 \
    --dates 2019-04-01 2019-04-11 2019-04-21 2019-04-30 2019-05\
    --radius 1320 \
    --bands B1 B2 B3 B4 B5 B6 B7 B8 B8A B9 B10 B11 B12 \
    --dtype uint16 \
    --num-workers 8 \
    --log-freq 100 \
    --match-file fist_100_centroids.csv \
    --indices-range 0 150
