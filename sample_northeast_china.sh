#!/usr/bin/env bash

#SBATCH --time=48:00:00
#SBATCH --mem=16G
#SBATCH --job-name=china_sample_100k
#SBATCH --partition=dali
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#SBATCH --mail-type=END
#SBATCH --mail-user=yichia3@illinois.edu
#SBATCH --mail-type=FAIL
#SBATCH --output=%x-%j.out

. /projects/dali/spack/share/spack/setup-env.sh
spack env activate dali

python3 sample_northeast_china.py
