import numpy as np

'''
    This problem was asked by Uber.

    Given an array of integers,
    return a new array such that each element at index i of the new array
    is the product of all the numbers in the
    original array except the one at i.

    For example, if our input was [1, 2, 3, 4, 5],
    the expected output would be [120, 60, 40, 30, 24].
    If our input was [3, 2, 1], the expected output would be [2, 3, 6].
'''


def get_product_with_divison(arr, index):
    product = 1
    for i in arr:
        product = product * i
    return product / arr[index]


def get_product_without_divison(arr, index):
    product = 1
    for idx, x in enumerate(arr):
        if idx != index:
            product = product * x
    return product


arr = np.random.randint(1, high=10, size=5)
index = 3

print(arr)

# with division
product = get_product_with_divison(arr, index)
print("With Division: " + str(product))

# without division
product = get_product_without_divison(arr, index)
print("Without Division: " + str(product))
