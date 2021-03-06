import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def G(x):
    return np.sin(x)**np.pi


amostra = np.linspace(0, 200, num=1000)

serie = pd.Series([G(i) for i in amostra])
serie.plot()

plt.show()
