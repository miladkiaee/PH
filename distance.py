from pyrivet import rivet
from pyrivet import hilbert_distance
import numpy as np
import os

from matplotlib import pyplot as plt

directory_in_str = '/home/milad/rivet/results_curvature/'
pic_directory_in_str = '/home/milad/rivet/pics_curvature/'

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
indexFile = open('indexFile.txt', 'w')

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
                    indexName = filename.split(".txt")[0]
                    indexFile.write("%s, %s\n" % (index, indexName))

indexFile.close()

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
                    b = rivet.betti_file(directory_in_str + filename, homology=0, x=50, y=50)
                    # np.save(directory_in_str + filename + '.npy', b.graded_rank)
                    face_h1_betti.append(b)
                    plt.imshow(b.graded_rank, origin='lower', aspect='auto', cmap='coolwarm')
                    plt.savefig(pic_directory_in_str + filename + '.png')


distances = np.zeros((count, count))

print("calculating hilbert distances .. ")
for index1 in range(0, count):
    for index2 in range(0, count):
        print("indices: ", index1, ", ", index2)
        h = hilbert_distance.distance(face_h1_betti[index1], face_h1_betti[index2])
        distances[index1, index2] = h


np.save('distances_curvature.npy', distances)

print("done!")
