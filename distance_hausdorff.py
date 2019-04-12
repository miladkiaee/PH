import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib.colors import LogNorm
from matplotlib.colors import PowerNorm
import seaborn as sns
import os
import scipy.spatial.distance as dist

directory_in_str = "/home/milad/rivet/hfiles_curvature/" # set the directory containing the files

directory = os.fsencode(directory_in_str)


def hausdorff(xa, xb):
    return dist.directed_hausdorff(xa, xb)


maxLambda = 10
levelHilberts = []
N = 0

for lambda0 in range(0, maxLambda):
    print("level ", lambda0)
    Hilberts = []

    numSub = 0
    for severity in [1, 2, 3, 4]:
        count = 0
        # storing all hilbert grid data first
        for file in os.listdir(directory):
            filename: str = os.fsdecode(file)

            if filename.startswith("hil"):
                osa = filename.split("osa")
                osa = osa[1].split(".")[0]

                # print("OSA: ", osa)
                if osa != "NA":
                    osa = int(osa)

                    if osa == severity:
                        count = count + 1
                        numSub = numSub + 1
                        # print(directory_in_str, filename)
                        cutoffHilbert = []

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

                                        if c[2] <= lambda0 and c[0] > 0 and c[1] > 0:
                                            cutoffHilbert.append([c[0], c[1]])

                        # all hilberts for all subject at the same levels are stored here
                        cutoff = np.array(cutoffHilbert)

                        Hilberts.append(cutoff)
        # print("number of osa : ", severity, " = ",  count)
    # print("total = ", numSub)

    # collection of same level hilberts
    levelHilberts.append(Hilberts)
    N = numSub


d = np.zeros((N, N))

for i in range(N):
    print("i", i)
    for j in range(N):
        # print("j", j)
        tmp = 0
        for level in range(0, maxLambda):
            # print("level ", level)
            l1 = levelHilberts[level][i]
            l2 = levelHilberts[level][j]

            if l1.shape[0] > 0 and l2.shape[0] > 0:
                a = hausdorff(l1, l2)
                a = a[0]
            else:
                a = -100

            if tmp < a:
                tmp = a
            d[i, j] = a


d = d + 0.001

# uneven bounds changes the colormapping
# sns.set()
# colors = ["light grey","light light blue", "white", "white", "butter", "dark orange", "red", "dark red",  "black"]
# sns.heatmap(d, cmap=sns.xkcd_palette(colors), norm=PowerNorm(gamma=3), vmin=0, vmax=d.max(), )

plt.show()
#plt.savefig('/home/milad/powerlaw.png', dpi=1000)