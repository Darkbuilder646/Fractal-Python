import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

def CustomCmap():
    colors = [(0, 0, 1), (0, 0, 0)]
    cmap = LinearSegmentedColormap.from_list('custom_cmap', colors, N=100)
    return cmap


def ComputesZ(complex, max_iterations = 100):
    z = 0
    for i in range(max_iterations):
        z = z * z + complex
        yield z

def ComputesMandelbrot(complex, max_iterations = 100):
    for n, z_nbr in enumerate(ComputesZ(complex, max_iterations)):
        if(abs(z_nbr) > 2.0):
            return n # => the sequence diverges
        
    return max_iterations # => the sequence does not diverge
  

def DrawMandelbrot(startX: float, endX: float, startY: float, endY: float, width, height, max_iterations=100):
    img = np.zeros((height, width))

    for x in range(width):
        for y in range(height):
            realNbr = startX + (x / (width - 1)) * (endX - startX)
            imagNbr = startY + (y / (height - 1)) * (endY - startY)
            c = complex(realNbr, imagNbr)
            color = ComputesMandelbrot(c, max_iterations)
            img[y, x] = color

    #cmap = CustomCmap()
    #default cmap = 'PuBu_r'
    plt.imshow(img, extent=(startX, endX, startY, endY), cmap='PuBu_r', origin='lower', vmax=max_iterations, vmin=0, interpolation='bilinear')
    plt.colorbar()
    plt.show()


DrawMandelbrot(-2.0, 1.0, -1.5, 1.5, 1000, 1000, 100)