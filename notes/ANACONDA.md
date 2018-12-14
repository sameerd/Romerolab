### Anaconda installation instructions

These instructions set up Anaconda and a tensorflow gpu environment on the
biochem cluster. 

```shell
# make scratch directory if it doesn't exist
mkdir -p /scratch/dcosta2 

# Download the latest version for linux 64bit(x86) 
# from https://www.anaconda.com/download/#linux
wget https://repo.anaconda.com/archive/Anaconda3-5.3.1-Linux-x86_64.sh

# install it into /scratch/dcosta2/anaconda3
sh Anaconda3-5.3.1-Linux-x86_64.sh
# when complete remove the installation file
rm Anaconda3-5.3.1-Linux-x86_64.sh
```

### tensorflow gpu environement

Create the tensorflow gpu version. (Instructions copied from
[here](https://towardsdatascience.com/tensorflow-gpu-installation-made-easy-use-conda-instead-of-pip-52e5249374bc) )

```shell
source /scratch/dcosta2/anaconda3/etc/profile.d/conda.sh

# create the tf_gpu environemnt with a gpu enabled tensorflow
conda create --name tf_gpu tensorflow-gpu
```

### USAGE INSTRUCTIONS 
To use `anaconda` and the `tf\_gpu` environment we run the following commands

```shell
source /scratch/dcosta2/anaconda3/etc/profile.d/conda.sh
conda activate tf_gpu
```

