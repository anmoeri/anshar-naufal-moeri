# To find the n-th Fibonacci Number using formula
from math import sqrt 

n = int(input("Masukkan Angka : ")) 
# import square-root method from math library
def nthFib(n):
    res = (((1+sqrt(5))**n)-((1-sqrt(5)))**n)/(2**n*sqrt(5))
    if n in res :
        print(f"Angka {n} merupakan angka fibonacci")
    else:
        print(f"Angka {n} bukan angka fibonacci")
