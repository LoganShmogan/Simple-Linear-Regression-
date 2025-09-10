# -*- coding: utf-8 -*-
"""
Created on Thu Aug  7 13:53:29 2025

@author: young
"""

# Imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Import Dataset
dataset = pd.read_csv("AgeCholesterol.csv")

# Give dataset values
x = dataset.iloc[:,0].values
y = dataset.iloc[:,1].values

# Graph 1 - Plotting data
plt.ylabel("Age of Person")
plt.xlabel("Cholesterol level")
plt.title("Age of Person VS Cholesterol Level with Linear Regression")
plt.scatter(x, y)
plt.show()

# Linear Regression
linearModel = np.polyfit(x, y, 1)

# Calc
print("Slope:", linearModel[0], sep="\n\t")
print("Linear Regression:", linearModel, sep="\n\t")
print("Y-Intercept:", linearModel[1], sep="\n\t")

# Graph
plt.ylabel("Age of Person")
plt.xlabel("Cholesterol level")
plt.title("Linear Regression – NUMPY.POLYFIT _ Degree 1")
plt.scatter(x, y)
plt.plot(x, np.polyval(linearModel, x), 'r--')
plt.show()


