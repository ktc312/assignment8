__author__ = 'ktc312'
import sys

def get_position_list():
    position_list = list()

    try:
        response = raw_input(
            'Input a list of the number of shares to buy in parallel: e.g. 1,10,100,1000 \n'
        )
    except:
        sys.exit()

    if response == "quit":
        sys.exit()

    try:
        response_split = response.split(',')
        for item in response_split:
            position_list.append(int(item))
    except:
        print 'invaild input'
        return get_position_list()
    return position_list


def get_num_trails():
    pass

