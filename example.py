import numpy as np

from pyrivet import rivet


#Equivalent to the 'points2.txt' sample data file in the RIVET distribution
points = rivet.PointCloud(
    points = [
        (0.3, 1.5, 2.1), # will appear at 1
        (4.2, 3.8, 4.9), # will appear at 3.2
        (5.6, 2.3, 6),   # will appear at 2
        (2.9, 5.1, 3.3), # will appear at 4
        (3.3, 2.0, 2.5), # will appear at 2.5
        (4.1, 1.1, 2.3), # will appear at 2.4
        (1.1, 1.3, 1.7), # will appear at 2
    ],
    second_param_name='time',
    appearance=[1, 3.2, 2, 4, 2.5, 2.4, 2],
    max_dist=3.1 # pyrivet will calculate max_dist if you leave it out
)

# Now let's take the Betti information
betti = rivet.betti(points)

print(betti)


# Let's look at H0, binned into 10x10.
aspirin_h0_betti = rivet.betti_file('aspirin-ZINC000000000053.sdf.txt', homology=0, x=10, y=10)
tylenol_h0_betti = rivet.betti_file('tylenol-ZINC000013550868.sdf.txt', homology=0, x=10, y=10)

# We can compute distance between these using Hilbert functions
from pyrivet import hilbert_distance
print("Distance with Hilbert functions:", 
      hilbert_distance.distance(
          aspirin_h0_betti, 
          tylenol_h0_betti
      )
     )
