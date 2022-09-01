import pandas as pd
import matplotlib.pyplot as plt
from glob import glob
import sys

sys.path.append("..")
from utility import plot_settings


# --------------------------------------------------------------
# Opening a single Excel file
# --------------------------------------------------------------

data = pd.read_excel(
    "../../data/raw/pump_sensor_data/20180401_pump_sensor_data.xlsx",
    parse_dates=[0],
    index_col=[0],
)

# --------------------------------------------------------------
# Explore data
# --------------------------------------------------------------

data.head(10)
data.describe()
data.info()

# --------------------------------------------------------------
# Transform data
# --------------------------------------------------------------

data = data.drop(["sensor_15"], axis=1)

# --------------------------------------------------------------
# Plot data
# --------------------------------------------------------------

data["sensor_00"].plot()
data["sensor_01"].plot()

# --------------------------------------------------------------
# Plot data in loop
# --------------------------------------------------------------

for col in data.columns[:5]:
    data[col].plot()
    plt.show()

# --------------------------------------------------------------
# Combining multiple Excel files
# --------------------------------------------------------------

path = "../../data/raw/pump_sensor_data"
files = sorted(glob(path + "/*.xlsx"))

data_combined = pd.concat(
    [
        pd.read_excel(f, parse_dates=[0], index_col=[0]).drop(["sensor_15"], axis=1)
        for f in files
    ]
)

data_combined["sensor_00"].plot()

# --------------------------------------------------------------
# Export to .xlsx
# --------------------------------------------------------------

data_combined.to_excel("../../data/interim/data_combined.xlsx")

# --------------------------------------------------------------
# Export to .csv
# --------------------------------------------------------------

data_combined.to_csv("../../data/interim/data_combined.csv")
