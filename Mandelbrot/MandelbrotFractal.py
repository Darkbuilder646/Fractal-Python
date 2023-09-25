import numpy as np
import matplotlib.pyplot as plt

"""
Mandelbrot formula :
Z0 = 0
Zn+1 = (Zn)**2 + C

C = x + yi

3 values of C :
C = -1 | C = 0 | C = +1

Define a set :
Value de base = 2
Si |Zn| < {value} => belongs to the set
Si |Zn| > {value} => does not belong to the set
"""
"""
#//? Recursive function are limited for +1000 itteration
def CalculZ(itteration, complex):
    if(itteration == 0):
        return 0
    else:
        return pow(CalculZ(itteration - 1, complex), 2) + complex
""" 

def Calcul_Z(complex):
    z = 0
    while True:
        yield z
        z = pow(z, 2) + complex

max = int(input("Max itération : "))

for n, z_nbr in enumerate(Calcul_Z(complex=1)):
    print(f"Z({n}) = {z_nbr}")
    if n >= max:
        break
 

