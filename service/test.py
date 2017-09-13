import pandas as pd
import numpy as np
import tensorflow as tf


class TestClass(object):
    def __init__(self, test_path):
        self.test_path = test_path

    def read_test(self):
        return pd.read_csv(self.test_path)

    def test_net(self):
        s = tf.placeholder("float", [1, 2])
        b = np.zeros(10)




