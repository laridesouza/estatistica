# %%
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
# %%
df = pd.read_csv("points_tmw.csv")
df.head()
# %%

group_prod = (df.groupby("descProduto")["idTransacao"].count().reset_index())
group_prod

group_prod = group_prod.sort_values(by="idTransacao")
# %%

sns.barplot(group_prod, y="descProduto", x="idTransacao")
plt.xlabel("Quantidade de Transações")
plt.ylabel("Produto")
plt.title("Frequência de Produtos")
plt.savefig("Gráfico de Barras dos Produtos")
# %%

df["dataTransacao"] = pd.to_datetime(df["dtTransacao"]).dt.date
group_data = df.groupby("dataTransacao").agg(
    {
        "qtdPontos": "sum",
        "idTransacao": "count",
    }
).reset_index()

group_data = group_data.sort_values(by="dataTransacao")

plt.figure(figsize=[8,6])
plt.plot(group_data["dataTransacao"], group_data["idTransacao"])
plt.ylabel("Qtde. Transações")
plt.title("Série Histórica de Transações")
plt.legend(["Qtde. Transacoes"])
group_data
# %%

plt.hist(group_data["qtdPontos"], bins=10)
plt.show()
