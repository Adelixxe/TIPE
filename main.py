import numpy as np
import matplotlib.pyplot as plot

#_______________________________________________
long=larg=haut=30 #Dimensions bac 30x30x30 (mm)
lambdaT = 0.75
µ=1250 #Volume massique 1250 pour la terre
c=1350 #Capacité thermique 1350 pour la terre
difTherm= lambdaT/(µ*c) #On obtient 0.44 *10^-6
Tf, Tc = 300, 700

dx=dy=dz=0.1
nx,ny,nz = int(larg/dx), int(long/dy), int(haut/dz)
dx2, dy2, dz2 = dx**2, dy**2, dz**2