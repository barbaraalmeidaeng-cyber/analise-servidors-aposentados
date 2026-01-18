"""
Análise exploratória de dados de servidores aposentados
Autor: Bárbara Almeida
Objetivo: gerar insights a partir de dados públicos
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Leitura da base de dados

df = pd.read_csv(
    '202501_Cadastro.csv',
    sep=';',
    encoding='latin1'
)


# Tratamento de datas

def limpar_converter_data(serie):
    return pd.to_datetime(
        serie.astype(str)
             .str.replace('\xa0', '', regex=False)
             .str.strip(),
        format='%d/%m/%Y',
        errors='coerce'
    )

colunas_data = [
    'DATA_APOSENTADORIA',
    'DATA_INGRESSO_CARGOFUNCAO'
]

df[colunas_data] = df[colunas_data].apply(limpar_converter_data)


# Análise exploratória

# Distribuição por tipo de aposentadoria
plt.figure(figsize=(8, 5))
ax = sns.countplot(
    data=df,
    x='TIPO_APOSENTADORIA',
    order=df['TIPO_APOSENTADORIA'].value_counts().index
)

for p in ax.patches:
    ax.annotate(
        p.get_height(),
        (p.get_x() + p.get_width() / 2, p.get_height()),
        ha='center',
        va='bottom'
    )

plt.title('Distribuição por Tipo de Aposentadoria')
plt.xlabel('Tipo de Aposentadoria')
plt.ylabel('Quantidade')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


# Distribuição por cargo
plt.figure(figsize=(8, 6))
ax = sns.countplot(
    data=df,
    y='DESCRICAO_CARGO',
    order=df['DESCRICAO_CARGO'].value_counts().index
)

for p in ax.patches:
    ax.annotate(
        p.get_width(),
        (p.get_width(), p.get_y() + p.get_height() / 2),
        va='center'
    )

plt.title('Distribuição por Cargo')
plt.xlabel('Quantidade')
plt.ylabel('Cargo')
plt.tight_layout()
plt.show()




