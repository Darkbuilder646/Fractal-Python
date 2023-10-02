import numpy as np
import matplotlib.pyplot as plt

""" Recursive function
#//? Recursive function are limited for +1000 itteration
def CalculZ(itteration, complex):
    if(itteration == 0):
        return 0
    else:
        return pow(CalculZ(itteration - 1, complex), 2) + complex
""" 
""" Test Function
def Calcul_Z(complex, stop = 0):
    z = 0
    while stop == 0:
        yield z
        z = pow(z, 2) + complex

max = 5
for n, z_nbr in enumerate(Calcul_Z(complex=1)):
    print(f"Z({n}) = {z_nbr}")
    if n >= max:
        break
"""

def Calcule_Z(complex, max_itteration = 100):
    z = 0
    for i in range(max_itteration):
        z = z * z + complex
        yield z

def CalculeMandelbrot(complex, max_itteration = 100):
    for n, z_nbr in enumerate(Calcule_Z(complex, max_itteration)):
        if(abs(z_nbr) > 2.0):
            return n # => la suite diverge
        
    return max_itteration # => la suite diverge pas
    
fig, ax = plt.subplots()

def DrawMandelbrot(start: float, end: float, step: float, max_itteration = 100):
    for x in np.arange(start, end+step, step):
        for y in np.arange(start, end+step, step):
            result = CalculeMandelbrot(x + y * 1j, max_itteration)
            if(result != max_itteration):
                point = plt.Circle((x, y), 0.015, color="white")
                ax.add_artist(point)
            else:
                point = plt.Circle((x, y), 0.015, color="black")
                ax.add_artist(point)

DrawMandelbrot(-2.5, 1.5, 0.05, 100)

fig.canvas.draw()
width, height = fig.canvas.get_width_height()
image_array = np.array(fig.canvas.renderer.buffer_rgba())

ax.set_xlim(-2.5,1)
ax.set_ylim(-1.5,1.5)

ax.axhline(0, color="black", linewidth=0.5)
ax.axvline(0, color="black", linewidth=0.5)

plt.xlabel("Réel")
plt.ylabel("Imaginair (i)")

plt.imshow(image_array)
plt.show()

