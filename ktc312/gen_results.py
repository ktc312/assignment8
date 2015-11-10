__author__ = 'ktc312'
import numpy as np
import matplotlib.pyplot as plt

def GenResults(result_output,position,daily_ret):
    with open(result_output,'a')as output:
        output.write('Number of Positions:  {0}  Mean:  {1}  Std. Dev.:  {2} \n'.format(position,np.mean(daily_ret),np.std(daily_ret)))

def PlotHist(position,daily_ret):
    plt.hist(daily_ret, 100, range = [-1,1])
    plt.xlim(-1, 1)
    plt.savefig('histogram_{0}_pos.pdf'.format(str(position).zfill(4)))
    plt.clf()
