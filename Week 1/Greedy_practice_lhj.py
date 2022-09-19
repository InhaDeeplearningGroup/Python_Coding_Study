import numpy as np
import sys


def practice1():
    n = map(int, input().split())
    data = list(map(int, input().split()))

    count = 0
    index = 0
    data.sort()
    print(data)

    while index <= len(data):
        index += index + data[index]
        if index > len(data):
            break
        else:
            count += 1

    print(count)


def practice3():
    data = list(map(str, input()))
    count = 0

    for i in range(len(data) - 1):
        if data[i] != data[i + 1]:
            count += 1

    print((count + 1) // 2)


if __name__ == '__main__':
    practice3()
