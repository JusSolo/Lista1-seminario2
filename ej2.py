import numpy as np
from sklearn.metrics import mutual_info_score
from scipy.stats import entropy
import matplotlib.pyplot as plt

X = np.random.choice([0, 1, 2], size=1000, p=[0.3, 0.5, 0.2])
Y = np.random.choice([0, 1, 2], size=1000, p=[0.4, 0.4, 0.2])

# Informacion mutua de muesstras X y Y
I_XY = mutual_info_score(X, Y)
print(f"I(X;Y): {I_XY} ")

p = [0.25]*4
H = entropy(p, base=2)
print(f'Entropia de Shannon: {H}')


# Calcular frecuencias de X e Y
valores = np.array([0, 1, 2])  # Posibles valores en X e Y
freq_X = np.bincount(X, minlength=3) / len(X)  # Frecuencia relativa de X
freq_Y = np.bincount(Y, minlength=3) / len(Y)  # Frecuencia relativa de Y

# Graficar las densidades de X e Y con barras separadas
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
offset = 0.2  # Desplazamiento para separar las barras
plt.bar(valores - offset, freq_X, width=0.4, color="blue", alpha=0.6, label="X")
plt.bar(valores + offset, freq_Y, width=0.4, color="red", alpha=0.6, label="Y")
plt.xlabel("Valor")
plt.ylabel("Frecuencia relativa")
plt.title("Distribuciones de X y Y")
plt.xticks(valores)
plt.legend()

# Graficar la distribución de P
plt.subplot(1, 2, 2)
plt.bar(range(len(p)), p, width=0.4, color="green", alpha=0.7)
plt.xlabel("Valor")
plt.ylabel("Probabilidad")
plt.title("Distribución de P")
plt.xticks(range(len(p)))

plt.tight_layout()
plt.show()
