import math


def my_pi(target_error):
    a = 1
    b = 1/((2)**(1/2))
    t = 1/4
    p = 1
    pi_estimate = 0

    while(abs(pi_estimate-math.pi) > target_error):
        ai = (a+b)/2
        bi = (a*b)**(1/2)
        ti = t - (p*(a-ai)**2)
        pi2 = 2*p

        a = ai
        b = bi
        t = ti
        p = pi2

        pi_estimate = ((a+b)**2)/(4*t)

    """
    Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """

    return pi_estimate




desired_error = 1E-10

approximation = my_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")
