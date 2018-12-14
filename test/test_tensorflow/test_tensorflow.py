# Testing tensorflow on GPU vs CPU

# https://stackoverflow.com/questions/41804380/testing-gpu-with-tensorflow-matrix-multiplication

import os
import sys
#os.environ["CUDA_VISIBLE_DEVICES"]="1"
import tensorflow as tf
import time

n = 8192
dtype = tf.float32

# Run matrix multiplication on the GPU
with tf.device("/gpu:0"):
    matrix1g = tf.Variable(tf.ones((n, n), dtype=dtype))
    matrix2g = tf.Variable(tf.ones((n, n), dtype=dtype))
    productg = tf.matmul(matrix1g, matrix2g)

# Run matrix multiplication on the CPU
with tf.device("/CPU:0"):
    matrixc1 = tf.Variable(tf.ones((n, n), dtype=dtype))
    matrixc2 = tf.Variable(tf.ones((n, n), dtype=dtype))
    productc = tf.matmul(matrixc1, matrixc2)


# avoid optimizing away redundant nodes
config = tf.ConfigProto(graph_options=tf.GraphOptions(
	optimizer_options=tf.OptimizerOptions(opt_level=tf.OptimizerOptions.L0)))
sess = tf.Session(config=config)

sess.run(tf.global_variables_initializer())
iters = 10

# pre-warming
sess.run(productg.op)

start = time.time()
for i in range(iters):
  sess.run(productg.op)

end_time = time.time()
ops = n**3 + (n-1)*n**2 # n^2*(n-1) additions, n^3 multiplications
elapsed = (end_time - start)
rate = iters*ops/elapsed/10**9
print('\n %d x %d GPU matmul took: %.2f sec, %.2f G ops/sec' % (n, n,
                                                            elapsed/iters,
                                                            rate,))
# pre-warming
sess.run(productc.op)

start = time.time()
for i in range(iters):
  sess.run(productc.op)

end_time = time.time()
ops = n**3 + (n-1)*n**2 # n^2*(n-1) additions, n^3 multiplications
elapsed = (end_time - start)
rate = iters*ops/elapsed/10**9
print('\n %d x %d CPU matmul took: %.2f sec, %.2f G ops/sec' % (n, n,
                                                            elapsed/iters,
                                                            rate,))

