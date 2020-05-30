# See wikipedia Gaussian function for this apodization window
import numpy as np
import matplotlib.pyplot as plt
import math

# See wikipedia Gaussian function for this apodization window
# returns a scale factor between on [0,1]
def gauss(angle,mina,maxa):
    width=float(maxa-mina)
    center=float(mina+width/2)
    x=float(angle)
    return (1-np.exp(-((x-center)**2 / ((.2*width)**2))))

def hann(angle,mina,maxa):
    width=float(maxa-mina)
    center=float(mina+width/2)
    w=width/(3.0*math.pi)
    x=float(angle)
    if (x-mina)<(width/3):
        return .5*(1+math.cos((x-mina)/w) )   
    elif (x-mina)>(2*width/3):
        return .5*(1-math.cos((x+(2*width/3)-mina)/w) )    
    else:
        return 0.0

x=np.zeros(180)
y=np.zeros(180)
for i in range(0,180):
    x[i]=i
    #y[i]=hann(i,130,150)
    y[i]=gauss(i,130,150)

plt.figure(1)
plt.subplot(111)
plt.plot(x[130:151],y[130:151])