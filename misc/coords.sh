#!/usr/bin/env bash

#SBATCH --time=12:00:00
#SBATCH --mem=128G
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

python3 get_coordinates.py
