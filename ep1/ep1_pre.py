import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

np.set_printoptions(precision=15, floatmode='maxprec')
  

def preliminar():
    x = np.arange(0, 20, 1) 
    resultados = [funcao(i) for i in x]
    return (x, resultados)
  
def funcao(x):
    return x**(2) - 5
  

variavel = preliminar()
tabela = pd.DataFrame({'X': variavel[0], 'f(X)': np.array(variavel[1], dtype=np.float64)})
pd.set_option('display.float_format', lambda x: f'{x:.15g}')
print(tabela)
  

fig, ax = plt.subplots()
ax.scatter(variavel[0], variavel[1], s=10)
ax.vlines(variavel[0], 0, variavel[1], colors='gray', linestyles='dashed')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.set_xlabel('X')
ax.set_ylabel('f(x)')
plt.show()
