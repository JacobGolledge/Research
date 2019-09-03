import matplotlib.pyplot as plt
plt.rcParams["backend"] = "TkAgg"

import csv
abscissa = []
ordinate = []

#with open('/home/jacob/Downloads/Research/data.v3.txt', 'r') as datafile:
with open('/Users/grudnick/Work/UGresearch/Fall2019/Golledge/Repo/Research/data.v3.txt', 'r') as datafile:
	plots = csv.reader(datafile)
	firstline = datafile.readline()
	for line in datafile:
		x, y, dy = line.split()


		abscissa.append(float(x))
		ordinate.append(float(y))
		
plt.plot(abscissa, ordinate, label='Loaded from file!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Data')
plt.legend()
plt.show()

