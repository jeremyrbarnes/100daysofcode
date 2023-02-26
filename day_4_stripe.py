'''
This problem was asked by Stripe.

Given an array of integers,
find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer
that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2.
The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''
from typing import Optional
import numpy as np


def find_first_missing_int(arr) -> Optional[int]:
    last_i = min(arr)
    if last_i > 0:
        last_i = 0

    for i in arr:
        if i - last_i > 1:
            return last_i + 1
        last_i = i
    return None


arr = np.random.randint(-100, high=100, size=25)
arr.sort()
print(arr)
print(find_first_missing_int(arr))
