#quadratic2.py
import math
def main():
    print(" \n")
    a,b,c=eval(input("Please enter the coefficients(a,b,c):"))
    delta=b*b-4*a*c
    if delta>=0:
        discRoot=math.sqrt(delta)
        root1=(-b+discRoot)/(2*a)
        root2=(-b-discRoot)/(2*a)
        print("\nThe solutions are:",root1,root2)
    else:
        print("The equation has no real roots!")
main()
