#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    j = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            j.append(True)
        else:
            j.append(False)
    return j
