import math
import pandas as pd
from ep1_pre import funcao

pd.options.display.float_format = '{:.8f}'.format

def derivada_funcao(x):
    return 2*x

def newton_raphson(f, df, x0, tol):
    lista_X = []
    lista_fX = []
    lista_dfX = []
    
    while True:
        fx = f(x0)
        dfx = df(x0)
        
        lista_X.append(x0)
        lista_fX.append(fx)
        lista_dfX.append(dfx)
        
        if abs(fx) < tol:
            break
        
        x0 = x0 - fx / dfx
    
    tabela = pd.DataFrame({
        'x': lista_X,
        'f(x)': lista_fX,
        'f\'(x)': lista_dfX
    })
    
    return x0, tabela

x0 = 2  # Chute inicial
tol = 1e-5  # Tolerância

raiz, tabela = newton_raphson(funcao, derivada_funcao, x0, tol)
print(f"A raiz encontrada é: {raiz:.8f}")

# Exibindo a tabela
print("\nTabela de valores:")
print(tabela)