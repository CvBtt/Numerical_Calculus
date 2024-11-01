import numpy as np
import matplotlib.pyplot as plt


class metodoSimpson():
    def __init__(self):
        self.sol_integral_analitica = 5 #estamos interessados apenas em uma função
        
    def fucao_integrada(self,x):
        return 6 - 6 * x ** 5
    
    def calcular_integral(self, limite_inicial, limite_final, numero_iteracao):
        numero_intervalos = 2 ** numero_iteracao
        tamanho_intervalo = (limite_final - limite_inicial)/numero_intervalos
        x = np.linspace(limite_inicial, limite_final, numero_intervalos + 1)
        pass
        
        
    
    def calcular_erro(self, valor_integral):
        return abs(self.sol_integral_analitica - valor_integral)
    
    def grafico(self):
        pass
    

        
        


