#import matplotlib #plotpackage
#matplotlib.use('TkAgg') #graphicspackage
#import matplotlib.pyplot as plt #might be a redunancy
from matplotlib import pyplot as plt #might be a redunancy
import csv

from statistics import mean
import numpy as np
from numpy.polynomial.polynomial import polyfit


def linefit():

    plt.figure()
    abscissa = []	#coordinate systems
    ordinate = []

    with open('/Users/grudnick/Work/UGresearch/Fall2019/Golledge/Repo/Research/data.v3.txt', 'r') as datafile:
        plots = csv.reader(datafile)
        firstline = datafile.readline()
        for line in datafile:
            x, y, dy = line.split()
            abscissa.append(float(x))
            ordinate.append(float(y))

    abscissa = np.array(abscissa)
    m, b = np.polyfit(abscissa, ordinate, 1)

    print(m, b)
    bestfunc = 'y= ' + str(m) + 'x+ ' + str(b)
    print(bestfunc)

    plt.plot(abscissa, ordinate, label='Data-line',color='green')
    plt.plot(abscissa, b + m * abscissa, '-', label='best-fit', color = 'orange')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Data')
    plt.legend()
    plt.show()
