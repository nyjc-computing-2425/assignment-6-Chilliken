from datetime import datetime
import time

# Part 1
def clock(n):
    """
    n is the number of time the clock moves
    """
    # Your code here
    number = 0
    while number <n:
        now = datetime.now()
        time_now_in_hms = datetime.strftime(now,"%H:%M:%S")
        print(time_now_in_hms,end="\r")
        time.sleep(1)
        number +=1



# Part 2
def lcm(a, b):
    """
    finding the least common multiple of a and b

    Parameters
    ---------
    a: int
        first number

    b: int
        second number

    Returns
    -------
    int   
        least common multiple of a and b
    
    """
    # Your code here
    a_original = a
    b_original = b
    while a != b:
        if a < b:
            a = a + a_original
        if a > b:
            b = b + b_original
    return a
    
                
# Part 3
def gcf(a, b):
    """
    finding the greatest common factor of a and b

    Parameters
    ---------
    a: int
        first number

    b: int
        second number

    Returns
    -------
    int   
        greatest common factor of a and b

    """
    # Your code here
    
    while a!= 1:
        if a == 0:
            return b
        if b == 0:
            return a
        if a == b:
            return a
        if a > b:
            a = a - b
        if b > a:
            b = b - a
    return a
