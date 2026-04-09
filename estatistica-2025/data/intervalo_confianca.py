# %%

import pandas as pd
from scipy.stats import t as t_student

df = pd.read_csv("points_tmw.csv")
df.head()

# agrupando usuários por id e somando seus pontos.
usuarios = ((df.groupby("idUsuario").agg({
                "qtdPontos" : "sum"
            }).reset_index()))

usuarios
# %%
# pegando uma amostra do dataset de tamanho 100.



def intervalo(sample, alpha=0.05):
    n= len(sample)
    x_barra = sample.mean()
    s = sample.std()
    t = t_student.ppf(1-alpha/2, n-1)

    inf =  x_barra - t * s / (n ** 0.05)
    sup = x_barra + t * s / (n ** 0.05)
    
    return x_barra, s, inf, sup

stats = []
for i in range(1000):
    n = 100
    sample = usuarios["qtdPontos"].sample(n)
    stats.append(intervalo(sample))

stats = pd.DataFrame(stats, columns=["média", "desvio", "inf", "sup"])
stats

stats["verdadeiro"] = usuarios["qtdPontos"].mean()


# %%
stats["check"] = (stats["verdadeiro"] > stats["inf"]) & (stats["verdadeiro"] < stats["sup"])
stats["check"].mean()

# %%

import matplotlib.pyplot as plt

for i in range(30):
    data = stats.iloc[i]
    color = 'green' if data["check"] else 'red'
    plt.plot(data[['inf', 'sup']], [i,i], 'o--', color=color, alpha=0.5)

plt.grid()
plt.show()