import numpy as np


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
