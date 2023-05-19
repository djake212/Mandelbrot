import numpy as np
import matplotlib.pyplot as plt

X = 512
Y = 384

#checking if in mandelbrot set function
def mandchecker(c):

    itcount = 1
    z = c
    for i in range(0,250):
       itcount += 1
       z = z**2 + c
       if abs(z) > 2.0:
           break
       elif abs(z) <= 2 and itcount == 250:
           itcount = 0
    return itcount

#zoom window
xstart = -0.110584319150
xend = -0.099361008487
ystart = 0.906417685636
yend = 0.898561368171

cplane = np.zeros((X,Y), dtype='uint8')
for x in range(0,X-1):
    for y in range(0,Y-1):
        comp = complex(xstart +(x/X)*(xend-xstart),ystart +(y/Y)*(yend-ystart))
        cplane[x,y] = mandchecker(comp)
        

plotarr = np.flipud(cplane.transpose())
f1, ax1 = plt.subplots()
picture = ax1.imshow(plotarr,cmap = 'nipy_spectral')
ax1.axis('off')
f1.show()
plt.savefig("fractal.ps")

input("\nPress <Enter> to exit...\n")