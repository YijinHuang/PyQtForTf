import pandas as pd
import numpy as np

judge_name = "judge"
analyze_time_length = 100
analyze_interval = 5
half_analyze_interval = analyze_interval//2
static_variety = 5

#use to get data
def read_data(path):
    return pd.read_csv(path)

def cut_data(data,name,cut=False,axis=1):
    if cut : return data.drop("time", axis = axis).drop(name, axis = axis).tail(analyze_time_length).values
    else:return data.drop("time", axis = axis).tail(analyze_time_length).values



def deal_data(path, cut = False):
    data = read_data(path)
    data = cut_data(data, judge_name, cut = cut)
    data_var = np.zeros(analyze_time_length)  # 方差
    data_var_diff = np.zeros(analyze_time_length)  # 方差差
    data_sum_log = np.zeros(analyze_time_length)  # 和
    data_mean = np.zeros(analyze_time_length)  # 均值
    data_mean_diff = np.zeros(analyze_time_length)  # 均值差
    for i in range(half_analyze_interval, analyze_time_length - half_analyze_interval):
        data_var[i] = np.var(data[i - half_analyze_interval:i + half_analyze_interval + 1])
        data_var_diff[i] = data_var[i - 1] - data_var[i]
        data_sum_log[i] = np.log(0.01 + np.sum(data[i - half_analyze_interval:i + half_analyze_interval + 1]))
        data_mean[i] = np.mean(data[i - half_analyze_interval:i + half_analyze_interval + 1])
        data_mean_diff[i] = data_mean[i - 1] - data_mean[i]

    return (data, data_var, data_var_diff, data_sum_log, data_mean, data_mean_diff)


def deal_label(path, label_name = judge_name):
    data = read_data(path)
    return data[label_name].tail(analyze_time_length).values

def get_ship(data):
    pass



   # new_wrist = pd.DataFrame(
   #     {'move': data, 'var': data_var, 'var_diff': data_var_diff, 'sum': data_sum_log, 'mean': data_mean, 'mean_diff': data_mean_diff})
   # new_wrist.to_csv("new_wrist.csv")





