import math
import pandas as pd
from ep1_pre import funcao

# Configurando o pandas para mostrar 8 casas decimais
pd.options.display.float_format = '{:.8f}'.format

def bisseccao(f, a, b, tol):
    lista_A, lista_B, lista_C = [], [], []
    lista_fA, lista_fB, lista_fC = [], [], []
    
    while (b - a) / 2.0 > tol:
        c = (a + b) / 2.0
        lista_A.append(a)
        lista_B.append(b)
        lista_C.append(c)
        
        fa, fb, fc = f(a), f(b), f(c)
        lista_fA.append(fa)
        lista_fB.append(fb)
        lista_fC.append(fc)
        
        if fc == 0:
            break
        if fa * fc < 0:
            b = c
        else:
            a = c
            
    # Criando o DataFrame
    tabela = pd.DataFrame({
        'a': lista_A,
        'b': lista_B,
        'c': lista_C,
        'f(a)': lista_fA,
        'f(b)': lista_fB,
        'f(c)': lista_fC
    })
    
    return c, tabela

raiz, tabela = bisseccao(funcao, 2, 3, 1e-5)
print(f"A raiz encontrada é: {raiz:.8f}")

# Exibindo a tabela
print("\nTabela de valores:")
print(tabela)
