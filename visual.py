import csv

import matplotlib.pyplot as plt
import seaborn as sns
import seaborn.linearmodels as snsl
from datetime import datetime
import pandas as pd
import numpy as np


if __name__ == "__main__":
    sns.set_style("whitegrid")

    data = pd.read_csv('data.csv', parse_dates=True, index_col=0)
    print data.head()
    plt.figure(1)
    data[1:610].plot(y='power_consumption', grid=True)
    plt.figure(2)
    data[data.user_id == 1416].plot(y='power_consumption', grid=True)

    plt.show()
