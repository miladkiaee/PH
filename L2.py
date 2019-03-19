import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib.colors import LogNorm
from matplotlib.colors import PowerNorm
import seaborn as sns
import os

directory_in_str = "" # set the directory containing the files

directory = os.fsencode(directory_in_str)

N = 50
Hilberts = []

for severity in [1, 2, 3, 4]:
    count = 0
    # storing all hilbert grid data first
    for file in os.listdir(directory):
        filename: str = os.fsdecode(file)

        if filename.startswith("hil"):
            osa = filename.split("osa")
            osa = osa[1].split(".")[0]

            #print("OSA: ", osa)
            if osa != "NA":
                osa = int(osa)

                if osa == severity:
                    count = count + 1
                    #print(directory_in_str, filename)
                    counter = 0
                    Hilbert = np.zeros((N, N))

                    with open(directory_in_str+filename, 'r') as f:
                        flag = 0
                        for line in f:

                            if 'Dimension' in line:
                                flag = 1

                                if 'Betti' in line:
                                    flag = 0
                                    break

                            if flag == 1:
                                if '(' in line:
                                    line = line.replace('(', '')
                                    line = line.replace(')', '')
                                    line = line.replace(' ', '')
                                    line = line.replace('\n', '')
                                    H = line.split(',')
                                    c = list(map(int, H))
                                    Hilbert[c[0], c[1]] = c[2]

                    # sort the array so we can access values easier
                    sorted(Hilbert, key=lambda x: (x[1], x[2]))
                    Hilberts.append(Hilbert)
    print("number of osa :", severity, "=",  count)


def l2_norm(a, b):
    a = a - b
    val = LA.norm(a, 'fro')
    return val


N = len(Hilberts)

l2 = np.zeros((N, N))

for i in range(N):
    for j in range(N):
        l2[i, j] = l2_norm(Hilberts[i], Hilberts[j])


l2 = l2 + 0.01
#l2 = l2/l2.max()

# uneven bounds changes the colormapping
sns.set()
colors = ["light grey","light light blue", "white", "white", "butter", "dark orange", "red", "dark red",  "black"]
sns.heatmap(l2, cmap=sns.xkcd_palette(colors), norm=PowerNorm(gamma=3), vmin=0, vmax=l2.max(), )

plt.show()
#plt.savefig('/home/milad/powerlaw.png', dpi=1000)
