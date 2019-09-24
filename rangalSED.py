import random
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
xval = [3650, 4450, 5510, 6580, 8060, 9000, 12200, 21900]
yval = []


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
        #goodflag = k_flag
        #goodmask = totmask
        #goodktot = float(hawkiks_tot)


        #goodmag = -2.5*math.log10(goodktot) + 25

        #galnum.append(id)
        #flagarr.append(goodflag)
        #maskarr.append(goodmask)

#a = np.where(allgal.k_flag == 0 & allgal.totmask == 0)

for gal in allgal:
    if gal.k_flag == 0 and gal.totmask == 0 and -2.5*math.log10(gal.hawkiks_tot) + 25 < 23:
        goodgal.append(gal)

#print(goodgal)

random.seed(21)
sample_list = random.sample(goodgal, k=5)
print(sample_list)      #IDs: 2279, 3914, 3016, 4310, 2638
#print(a)

for goodgal in sample_list:
    print(id)








