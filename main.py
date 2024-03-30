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
        print(datetime.strftime(datetime.now(),"%H:%M:%S"),end="\r")
        time.sleep(1)
        number +=1
    pass


# Part 2
def lcm(a, b):
    """
    dividing the product of a and b with the greatest common factor found in gcf(a,b)
    """
    # Your code here
    lcm = a//(gcf(a,b))*b
    return lcm
                
        
    pass

# Part 3
def gcf(a, b):

    """
    recursive function by applying euclidean algorithm
    """
    # Your code here
    if a == 0:
        return b
    if b == 0:
        return a


    if a == b:
        return a

    if a > b:
        return gcf(a-b, b)
    return gcf(a, b-a)

    pass
print(lcm(3,6))