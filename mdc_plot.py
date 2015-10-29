# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
from matplotlib import pyplot as plt

def mdc(a, b):
    if b <=1:
        return a
    else:
        return mdc(b, a % b)

#pd.Series([mdc(5, i) for i in range(100)]).plot()

lista_dicionarios = []

for i in range(10):
   resultados = []
   for j in range(10):
       resultados.append(mdc(i, j))
   lista_dicionarios.append(resultados)


data = pd.DataFrame(lista_dicionarios)

data.plot()




plt.show()
