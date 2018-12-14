### INSTALLATION INSTRUCTIONS 

```shell
# make scratch directory if it doesn't exist
mkdir -p /scratch/dcosta2 

# Download the latest version for linux 64bit(x86) 
# from https://www.anaconda.com/download/#linux
wget https://repo.anaconda.com/archive/Anaconda3-5.3.1-Linux-x86_64.sh
# install it into /scratch/dcosta2
sh Anaconda3-5.3.1-Linux-x86_64.sh
rm Anaconda3-5.3.1-Linux-x86_64.sh

source /scratch/dcosta2/anaconda3/etc/profile.d/conda.sh

# create the tf_gpu environemnt with a gpu enabled tensorflow
conda create --name tf_gpu tensorflow-gpu
```

### USAGE INSTRUCTIONS 
To use anaconda we run the following commands

```shell
source /scratch/dcosta2/anaconda3/etc/profile.d/conda.sh
conda activate tf_gpu
```

