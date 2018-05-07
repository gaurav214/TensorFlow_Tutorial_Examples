'''
Introductory example using TensorFlow library.
Author: Gaurav Negi
'''

#importing tensorflow (to install type in terminal: pip install tensorflow)

import tensorflow as tf

#Creating variable with constant values a = 4 and b = 5
a = tf.constant(4)
b = tf.constant(5)

c = a * b

#start tf session
sess = tf.Session()

#run session
print(sess.run(c))
