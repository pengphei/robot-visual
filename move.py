
import matplotlib.pyplot as plt


def dist_by_speed(v, t):
    """get distance by speed"""
    return v*t

def dist_by_accel(v, a, t):
    """get distance by speed, accel, and time"""
    return v*t + a*t*t/2

def speed_by_acccel(vs, a, t):
    """ get speed by accel"""
    return vs + a*t

def matrix_speed_time_calc(distance, vs, ve, vmax, saccel, daccel):
    "get time speed matrix"
    ts = (vmax-vs)/saccel
    te = (vmax-ve)/daccel
    tm = (distance - dist_by_accel(vs, saccel, ts) - dist_by_accel(vmax, -daccel, te))/vmax


    return [[0, ts, ts+tm, ts+te+tm], [vs, vmax, vmax, ve]]

def matrix_speed_distance_calc(distance, vs, ve, vmax, saccel, daccel):
    "get time speed matrix"
    ts = (vmax-vs)/saccel
    te = (vmax-ve)/daccel
    tm = (distance - dist_by_accel(vs, saccel, ts) - dist_by_accel(vmax, -daccel, te))/vmax


    return [[0, ts, ts+tm, ts+te+tm], [vs, vmax, vmax, ve]]

def matrix_distance_time_calc(distance, vs, ve, vmax, saccel, daccel):
    "get time speed matrix"
    ts = (vmax-vs)/saccel
    te = (vmax-ve)/daccel
    tm = (distance - dist_by_accel(vs, saccel, ts) - dist_by_accel(ve, daccel, te))/vmax


    return [[0, ts, ts+tm, ts+te+tm], [vs, vmax, vmax, ve]]


def matplot_speed_time(distance, vs, ve, vmax, saccel, daccel):
    m = matrix_speed_time_calc(distance, vs, ve, vmax, saccel, daccel)
    plt.plot(m[0], m[1])
    plt.title('Speed & Time')

    for x in range(len(m[0])):
        tag = "({},{})".format(m[0][x], m[1][x])
        plt.text(m[0][x], m[1][x]+1, tag)
    
    plt.ylabel(u'Speed',fontproperties='SimHei')
    plt.xlabel(u'Time',fontproperties='SimHei')
    plt.grid(True)
    plt.show()



# matplot_speed_time(1000, 100, 100, 200, 1000, 1000)

