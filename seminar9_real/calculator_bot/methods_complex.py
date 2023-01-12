# num_one[0] = a
# num_one[1] = b
# num_two[0] = c
# num_two[1] = d
import math

def sum(num_one: list, num_two: list):
    return [num_one[0] + num_two[0], num_one[1] + num_two[1]]


def substraction(num_one: list, num_two: list):
    return [num_one[0] - num_two[0], num_one[1] - num_two[1]]


def multiplication(num_one: list, num_two: list):
    return [num_one[0] * num_two[0] - num_one[1] * num_two[1], num_one[0] * num_two[1] + num_one[1] * num_two[0]]


def division(num_one: list, num_two: list):
    return [(num_one[0] * num_two[0] + num_one[1] * num_two[1]) / (num_two[0] * num_two[0] + num_two[1] * num_two[1]),
            (num_one[1] * num_two[0] - num_one[0] * num_two[1]) / (num_two[0] * num_two[0] + num_two[1] * num_two[1])]


def power(num_one: list, num_two):
    module = round(math.sqrt(num_one[0] * num_one[0] + num_one[1] * num_one[1]), 3)
    if num_one[0] > 0:
        fi = math.atan2(num_one[1], num_one[0])
    else:
        if num_one[1] > 0:
            fi = math.atan2(num_one[1], num_one[0]) + math.pi
        else:
            fi = math.atan2(num_one[1], num_one[0]) - math.pi
    return [round(pow(module, num_two) * math.cos(num_two * fi), 3),
            round(pow(module, num_two) * math.sin(num_two * fi), 3)]


if __name__ == "__main__":
    print(power([1, math.sqrt(3)], 3))