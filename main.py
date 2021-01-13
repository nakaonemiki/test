import numpy as np

# 照射条件生成に必要なパラメータ
start_x, end_x, step_x = -16e-3, 16.0e-3, 2.0e-3
start_y, end_y, step_y = 0.0, 6.0e-3, 5.0e-3
start_p, end_p, step_p = 400, 4000, 720

def creat_laserpathfile(x_conf):
    for x in x_conf:

if __name__ == '__main__':
    x_conf = np.arange(start_x, end_x + 1.0e-3, step_x)
    creat_laserpathfile(x_conf)
    #print(x_conf)
