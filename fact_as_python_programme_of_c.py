#definning python programme that is written in c language

from ctypes import*
fact=CDLL('factorial61.so')
def factorial(n):
    f=fact.factorial(n)
    if (f==-1):
        return "Give another value"
    else:
        return f
n1=input("Give the value of a positive integer")
n=int(n1)
print ("The value of the factorial ",n1," is ",factorial(n))
    
