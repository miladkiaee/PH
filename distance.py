from pyrivet import rivet
from pyrivet import hilbert_distance
import seaborn as sns
import numpy as np
import os

from matplotlib import pyplot as plt

directory_in_str = '/home/milad/rivet/results_curvature/'

directory = os.fsencode(directory_in_str)

N = 40
count = 0

print('counting number of files ..')
for file_path in os.listdir(directory):
    filename: str = os.fsdecode(file_path)

    if filename.startswith("C"):
        osa = filename.split("osa")
        osa = osa[1].split(".")[0]

        if osa != "NA":
            print(filename)
            count = count + 1

print("calculated count = ", count)

face_h1_betti = []

print('calculating betti for faces for all subjects ..')

index = 0
for severity in [1, 2, 3, 4]:

        for file_path in os.listdir(directory):

            filename: str = os.fsdecode(file_path)

            if filename.startswith("C"):

                osa = filename.split("osa")
                osa = osa[1].split(".")[0]

                if osa != "NA":
                    osa = int(osa)

                    if osa == severity:
                        index = index + 1
                        print('file: ', filename, ' ..')
                        b = rivet.betti_file(directory_in_str + filename, homology=1, x=40, y=40)
                        face_h1_betti.append(b)
                        plt.imshow(b.graded_rank, origin='lower', aspect='auto', cmap='coolwarm')
                        plt.savefig('/home/milad/rivet/pics_curvature/' + filename + '.png')


distances = np.zeros((count, count))

for index1 in range(0, count):

    for index2 in range(0, count):

        h = hilbert_distance.distance(face_h1_betti[index1], face_h1_betti[index2])
        distances[index1, index2] = h


sns.set()
colors = ["white", "light grey", "grey", "dark grey", "light green", "green", "dark green",  "light blue",  "blue", "dark blue",  "butter", "orange", "dark orange", "light red",  "red", "dark red", "black"]
#sns.heatmap(l2, cmap=sns.xkcd_palette(colors), norm=PowerNorm(gamma=1), vmin=0, vmax=l2.max(), )

sns.heatmap(distances)
# plt.show()
plt.savefig('/home/milad/hilbert_heights.png', dpi=1000)

