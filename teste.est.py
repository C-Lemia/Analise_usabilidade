import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import demog  # Certifique-se de que o módulo demog esteja acessível

# Gerar os DataFrames chamando as funções do módulo demog
df_demografico = demog.criar_dados_demograficos()
df_teste = demog.criar_dados_teste()

# Unir os dados demográficos com os dados de teste
df_teste = pd.merge(df_teste, df_demografico[['Codigo', 'Tipo_Cabelo']], on='Codigo')

# Preparar os dados para a análise
oleosidade_d0 = df_teste['Oleosidade_D0']
oleosidade_d28 = df_teste['Oleosidade_D28']

porosidade_d0 = df_teste['Porosidade_D0']
porosidade_d28 = df_teste['Porosidade_D28']

hidratacao_d0 = df_teste['Hidratacao_D0']
hidratacao_d28 = df_teste['Hidratacao_D28']

# Calcular as diferenças para cada participante
df_teste['Diferença_Oleosidade'] = oleosidade_d28 - oleosidade_d0
df_teste['Diferença_Porosidade'] = porosidade_d28 - porosidade_d0
df_teste['Diferença_Hidratação'] = hidratacao_d28 - hidratacao_d0

# Realizar o teste T pareado para Oleosidade
t_stat_oleosidade, p_value_oleosidade = stats.ttest_rel(oleosidade_d0, oleosidade_d28)

# Realizar o teste de Wilcoxon para Oleosidade
wilcoxon_stat_oleosidade, wilcoxon_p_value_oleosidade = stats.wilcoxon(oleosidade_d0, oleosidade_d28)

# Realizar o teste T pareado para Porosidade
t_stat_porosidade, p_value_porosidade = stats.ttest_rel(porosidade_d0, porosidade_d28)

# Realizar o teste de Wilcoxon para Porosidade
wilcoxon_stat_porosidade, wilcoxon_p_value_porosidade = stats.wilcoxon(porosidade_d0, porosidade_d28)

# Realizar o teste T pareado para Hidratação
t_stat_hidratacao, p_value_hidratacao = stats.ttest_rel(hidratacao_d0, hidratacao_d28)

# Realizar o teste de Wilcoxon para Hidratação
wilcoxon_stat_hidratacao, wilcoxon_p_value_hidratacao = stats.wilcoxon(hidratacao_d0, hidratacao_d28)

# Compilar os resultados
resultados = {
    'Métrica': ['Oleosidade', 'Porosidade', 'Hidratação'],
    'Estatística T': [t_stat_oleosidade, t_stat_porosidade, t_stat_hidratacao],
    'P-Valor T-Pareado': [p_value_oleosidade, p_value_porosidade, p_value_hidratacao],
    'Estatística Wilcoxon': [wilcoxon_stat_oleosidade, wilcoxon_stat_porosidade, wilcoxon_stat_hidratacao],
    'P-Valor Wilcoxon': [wilcoxon_p_value_oleosidade, wilcoxon_p_value_porosidade, wilcoxon_p_value_hidratacao],
}

df_resultados = pd.DataFrame(resultados)

# Criar gráfico para as estatísticas
x_labels = df_resultados['Métrica']

# Definindo as posições dos grupos no gráfico
x = range(len(x_labels))

# Criar um gráfico de barras para T-Statistic e Wilcoxon Statistic
plt.figure(figsize=(12, 6))

# Gráfico para Estatísticas T
plt.bar(x, df_resultados['Estatística T'], width=0.4, label='Estatística T', color='#8B4513', align='center')

# Gráfico para Estatísticas Wilcoxon
plt.bar([p + 0.4 for p in x], df_resultados['Estatística Wilcoxon'], width=0.4, label='Estatística Wilcoxon', color= '#A9A9A9', align='center')

# Adicionando título e rótulos
plt.title('Comparação de Estatísticas T e Wilcoxon')
plt.xticks([p + 0.2 for p in x], x_labels)  # Ajustar rótulos no meio dos grupos
plt.ylabel('Valor da Estatística')
plt.xlabel('Métricas')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  # Linha horizontal para referência
plt.legend()

# Exibir o gráfico
plt.grid(axis='y')
plt.show()
