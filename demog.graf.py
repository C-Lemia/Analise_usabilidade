# demog.graf.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import demog

# Gerar os DataFrames chamando as funções do módulo demog
df_demografico = demog.criar_dados_demograficos()
df_teste = demog.criar_dados_teste()

# Exibir o DataFrame de teste para verificação
print("DataFrame de Teste:\n", df_teste.head())  # Verifique se a coluna 'Dia' está presente

# Unir os dados demográficos com os dados de teste
df_teste = pd.merge(df_teste, df_demografico[['Codigo', 'Tipo_Cabelo']], on='Codigo')

# Exibir o DataFrame após a mesclagem para verificar as colunas
print("DataFrame de Teste após Mesclagem:\n", df_teste.head())  # Verifique a nova estrutura
print("Colunas do DataFrame de Teste após Mesclagem:\n", df_teste.columns)  # Verifique os nomes das colunas

# Configurar cores marrons, bege e cinza
cores = ['#8B4513', '#D2B48C', '#A9A9A9', '#CD853F', '#FFD700', '#FF6347']  # Adicione mais cores se necessário

# Ordenar Phototipo
df_demografico['Phototipo'] = pd.Categorical(df_demografico['Phototipo'], 
                                              categories=['I', 'II', 'III', 'IV', 'V', 'VI'], 
                                              ordered=True)

# Gráfico 1: Análise demográfica
plt.figure(figsize=(10, 6))
sns.countplot(data=df_demografico, x='Genero', hue='Genero', palette=cores[:2])  # Adicione 'hue'
plt.title('Distribuição de Gênero')
plt.xlabel('Gênero')
plt.ylabel('Número de Participantes')
plt.legend(title='Gênero')  # Mover a legenda para evitar sobreposição
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(data=df_demografico, x='Idade', kde=True, color=cores[0])
plt.title('Distribuição de Idade')
plt.xlabel('Idade')
plt.ylabel('Número de Participantes')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(data=df_demografico, x='Phototipo', hue='Phototipo', palette=cores[:6])  # Adicione 'hue'
plt.title('Distribuição de Phototipos (Fitzpatrick)')
plt.xlabel('Phototipo')
plt.ylabel('Número de Participantes')
plt.legend(title='Phototipo')  # Mover a legenda para evitar sobreposição
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(data=df_demografico, x='Tipo_Cabelo', hue='Tipo_Cabelo', palette=cores[:6])  # Adicione 'hue'
plt.title('Distribuição de Tipos de Cabelo')
plt.xlabel('Tipo de Cabelo')
plt.ylabel('Número de Participantes')
plt.legend(title='Tipo de Cabelo')  # Mover a legenda para evitar sobreposição
plt.show()

# Gráfico 2: Comparação dos Dias D0, D14 e D28
# Verifique se a coluna 'Dia' está presente no DataFrame df_teste
print("Colunas do DataFrame de Teste após Mesclagem:\n", df_teste.columns)

# Preparar os dados para o gráfico de linha
df_teste_melted = df_teste.melt(id_vars=['Codigo', 'Tipo_Cabelo'], 
                                  value_vars=['Oleosidade_D0', 'Oleosidade_D14', 'Oleosidade_D28'],
                                  var_name='Dia', value_name='Oleosidade')

# Limpar os nomes das colunas 'Dia'
df_teste_melted['Dia'] = df_teste_melted['Dia'].str.replace('Oleosidade_', '').str.replace('D', 'D')

# Gráfico para Oleosidade
plt.figure(figsize=(10, 6))
sns.lineplot(data=df_teste_melted, x='Dia', y='Oleosidade', hue='Tipo_Cabelo', palette=cores[:6])
plt.title('Comparação de Oleosidade entre D0, D14 e D28')
plt.xlabel('Dias')
plt.ylabel('Oleosidade')
plt.legend(title='Tipo de Cabelo')
plt.show()

# Para Porosidade
df_teste_melted = df_teste.melt(id_vars=['Codigo', 'Tipo_Cabelo'], 
                                  value_vars=['Porosidade_D0', 'Porosidade_D14', 'Porosidade_D28'],
                                  var_name='Dia', value_name='Porosidade')

# Limpar os nomes das colunas 'Dia'
df_teste_melted['Dia'] = df_teste_melted['Dia'].str.replace('Porosidade_', '').str.replace('D', 'D')

plt.figure(figsize=(10, 6))
sns.lineplot(data=df_teste_melted, x='Dia', y='Porosidade', hue='Tipo_Cabelo', palette=cores[:6])
plt.title('Comparação de Porosidade entre D0, D14 e D28')
plt.xlabel('Dias')
plt.ylabel('Porosidade')
plt.legend(title='Tipo de Cabelo')
plt.show()

# Para Hidratação
df_teste_melted = df_teste.melt(id_vars=['Codigo', 'Tipo_Cabelo'], 
                                  value_vars=['Hidratacao_D0', 'Hidratacao_D14', 'Hidratacao_D28'],
                                  var_name='Dia', value_name='Hidratacao')

# Limpar os nomes das colunas 'Dia'
df_teste_melted['Dia'] = df_teste_melted['Dia'].str.replace('Hidratacao_', '').str.replace('D', 'D')

plt.figure(figsize=(10, 6))
sns.lineplot(data=df_teste_melted, x='Dia', y='Hidratacao', hue='Tipo_Cabelo', palette=cores[:6])
plt.title('Comparação de Hidratação entre D0, D14 e D28')
plt.xlabel('Dias')
plt.ylabel('Hidratação')
plt.legend(title='Tipo de Cabelo')
plt.show()
