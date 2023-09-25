import numpy as np

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

