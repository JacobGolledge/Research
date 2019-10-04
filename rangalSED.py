import random
import numpy as np
from numpy.polynomial.polynomial import polyfit
import matplotlib
import numpy as np
from numpy.polynomial.polynomial import polyfit
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import csv
import math
from collections import Counter

galnum = []
flagarr = []
maskarr = []
goodgal = []
xval = np.array([3739.739, 4321.689, 5473.757, 6480.621, 8210.915, 9179.498, 12410.147, 21475.139, 35576.76, 45035.187])
#xval = [3650, 4450, 5510, 6580, 8060, 9000, 12200, 21900, 35500, 44930]


yval = []
wave = []


galtwoy = []
galthreey = []
galfoury = []
galfivey = []


class Galaxy:
    def __init__(self, id , ra , dec , x , y , hawkiks_tot , k_flag , k_star , k_fluxrad , totmask , hawkiks , ehawkiks , vimosu , evimosu , vimosb , \
        evimosb , vimosv , evimosv , vimosr , evimosr , vimosi , evimosi , decamz , edecamz , fourstarj1 , efourstarj1 , hawkij , ehawkij , \
        irac1 , eirac1 , irac2, eirac2 , irac3 , eirac3 , irac4 , eirac4):
        self.id    = int(id)
        self.hawkiks_tot    = float(hawkiks_tot)
        self.k_flag = int(k_flag)
        #self.k_star    =
        #self.k_fluxrad    =
        self.totmask    = int(totmask)
        self.hawkiks    = float(hawkiks)
        #self.ehawkiks    =
        self.vimosu    = float(vimosu)
        #self.evimosu    =
        self.vimosb    = float(vimosb)
        #self.evimosb    =
        self.vimosv    = float(vimosv)
        #self.evimosv    =
        self.vimosr    = float(vimosr)
        #self.evimosr    =
        self.vimosi    = float(vimosi)
        #self.evimosi    =
        self.decamz    = float(decamz)
        #self.edecamz    =
        #self.fourstarj1    =
        #self.efourstarj1    =
        self.hawkij    = float(hawkij)
        #self.ehawkij    =
        self.irac1 = float(irac1)
        self.irac2 = float(irac2)
        self.irac3 = float(irac3)


    def __str__(self):
        return id + ' ' + hawkiks_tot + ' ' + k_flag + ' ' + totmask + ' ' + hawkiks + ' ' + vimosu + ' ' + vimosb + ' ' \
               + vimosv + ' ' + vimosr + ' ' + vimosi + ' ' + decamz + ' ' + hawkij


allgal = []

with open('/home/jacob/PHOTOMETRY/PHOTOM_CATS/SpARCS-0035_totalall_HAWKIKs.cat', 'r') as magfile:
    magplots = csv.reader(magfile)
    firstmagline = magfile.readline()
    for line in magfile:
        id , ra , dec , x , y , hawkiks_tot , k_flag , k_star , k_fluxrad , totmask , hawkiks , ehawkiks , vimosu , evimosu , vimosb , \
        evimosb , vimosv , evimosv , vimosr , evimosr , vimosi , evimosi , decamz , edecamz , fourstarj1 , efourstarj1 , hawkij , ehawkij , \
        irac1 , eirac1 , irac2, eirac2 , irac3 , eirac3 , irac4 , eirac4 = line.split()

        gal = Galaxy(id , ra , dec , x , y , hawkiks_tot , k_flag , k_star , k_fluxrad , totmask , hawkiks , ehawkiks , vimosu , evimosu , vimosb , \
        evimosb , vimosv , evimosv , vimosr , evimosr , vimosi , evimosi , decamz , edecamz , fourstarj1 , efourstarj1 , hawkij , ehawkij , \
        irac1 , eirac1 , irac2, eirac2 , irac3 , eirac3 , irac4 , eirac4)

        allgal.append(gal)
        goodflag = int(k_flag)
        goodmask = totmask
        #print(k_flag)
        #print(totmask)
        #goodktot = float(hawkiks_tot)


        #goodmag = -2.5*math.log10(goodktot) + 25

        #galnum.append(id)
        flagarr.append(goodflag)
        maskarr.append(goodmask)

#print(flagarr)
#a = np.where((flagarr == 0) & (maskarr == 0))
#a = np.where(flagarr == 0)
#print(a)

for gal in allgal:
    if (gal.k_flag == 0) and (gal.totmask == 0) and (-2.5*math.log10(gal.hawkiks_tot) + 25 < 23):
        goodgal.append(gal)

#print(goodgal[0].vimosu)

random.seed(21)
sample_list = random.sample(goodgal, k=5)
print(sample_list)      #IDs: 2279, 3914, 3016, 4310, 2638
#print(a)

for rangal in sample_list:
    yval.append(rangal.vimosu)
    yval.append(rangal.vimosb)
    yval.append(rangal.vimosv)
    yval.append(rangal.vimosr)
    yval.append(rangal.vimosi)
    yval.append(rangal.decamz)
    yval.append(rangal.hawkij)
    yval.append(rangal.hawkiks)
    yval.append(rangal.irac1)
    yval.append(rangal.irac2)
    #print(yval)
    print(rangal.id)
    #print(yval)

galoney = yval[0:10]
galtwoy = yval[10:20]
galthreey = yval[20:30]
galfoury = yval[30:40]
galfivey = yval[40:50]

#G1y = np.array(galoney)



print(yval)
print(galoney)
print(galtwoy)
print(galthreey)
print(galfoury)
print(galfivey)
print(xval)
#print(G1y)


plt.plot(xval, galoney, '.')
plt.xlabel('Wavelength Angstroms')
plt.ylabel('f_nu')
plt.title('Galaxy One: 2279')
plt.show()

plt.plot(xval, galtwoy, '.')
plt.xlabel('Wavelength Angstroms')
plt.ylabel('f_nu')
plt.title('Galaxy One: 3914')
plt.show()

plt.plot(xval, galthreey, '.')
plt.xlabel('Wavelength Angstroms')
plt.ylabel('f_nu')
plt.title('Galaxy One: 3016')
plt.show()

plt.plot(xval, galfoury, '.')
plt.xlabel('Wavelength Angstroms')
plt.ylabel('f_nu')
plt.title('Galaxy One: 4310')
plt.show()

plt.plot(xval, galfivey, '.')
plt.xlabel('Wavelength Angstroms')
plt.ylabel('f_nu')
plt.title('Galaxy One: 2638')
plt.show()









