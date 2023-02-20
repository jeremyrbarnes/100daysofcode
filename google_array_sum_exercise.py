import numpy as np

'''
    This problem was recently asked by Google.
    Given a list of numbers and a number k,
    return whether any two numbers from the list add up to k.
    For example, given [10, 15, 3, 7] and k of 17,
    return true since 10 + 7 is 17.
'''


def check_for_sum(arr, k):
    sub_arr = []
    for i in arr:
        if i <= k:
            for j in sub_arr:
                if j + i == k:
                    return True

            sub_arr.append(i)

    return False


arr = np.random.randint(0, high=200, size=100)
k = 11
print(check_for_sum(arr, k))
