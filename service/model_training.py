import pandas as pd
import numpy as np
import tensorflow as tf
from service import data_pre

analyze_time_length = data_pre.analyze_time_length
train_analyze_time_length = 100
analyze_interval = data_pre.analyze_interval
half_analyze_interval = data_pre.half_analyze_interval
static_variety = data_pre.static_variety
model_path = "./sjsr_model"


def model(data, txt_win, label):
    try:
        tf.reset_default_graph()
        Xtr = tf.placeholder("float", [1, analyze_interval + static_variety], name="Xtr")
        Ytr = tf.placeholder("float", [1, 1], name="Ytr")

        Q = tf.Variable(tf.random_normal([analyze_interval + static_variety, 1]), name="Q")
        b = tf.Variable(np.random.randn())

        ss = tf.add(tf.matmul(Xtr, Q), b, name="ss")
        pred = tf.sigmoid(ss, name="pred")

        cost = tf.pow(pred - Ytr, 2)

        optimizer = tf.train.GradientDescentOptimizer(0.01).minimize(cost)

        init = tf.global_variables_initializer()

        saver = tf.train.Saver()

        txt_win.result_txt.append("Star to train model......")

        with tf.Session() as sess:
            sess.run(init)

            for i in range(half_analyze_interval, analyze_time_length - half_analyze_interval):
                _, c, model_pred = sess.run([optimizer, cost, pred], feed_dict={Xtr: [
                    [data[0][i - 2], data[0][i - 1], data[0][i], data[0][i + 1], data[0][i + 2], data[1][i], data[2][i], data[3][i], data[4][i],
                     data[5][i]]], Ytr: [[label[i]]]})
                log = "At step" + str(i) + "   model_pred:" + str(model_pred[0][0]) + "  real_label:" + str(label[i])
                txt_win.result_txt.append(log)

            save_path = saver.save(sess, model_path)
            txt_win.result_txt.append("Model saved in file: %s" % save_path)
    except Exception as e:
        txt_win.result_txt.append('error: %s' % e)


def model_jugde(data, txt_win, label=None, model_path=model_path):
    try:
        with tf.Session() as sess:
            saver = tf.train.import_meta_graph(model_path+'.meta')
            saver.restore(sess, tf.train.latest_checkpoint('./'))

            txt_win.result_txt.append("Model restored from file: %s" % model_path)

            graph = tf.get_default_graph()
            Xtr = graph.get_tensor_by_name("Xtr:0")

            pred = graph.get_tensor_by_name("pred:0")

            for i in range(half_analyze_interval, analyze_time_length - half_analyze_interval):

                model_pred = sess.run(pred, feed_dict={Xtr: [
                    [data[0][i - 2], data[0][i - 1], data[0][i], data[0][i + 1], data[0][i + 2], data[1][i], data[2][i],
                     data[3][i], data[4][i],
                     data[5][i]]]})
                if i % 10 == 0:
                    log = "For preople id" + str(i) + "   model_pred:" + str(model_pred[0][0])
                    txt_win.result_txt.append(log)

    except Exception as e:
        txt_win.result_txt.append('error: %s' % e)

# model(data_pre.deal_data("wrist.csv",cut=True), data_pre.deal_label("wrist.csv"))
# model_jugde(data_pre.deal_data("wrist.csv",cut=True), label = data_pre.deal_label("wrist.csv") )
