import unittest
import sys
import time
import numpy as np
import tensorflow as tf
import logging
from datetime import datetime

#https://www.tensorflow.org/install/install_windows
#https://www.tensorflow.org/tutorials/using_gpu
#https://nitishmutha.github.io/tensorflow/2017/01/22/TensorFlow-with-gpu-for-windows.html
#https://learningtensorflow.com/lesson10/
#http://www.heatonresearch.com/2017/01/01/tensorflow-windows-gpu.html


class TFTest(unittest.TestCase):
    def test_hellotf(self): 
        hello = tf.constant('Hello, TensorFlow!')
        sess = tf.Session()
        print(sess.run(hello))
    
    

    #problem encountered, cpu version is always used, not gpu one
    #do not follow the tensorflow install tutorial, pip3 install --upgrade tensorflow-gpu
    #use this instead pip install --upgrade https://storage.googleapis.com/tensorflow/windows/gpu/tensorflow_gpu-0.12.1-cp35-cp35m-win_amd64.whl
    #find the latest here https://pypi.python.org/pypi/tensorflow
    def test_gpu(self): 
        with tf.device("/gpu:0"):
            a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
            b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
        c = tf.matmul(a, b)
        config = tf.ConfigProto(log_device_placement=True)
        sess = tf.Session(config=config)
        print(sess.run(c))
        print('----done')

   


    def condition(self, i):
        return  tf.less(i, 10)
    
    def mybody(self, i):
        #tf.add(i, 1)
        return i + 1 

    #https://stackoverflow.com/questions/43792961/understanding-the-while-loop-in-tensorflow
    def test_gpu_while(self):
        with tf.device("/gpu:0"):
            i = tf.constant(0)
            c = self.condition
            b = self.mybody
            #c = lambda i: tf.less(i, 10)
            #b = lambda i: tf.add(i, 1)
        
            
        r = tf.while_loop(cond = c, body =  b, loop_vars = [i])
        config = tf.ConfigProto(log_device_placement=True)
        sess = tf.Session(config=config)
        print(sess.run(r))


    def gpu_cpu_compare(self, device_name, shape):
        with tf.device(device_name):
            random_matrix = tf.random_uniform(shape=shape, minval=0, maxval=1)
            dot_operation = tf.matmul(random_matrix, tf.transpose(random_matrix))
            sum_operation = tf.reduce_sum(dot_operation)
        
        start = time.time()

        with tf.Session(config=tf.ConfigProto(log_device_placement=True)) as session:
            result = session.run(sum_operation)
            print(result)

        # It can be hard to see the results on the terminal with lots of output -- add some newlines to improve readability.
        print("\n" * 5)
        print("Shape:", shape, "Device:", device_name)
        print("Time taken:", time.time() - start)
        print("\n" * 5)

       
    def test_gpu_cpu_compare(self):
        try:
            self.gpu_cpu_compare("/gpu:0",(8000,8000))
        except Exception as e:
            self.logger.error(e)
        try:     
            self.gpu_cpu_compare("/cpu:0",(8000,8000))
        except Exception as e:
            self.logger.error(e)
        
        
        print('----------------------------')

       
        


