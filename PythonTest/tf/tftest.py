import unittest
import sys
import numpy as np
import tensorflow as tf
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
    def test_gpu(self): 
        import tensorflow as tf
        with tf.device("/gpu:0"):
            a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
            b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
        c = tf.matmul(a, b)
        config = tf.ConfigProto(log_device_placement=True)
        sess = tf.Session(config=config)
        print(sess.run(c))
        print('----done')
       
            
       
        


