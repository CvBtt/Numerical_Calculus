import numpy as np
import matplotlib.pyplot as plt

# Constantes e parâmetros
h = 0.01 * 2 * np.pi  # Passo inicial (fração do período)
F_start = 0.0         # Valor inicial de F
F_end = 0.35          # Valor final de F
dF = 0.00025          # Incremento de F
omega = 1.0           # Fator frequência (ajustável conforme necessário)
transiente = 200000   # Número de passos para evolução do transiente
periodos = 100        # Evolução de 100 períodos após o transiente

# Sistema de equações (ajuste conforme necessário)
def g(t, x, v, F):
    return v

def f(t, x, v, F):
    return F * np.cos(omega * t) - x

# Método RK4 para resolver as EDOs
def runge_kutta_4(t, x, v, F, h):
    k1x = h * g(t, x, v, F)
    k1v = h * f(t, x, v, F)
    
    k2x = h * g(t + h / 2, x + k1x / 2, v + k1v / 2, F)
    k2v = h * f(t + h / 2, x + k1x / 2, v + k1v / 2, F)
    
    k3x = h * g(t + h / 2, x + k2x / 2, v + k2v / 2, F)
    k3v = h * f(t + h / 2, x + k2x / 2, v + k2v / 2, F)
    
    k4x = h * g(t + h, x + k3x, v + k3v, F)
    k4v = h * f(t + h, x + k3x, v + k3v, F)
    
    x_next = x + (k1x + 2 * k2x + 2 * k3x + k4x) / 6
    v_next = v + (k1v + 2 * k2v + 2 * k3v + k4v) / 6
    t_next = t + h
    
    return t_next, x_next, v_next

# Inicializando listas para o diagrama de bifurcação
bifurcation_F = []
bifurcation_x = []

# Loop para varrer os valores de F
F = F_start
while F <= F_end:
    # Condições iniciais
    t = 0.0
    x = 0.0
    v = 0.0
    
    # Evoluir transiente
    for _ in range(transiente):
        t, x, v = runge_kutta_4(t, x, v, F, h)
    
    # Ajustar passo para resolver cada período
    h_periodo = 0.001 * 2 * np.pi
    pontos_periodo = []
    
    # Evoluir por 100 períodos e coletar os valores de x
    for i in range(periodos):
        for _ in range(int(2 * np.pi / h_periodo)):
            t, x, v = runge_kutta_4(t, x, v, F, h_periodo)
        pontos_periodo.append(x)
    
    # Salvar os valores para o diagrama de bifurcação
    bifurcation_F.extend([F] * len(pontos_periodo))
    bifurcation_x.extend(pontos_periodo)
    
    # Incrementar F
    F += dF

# Plotar o diagrama de bifurcação
plt.figure(figsize=(10, 6))
plt.scatter(bifurcation_F, bifurcation_x, s=0.1, color="black")
plt.xlabel("F")
plt.ylabel("x")
plt.title("Diagrama de Bifurcação")
plt.grid(True)
plt.show()
