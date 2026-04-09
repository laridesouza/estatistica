# %%

import pandas as pd 
import sqlalchemy

df = pd.read_csv("points_tmw.csv")
df.head()

# abrindo conexão com sqlalchemy
engine = sqlalchemy.create_engine("sqlite:///points_tmw.db")
df.to_sql("points", engine, if_exists="replace", index=False)
# %%

freq_produto = df.groupby(df["descProduto"])[["idTransacao"]].count() # freq. abs.

freq_produto["Freq. Abs Acum."] = freq_produto["idTransacao"].cumsum() # freq. abs. acum.

freq_produto["Freq. Rel. "] = freq_produto["idTransacao"] / freq_produto["idTransacao"].sum() # freq. rel.

freq_produto["Freq. Rel. Abs."] = freq_produto["Freq. Rel. "].cumsum() # freq. rel. acum.

freq_produto

# %%

# fazendo as frequeências para descCategoriaProduto 

# tabela de frequência absoluta (contagem)

freq_categoria = df.groupby(df["descCategoriaProduto"])[["idTransacao"]].count()

# tabela de frequência absoluta acumulada
freq_categoria["Freq. Abs. Acum."]= freq_categoria.cumsum()
freq_categoria

# tabela de frequência relativa
freq_categoria["Freq. Rel."] = freq_categoria["idTransacao"] / freq_categoria["idTransacao"].sum()
freq_categoria

# tabela de frequência relativa acumulada
freq_categoria["Freq. Rel. Acum."] = freq_categoria["Freq. Rel."].cumsum()
freq_categoria

# %%

freq_cat = df.groupby(["descCategoriaProduto"])[["idTransacao"]].count().rename(columns={"idTransacao" : "Freq. Abs"})

freq_cat["Freq. Abs. Acum"] = freq_cat.cumsum()
freq_cat

freq_cat["Freq. Rel."] = freq_cat["Freq. Abs"] / freq_cat["Freq. Abs"].sum()

freq_cat["Freq. Rel. Acum."] = freq_cat["Freq. Rel."].cumsum()
freq_cat