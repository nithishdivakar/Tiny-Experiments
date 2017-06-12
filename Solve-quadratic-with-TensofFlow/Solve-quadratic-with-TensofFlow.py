import tensorflow as tf

a = tf.placeholder(tf.float32,[])        # constant
x = tf.Variable([0.0],tf.float32)        # variable
f = tf.square(x-a)                       # f= (x-a)^2
minimize_op = tf.train.GradientDescentOptimizer(0.1).minimize(f)  # min f

with tf.Session() as sess:
  init = tf.global_variables_initializer()
  sess.run(init)
  for step in range(100+1):                           # loop
    _ = sess.run(minimize_op, feed_dict={a:20.0})     # run the min op
    if step % 10 == 0:
      f_val, x_val = sess.run([f,x], feed_dict={a : 20.0})
      print ("step : {:3d} f = {:e} x = {:4.2f}".format(step,f_val[0],x_val[0]))
