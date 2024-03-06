#!/usr/bin/python3
"""Making Change Problem"""


def makeChange(coins, total):
    """Making Changes"""
    if total <= 0:
        return 0
<<<<<<< HEAD
    check = 0
    temp = 0
    coins.sort(reverse=True)
    for i in coins:
        while check < total:
            check += i
            temp += 1
        if check == total:
            return temp
        check -= i
        temp -= 1
    return -1
=======
    elif total > 0:
        newList = sorted(coins[:])
        newList = list(reversed(newList))
        count = 0
        value = total + 0
        index = 0
        while value >= 0 and (index < len(newList)):
            if value >= newList[index]:
                value = value - newList[index]
                count += 1
            elif value < newList[index]:
                index += 1
        if index == len(newList):
            if value != 0:
                return -1
            elif value == 0:
                return count
>>>>>>> 2b404ccac7c9730aacb28b2021fe6548171359d5
