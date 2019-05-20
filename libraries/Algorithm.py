import numpy as np
from sklearn.linear_model import RANSACRegressor, LinearRegression

def kalman_filter(data_list, Q=200, R=400, x0=200, p0=1):
    data_list = [float(data_list[i]) for i in range(len(data_list))]
    try:
        N = len(data_list)
        K, X, P = list(range(N)), list(range(N)), list(range(N))
        X[0] = x0
        P[0] = p0
        for i in range(1, N):
            K[i] = P[i-1] / (P[i-1]+R)
            X[i] = X[i-1] + K[i]*(data_list[i]-X[i-1])
            P[i] = P[i-1] - K[i]*P[i-1]+Q
    except:
        X = None
    finally:
        return X


def average_filter(data_list, N=11):
    data_list = [float(data_list[i]) for i in range(len(data_list))]
    try:
        data = [np.mean(sorted(data_list[max(0, int(n-N/2)) : min(len(data_list)-1, int(n+N/2))])[1:-1]) for n in range(len(data_list))]
    except:
        data = None
    finally:
        return data
