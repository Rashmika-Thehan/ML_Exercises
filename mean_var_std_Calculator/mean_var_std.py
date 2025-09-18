import pandas as pd
import numpy as np

def calculate(input_list):
    arr = np.array(input_list).reshape(3,3)
    mean_axis1, mean_axis2, mean_flatten = arr.mean(axis =0), arr.mean(axis=1), arr.flatten().mean()
    var_axis1, var_axis2, var_flatten = arr.var(axis =0), arr.var(axis=1), arr.flatten().var()
    std_axis1, std_axis2, std_flatten = arr.std(axis =0), arr.std(axis=1), arr.flatten().std()
    max_axis1, max_axis2, max_flatten = arr.max(axis =0), arr.max(axis=1), arr.flatten().max()
    min_axis1, min_axis2, min_flatten = arr.min(axis =0), arr.min(axis=1), arr.flatten().min()
    sum_axis1, sum_axis2, sum_flatten = arr.sum(axis =0), arr.sum(axis=1), arr.flatten().sum()
    
    output_dict = {'mean':[mean_axis1.tolist(), mean_axis2.tolist(), float(mean_flatten)],
                   'varience':[var_axis1.tolist(), var_axis2.tolist(), float(var_flatten)],
                   'standerd deviation':[std_axis1.tolist(), std_axis2.tolist(), float(std_flatten)],
                   'max':[max_axis1.tolist(), max_axis2.tolist(), float(max_flatten)],
                   'min':[min_axis1.tolist(), min_axis2.tolist(), float(min_flatten)],
                   'sum':[sum_axis1.tolist(), sum_axis2.tolist(), float(sum_flatten)]}
    
    return output_dict
    
