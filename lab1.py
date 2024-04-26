import math

def add(x, y):
    return x + y
def multiply(x, y):
    return x * y

def subtract(x, y):
    return x - y

def my_map(func, *args):
    print("Function:", func.__name__)
    print("Arguments:", args)
    return [func(*arg_pair) for arg_pair in zip(*args)]


result = my_map(add, [1, 2, 3], [4, 5, 6])
print(result)  # Output: [5, 7, 9]

def calc_distance(point1, point2):
    distx = point2[0] - point1[0]
    disty = point2[1] - point1[1]
    distz = point2[2] - point1[2]
    return math.sqrt(distx**2 + disty**2 + distz**2)


distance = calc_distance([4, 0, 10], [1, 1, 1])
print(distance)  # Output: 9.539392014169456
