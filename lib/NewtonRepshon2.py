from math import *
import math
def NewtonRaphsonMethod1(y, derivY , x0, TOL=0.01, NMAX=10):


    def f(x):
        return (x**3 - 3*x +2)
    def f_(x):
        return (3*x**2-3)

    # print ("\nThis script finds the x intercept of the function e^(-x/5)-sin(x), within the given range.\n")
    a = input("Enter the lower bound, a: ")
    b = input("Enter the upper bound, b: ")
    a = int(a)
    b = int(b)

    xn = a #semi-arbitrary starting point
    y = f(xn) #f #pow(e,(-xn/5.0))-sin(xn)
    derivY = f_(xn) #-(0.2)*pow(e,(-xn/5.0))-cos(xn)
    print ("xn = "),
    print (xn)
    print ("y = "),
    print (y)
    print ("derivative of y = "),
    print (derivY)

    steps = 0

    print ("\n********starting ********\n")

    while (abs(y) > 0.0000001):
        xnn = xn - (y / derivY)
        xn = xnn
        print ("new x is now at ",)
        print (xn)
        # y = pow(e,(-xn/5.0))-sin(xn)
        y = f(xn)
        print ("y value is now ",)
        print (y)
        derivY = f_(xn)
        # derivY = -(0.2)*pow(e,(-xn/5.0))-cos(xn)
        steps = steps+1
        print ("\n <><><><><><><><><><><><><><> \n")

    print ("\n********ended ********\n")

    print ("Newton's Method approximates that there is an x intercept at x = {0} ".format(xn))
    print ("{0} steps were taken.\n".format(steps))
    # print ("NOTE: THIS SCRIPT CAN ONLY FIND ONE INTERCEPT AT A TIME.")
    print ("RUN MULTIPLE TIMES WITH TARGETED RANGES TO FIND ALL INTERCEPTS.\n")

NewtonRaphsonMethod1(lambda x: math.pow(x,3) -3 * x +2,lambda x: 3*math.pow(x,2)-3,-2.4)

# -2.4