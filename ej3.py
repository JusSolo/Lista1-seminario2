import numpy as np
import matplotlib.pyplot as plt

def simular_lanzamientos(p, N=100000):
    resultados = [0] * N
    for i in range(N):
        j = 1
        while np.random.binomial(1, p) == 0:
            j += 1
        resultados[i] = j
    return resultados

# Valores de p
p_values = [0.1, 0.2, 0.5, 0.7]
N = 10000  # Número de simulaciones

# Crear figura
fig, ax = plt.subplots(figsize=(10, 6))

for p in p_values:
    r = simular_lanzamientos(p, N)  # Genera los datos
    r = np.array(r)/1000
    ax.hist(r, bins='auto', density=True, histtype='stepfilled', alpha=0.4, label=f"p={p}")

ax.set_xlabel("Número de intentos hasta el primer éxito")
ax.set_ylabel("Densidad empírica")
ax.set_title("Densidades de la distribucion generada por el lansamiento de una moneda")
ax.legend()
ax.grid()

plt.show()
