def is_leap(year):
    """Returns True if the year is a leap year and returns False if it is not"""
    leap = False

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    return leap


year = int(input())


"""Prints a string of all numbers below n e.g 12345 """
if __name__ == '__main__':
    n = int(input())
    for num in range(1, n + 1):
        print(num, end='')

"""List comprehension"""
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print(list([i, j, k] for i in range(x+1) for j in range(y+1)
               for k in range(z+1) if i+j+k != n))


def oddNumbers(l, r):
    # Write your code here
    for numb in range(l, r+1):
        if numb % 2 != 0:
            print(numb, end=" ")
