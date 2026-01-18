"""
Análise inicial da base 202501_Cadastro.csv
- Importação
- Limpeza básica
- Análise exploratória simples
"""

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(
    '202501_Cadastro.csv',
    sep=';',
    encoding='latin1'
)

df['DATA_APOSENTADORIA'] = (
    df['DATA_APOSENTADORIA']
    .astype(str)
    .str.replace('\xa0', '', regex=False)
    .str.strip()
)

df['DATA_APOSENTADORIA'] = pd.to_datetime(
    df['DATA_APOSENTADORIA'],
    format='%d/%m/%Y',
    errors='coerce'
)

df['DATA_APOSENTADORIA'] = pd.to_datetime(
    df['DATA_APOSENTADORIA'],
    format='%d/%m/%Y',
    errors='coerce'
)

df['DATA_INGRESSO_CARGOFUNCAO'] = (
    df['DATA_INGRESSO_CARGOFUNCAO']
    .astype(str)
    .str.replace('\xa0', '', regex=False)
    .str.strip()
)

df['DATA_INGRESSO_CARGOFUNCAO'] = pd.to_datetime(
    df['DATA_INGRESSO_CARGOFUNCAO'],
    format='%d/%m/%Y',
    errors='coerce'
)

df['DATA_INGRESSO_CARGOFUNCAO'] = pd.to_datetime(
    df['DATA_INGRESSO_CARGOFUNCAO'],
    format='%d/%m/%Y',
    errors='coerce'
)

#Mostrar colunas selecionadas
df_selecionado = df[['NOME', 'MATRICULA', 'DATA_APOSENTADORIA',
                     'DESCRICAO_CARGO', 'SITUACAO_VINCULO']]

'''
#Ver todas as colunas e todas as infos
df.info()
print (df.head())

df.info()
print (df['DESCRICAO_CARGO'].value_counts())
print (df['SITUACAO_VINCULO'].value_counts())
print (df['TIPO_APOSENTADORIA'].value_counts())
'''
#O que essa base contém? Esta base contem dados de funcionarios aposentados de certo departamento publico

#Quais colunas fazem mais sentido analisar? Tipo de aposentadoria, descrição do cargo, tempo médio de
#permanência no cargo, Jornada de trabalho, Regime juridico

#O que ainda não foi feito? Leitura dinamica com graficos
#sem rotulo de dados
'''
plt.figure(figsize=(7,5))

sns.countplot(
    data=df,
    x='TIPO_APOSENTADORIA',
    order=df['TIPO_APOSENTADORIA'].value_counts().index
)

#Adicionam títulos ao gráfico e aos eixos para ficar claro o que está sendo mostrado.
plt.title('Distribuição por Tipo de Aposentadoria')
plt.xlabel('Tipo de Aposentadoria')
plt.ylabel('Quantidade')
#ROTACIONA LEGENDA
plt.xticks(rotation=90)
#Garante que tudo fique a mostra no gráfico, sem cortes
plt.tight_layout()
plt.show()
'''
#Com rotulo de dados
ax = sns.countplot(data=df, x='TIPO_APOSENTADORIA')

for p in ax.patches:
    ax.annotate(
        p.get_height(),                    # valor
        (p.get_x() + p.get_width() / 2,    # posição X
         p.get_height()),                  # posição Y
        ha='center',
        va='bottom'
    )
plt.title('Distribuição por Tipo de Aposentadoria')
plt.xlabel('Tipo de Aposentadoria')
plt.ylabel('Quantidade')
plt.show()


ax = sns.countplot(data=df, y='DESCRICAO_CARGO')

for p in ax.patches:
    ax.annotate(
        p.get_width(),
        (p.get_width(), p.get_y() + p.get_height() / 2),
        va='center'
    )

plt.title('Distribuição por Cargo')
plt.xlabel('Cargo')
plt.ylabel('Quantidade')
plt.tight_layout()
plt.show()


'''
sns.countplot(
    data=df, 
    x='JORNADA_DE_TRABALHO', 
    order= df['JORNADA_DE_TRABALHO'].value_counts().index
)

plt.title('Jornada de Trabalho geral')
plt.xlabel ('Tipo de jornada')
plt.ylabel ('Quantidade')
plt.xticks (rotation = 90)
plt.tight_layout

plt.show()
'''