def is_leap(year):
    """Returns True if the year is a leap year and returns False if it is not"""
    leap = False
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else: return True
    else: return False
    return leap

year = int(input())
