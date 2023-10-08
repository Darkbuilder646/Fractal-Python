import numpy as np
import matplotlib.pyplot as plt


def Computes_Z(complex, max_itteration = 100):
    z = 0
    for i in range(max_itteration):
        z = z * z + complex
        yield z

def ComputesMandelbrot(complex, max_itteration = 100):
    for n, z_nbr in enumerate(Computes_Z(complex, max_itteration)):
        if(abs(z_nbr) > 2.0):
            return n # => the sequence diverges
        
    return max_itteration # => the sequence does not diverge
    
fig, ax = plt.subplots()

def DrawMandelbrot(start: float, end: float, step: float, max_itteration = 100):
    for x in np.arange(start, end+step, step):
        for y in np.arange(start, end+step, step):
            result = ComputesMandelbrot(x + y * 1j, max_itteration)
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

plt.xlabel("Real")
plt.ylabel("imaginary")

plt.imshow(image_array)
plt.show()