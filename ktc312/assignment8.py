__author__ = 'ktc312'

from positions import *
from trials import *

budget = 1000
odds = 0.51
result_output = 'results.txt'

def main():
    position_list = get_position_list()
    num_trails = get_num_trials()
    trial(position_list, num_trails, budget, odds, result_output)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print 'Keyboard Interrupt'


