# %%

import pandas as pd

df = pd.read_csv("points_tmw.csv")
df.head()
# %%

print("Estatísticas de Posição para Transacoes:")

minimo = df["qtdPontos"].min()
print("Mínimo:", minimo)

media = df["qtdPontos"].mean()
print("Média:", media)

quartil_1 = df["qtdPontos"].quantile(0.25)
print("1 quartil:", quartil_1)

mediana = df["qtdPontos"].median()
print("Mediana:", mediana)

quartil_3 = df["qtdPontos"].quantile(0.75)
print("3 quartil:", quartil_3)

maximo = df["qtdPontos"].max()
print("Máximo:", maximo)

df["qtdPontos"].describe()
# %%
print("#########################")
print(("Estatísticas de Posição para Usuários:")
)
usuarios = df.groupby(["idUsuario"]).agg(
    {
    "idTransacao":"count",
    "qtdPontos":"sum",
    }
).reset_index()

usuarios
# %%

sumario = usuarios[['idTransacao', 'qtdPontos']].describe()

print(sumario.to_string())