from platform import platform
import matplotlib as mpl
import matplotlib.pyplot as plt
from cycler import cycler

mpl.style.use("ggplot")
mpl.rcParams["figure.figsize"] = (20, 5)
mpl.rcParams["axes.facecolor"] = "white"
mpl.rcParams["axes.grid"] = True
mpl.rcParams["grid.color"] = "lightgray"
mpl.rcParams["axes.prop_cycle"] = cycler(
    color=plt.get_cmap("tab10").colors
)  # ["b", "r", "g", "y"]
