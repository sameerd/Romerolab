
### Testing Tensorflow on the cpu vs gpu

Run [test_tensorfow.py](test_tensorflow.py) on a compute node with a gpu.
This script needs [Anaconda to be installed first](../../notes/ANACONDA.md)

```shell
# submit job
condor_submit test_tensorflow.sub

# monitor job
condor_q

# output 
cat logs/test_tensorflow.out
```


