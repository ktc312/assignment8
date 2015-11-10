__author__ = 'ktc312'

from positions import *
from trial import *

budget = 1000
odds = 0.51
result_output = 'results.txt'

def main():
    position_list = get_position_list()
    num_trails = get_num_trails()
    trial(position_list, num_trails, budget, odds, result_output)

