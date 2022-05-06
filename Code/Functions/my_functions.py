
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



# In[3]:
def fn_plot_res(y,x):
    res =  y - x
    Zeros = y * 0
    plt.figure(figsize=(15, 5))
    ax = plt.axes()
    ax.scatter(x,res)
    ax.plot(x, Zeros,color = 'red')
    ax.set_xlim(min(x),max(x))
    ax.set_ylim(-1*max(res),1.1*max(res))
    plt.xlabel('Fitted Values')
    plt.ylabel('Residuals')    
    
def fn_bias_rmse(y,yhat):
    """
    theta0 - true parameter value
    thetatahat - estimated parameter value
    se_thetahat - estiamted se of thetahat
    """
    n = len(yhat)
    res =  y - yhat
    bias = np.mean(res)
    rmse = np.sqrt(np.mean(res**2))
    return (bias,rmse)  