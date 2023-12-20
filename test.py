import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit

# generate a random dataframe with an exponential decay

x = np.linspace(0, 10, 1000)
y = np.exp(-x)

df = pd.DataFrame({'x': x, 'y': y})

# add some noise to the y data
df['y'] = df['y'] + np.random.normal(0, 0.1, len(df['y']))


# define the function to fit
def func(x, a, b):
    return a * np.exp(-b * x)

# fit the data
popt, pcov = curve_fit(func, df['x'], df['y'])

# plot the data
plt.plot(df['x'], df['y'])

# plot the fit
plt.plot(df['x'], func(df['x'], *popt), 'r-')

plt.show()