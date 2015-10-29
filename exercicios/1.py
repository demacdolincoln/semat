import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def f(x):
    return (x**5) * np.cos(x)


amostra = np.linspace(-100, 100, num=1000)

serie = pd.Series([f(i) for i in amostra])
serie.plot()

plt.show()
