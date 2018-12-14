
### Testing Tensorflow on the cpu vs gpu

Run [test\_tensorflow.py](test_tensorflow.py) on a compute node with a gpu.
This script first needs [Anaconda and the tf\_gpu environment installed](../../notes/ANACONDA.md).

```shell
# submit job
condor_submit test_tensorflow.sub

# monitor job
condor_q

# output 
cat logs/test_tensorflow.out
```
<pre>

 8192 x 8192 GPU matmul took: 0.41 sec, 2655.55 G ops/sec

 8192 x 8192 CPU matmul took: 250.17 sec, 4.39 G ops/sec

</pre>

The results are dependent on how busy the compute nodes are. A speed up of
around 100x seems normal. 

