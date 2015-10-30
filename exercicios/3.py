# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def H(x):
    return np.log10(x) * (np.sin(x) ** x)


amostra = np.linspace(0, 200, num=1000)

serie = pd.Series([H(i) for i in amostra])
serie.plot()

plt.show()
