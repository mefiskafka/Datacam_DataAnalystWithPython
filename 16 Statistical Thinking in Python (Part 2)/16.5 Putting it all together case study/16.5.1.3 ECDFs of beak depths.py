"""
ECDFs of beak depths
While bee swarm plots are useful, we found that ECDFs are often even better when doing EDA. Plot the ECDFs for the 1975 and 2012 beak depth measurements on the same plot.

For your convenience, the beak depths for the respective years has been stored in the NumPy arrays bd_1975 and bd_2012.

Instructions
100 XP
Compute the ECDF for the 1975 and 2012 data.
Plot the two ECDFs.
Set a 2% margin and add axis labels and a legend to the plot.
Hit 'Submit Answer' to view the plot!
Take Hint (-30 XP)

"""
import numpy as np
import pandas as pd
import os
from matplotlib import matplot as plt

mainpath = r"C:\\Users\\GESCOMEX\\Documents\\GitHub\\Datacam_DataAnalystWithPython\\_data"
filename = "*.csv"
fullpath = os.path.join(mainpath, filename)

bd_1975 = pd.read_csv(fullpath)
bd_2012 = pd.read_csv(fullpath)


def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n

    return (x, y)


# Compute ECDFs
x_1975, y_1975 = ecdf(bd_1975)
x_2012, y_2012 = ecdf(bd_2012)

# Plot the ECDFs
_ = plt.plot(x_1975, y_1975, marker='.', linestyle='none')
_ = plt.plot(x_2012, y_2012, marker='.', linestyle='none')

# Set margins
plt.margins(0.02)

# Add axis labels and legend
_ = plt.xlabel('beak depth (mm)')
_ = plt.ylabel('ECDF')
_ = plt.legend(('1975', '2012'), loc='lower right')

# Show the plot
plt.show()