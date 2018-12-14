#!/bin/bash

# activate anaconda tensorflow gpu
source /scratch/dcosta2/anaconda3/etc/profile.d/conda.sh
conda activate tf_gpu

# run the test
python test_tensorflow.py

