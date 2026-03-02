import math

"""
Use the Gauss-Legendre Algorithm to estimate Pi. Perform 10 approximation loops. Once complete, return the approximation.
:return:
"""

# a variable to hold your returned estimate for PI. When you are done,
# set your estimated value to this variable. Do not change this variable name
pi_estimate = 0

"""
Step 1: Declare and initialize all the values for the Gauss-Legendre algorithm
"""

# modify these lines to correct set the variable values
a = 1
b = 1/((2)**(1/2))
t = 1/4
p = 1

# perform 10 iterations of this loop
for i in range(1, 10):
    ai = (a+b)/2
    bi = (a*b)**(1/2)
    ti = t - (p*(a-ai)**2)
    pi2 = 2*p

    a = ai
    b = bi
    t = ti
    p = pi2
    

    # print out the current loop iteration. This is present to have something in the loop.
    print("Loop Iteration: ", i)

"""
Step 3: After iterating 10 times, calculate the final value for PI
"""

# modify this line below to estimate PI
pi_estimate = ((a+b)**2)/(4*t)

print("Final estimate for PI: ", pi_estimate)
print("Error on estimate: ", abs(pi_estimate - math.pi))
