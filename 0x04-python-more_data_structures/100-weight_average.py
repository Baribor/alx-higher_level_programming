#!/usr/bin/python3

def weight_average(my_list=list):
    if not my_list or len(my_list) == 0:
        return 0

    weighted_sum = 0
    average = 0

    for w in my_list:
        a, b = w
        weighted_sum += a * b
        average += b
    return weighted_sum / average


if __name__ == "__main__":
    my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
    # = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
    result = weight_average(my_list)
    print("Average: {:0.2f}".format(result))
