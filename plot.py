import numpy as np
import seaborn as sns

from matplotlib.colors import PowerNorm
from matplotlib import pyplot as plt
from argparse import ArgumentParser

parser = ArgumentParser()

directory_in_str = '/home/milad/rivet/results_height/'

parser.add_argument("-i", "--input", default= "", help="input file name")
parser.add_argument("-o", "--output", default= "", help="output file name")

args = parser.parse_args()

data = np.load(args.input)

sns.set()

colors = ["black", "dark blue", "dark red", "red",  "butter",  "white"]
midpoint = (data.max() - data.min()) / 2

sns.heatmap(data, cmap=sns.xkcd_palette(colors), norm=PowerNorm(gamma=1), vmin=0, vmax=data.max(), center=midpoint )

# sns.heatmap(data, cmap=sns.color_palette("RdYlBu", 100), center=midpoint)

#plt.show()
plt.savefig(args.output, dpi=1000)
