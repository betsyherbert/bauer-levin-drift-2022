
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


def matrix_drift(u, drift_tau=10, drift_alpha=0.01):
    # smaller alpha = less drift
    # return u * np.sqrt(1-drift_alpha) + np.random.randn() * np.sqrt(drift_alpha)

    a = 1
    b = 0
    return u * a + np.random.randn() * b

def nonlinearity(x):
    return np.tanh(x)

def get_input(N, theta):

    s_y = np.linspace(-90, 90, N)  # center of tuning curves (i.e. most responsive stimulus)

    # define tuning curves: normal distributions

    d = np.abs(theta - s_y)    # distance to input theta
    sigma = 10  #* 2*np.pi     # response width
    amp = 80                   # response amplitude

    y = amp * np.exp(-(d**2)/(2*sigma**2))

    return y




