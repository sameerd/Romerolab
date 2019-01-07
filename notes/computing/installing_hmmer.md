### Hmmer3 installation instructions

These instructions install Hmmer on the biochem cluster. 

```shell

# Download the latest version for linux 64bit(x86) 
wget http://eddylab.org/software/hmmer/hmmer-3.2.tar.gz
tar zxf hmmer-3.2.tar.gz 
cd hmmer-3.2
./configure --prefix=/scratch/dcosta2/software
make
make install
```


