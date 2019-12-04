"""factorial_using_scipy_ritambasu61

"""
#used_timeit_to_calculate_the_time_taken_to_run_the_code
import scipy.special as sp
import timeit
m=int(input("Give a positive integer: "))
fact=sp.factorial(m)
print ("The value of factorial ",m," is ",fact,"\ntime taken to run the code: ", timeit.timeit())

