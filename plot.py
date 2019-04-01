import numpy as np
import seaborn as sns

from matplotlib.colors import PowerNorm
from matplotlib import pyplot as plt
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument("-i", "--input", default= "", help="input file name")
parser.add_argument("-o", "--output", default= "", help="output file name")

args = parser.parse_args()

data = np.load(args.input)

sns.set()
colors = ["white", "light grey", "grey", "dark grey", "light green",
          "green", "dark green",  "light blue",  "blue", "dark blue",
          "butter", "orange", "dark orange", "light red",  "red", "dark red", "black"]

sns.heatmap(data, cmap=sns.xkcd_palette(colors), norm=PowerNorm(gamma=1), vmin=0, vmax=data.max(), )

# sns.heatmap(distances)
plt.show()
plt.savefig(args.output, dpi=1000)
