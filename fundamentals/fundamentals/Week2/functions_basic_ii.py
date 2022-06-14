"""
Assignment: Functions Basic II
Author: Rodrigo Arguello-Serrano
Date:06/13/2022
"""

def countdown(c_number):
    """
    Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
    
    Example: countdown(5) should return [5,4,3,2,1,0]
    
    Parameter c_number: is the number to start the countdown
    Precondition: c_number is a interger
    """
    result = []
    for i in range(c_number,-1,-1):
        result.append(i)
    return result

print(countdown(8))

def print_and_return(l):
    """
    Print the first value and return the second.
    Example: print_and_return([1,2]) should print 1 and return 2

    Parameter l: is a list with two elements
    Precondition: l has two elements
    """
    print(l[0])
    return l[1]
print(print_and_return([1,2]))

def values_greater_than_second(l):
    """
    Return a new list containing only the values from the original list that are greater than its 2nd value. 
    Print how many values this is and then return the new list. If the list has less than 2 elements,
    have the function return False.
    
    Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
    Example: values_greater_than_second([3]) should return False

    Parameter l: is a list
    Precondition: l is not EMPTY 
    """
    result = []
    if len(l) < 2:
        return False
    elif len(l) >=2:
        for i in range(len(l)):
            if l[i] > l[1] and i !=1:
                result.append(l[i])
        print(len(result))
        return result 

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([5]))

def this_length_that_value(size, value):
    """
    Return a list whose length is equal to the given size, and whose values are all the given value.
    
    Example: length_and_value(4,7) should return [7,7,7,7]
    Example: length_and_value(6,2) should return [2,2,2,2,2,2]
    
    Parameter size: is an integer
    Parameter value: is an integer
    Precondition: size and value are not zero 
    """
    result = []
    for i in range(size):
        result.append(value)
    return result

print(this_length_that_value(4,7))

print(this_length_that_value(6,2))