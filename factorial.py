# In this exercise you are going to create a function that takes a number parameter and returns the factorial 
# of it.
# A factorial is the result of multiplying a sequence of descending numbers down to 0. Factorials are only defined for non-negative integer 
# numbers. This definition includes zero. Though 0! is equal to 1, so treat it as an edge case.

# factorial(4) # => 24 (4 * 3 * 2 * 1)

def factorial(num):
    answer = 0
    i = num
    while i > 1:
        answer = num * (i -1)
        num = answer
        i-= 1
    
    return answer
print(factorial(6))

pass