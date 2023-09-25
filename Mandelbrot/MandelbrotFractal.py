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

def CalculZ(itteration, complex):
    if(itteration == 0):
        return 0
    else:
        return CalculZ(itteration - 1, complex) ** 2 + complex
 

for n in range(10):
    print(f"Z({n}) = {CalculZ(n, complex = 1)}")
 

