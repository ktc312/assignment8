__author__ = 'ktc312'
import numpy as np

class Simulation(object):

    def __init__(self, budget, odds, position):
        self.position = position
        self.position_value = budget/position
        self.odds = odds

    def run(self):
        returns = 0
        rands = np.random.random_sample(self.position)

        for i in range(0, self.position):
            if rands[i] >= self.odds:
                returns += 2*self.position_value
        return returns

def trial(position_list, num_trails, budget, odds, result_output):
    open(result_output,'w').close()

    for position in position_list:
        invest_simulate = Simulation(budget,odds,position)
        cumu_ret  = np.zeros(num_trails)
        daily_ret = np.zeros(num_trails)

        for times in range(0, num_trails):
            cumu_ret[times] = invest_simulate.run()
            daily_ret[times] = (cumu_ret[times] / budget) - 1
    pass
