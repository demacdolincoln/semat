# -*- coding: utf-8 -*-
"""
sendo:

F(x) = x**5 - cos(x)
G(x) = sen(x)**pi

calcule e exiba o gráfico de FoG

depois calcule e exiba o gráfico de GoF
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def F(x):
    return (x**5) - np.cos(x)
    
def G(x):
    return np.sin(x)**np.pi
    
amostra = np.linspace(-100, 100, num=1000)

pd.Series([F(G(x)) for x in amostra]).plot()
pd.Series([G(F(x)) for x in amostra]).plot()
plt.show()