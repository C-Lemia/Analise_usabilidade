import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import demog 

# Gerar os dados demográficos e de teste
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

# Realizar o teste t pareado
t_stat_oleosidade, p_value_oleosidade = stats.ttest_rel(oleosidade_d0, oleosidade_d28)
t_stat_porosidade, p_value_porosidade = stats.ttest_rel(porosidade_d0, porosidade_d28)
t_stat_hidratacao, p_value_hidratacao = stats.ttest_rel(hidratacao_d0, hidratacao_d28)

# Compilar os resultados
resultados = {
    'Métrica': ['Oleosidade', 'Porosidade', 'Hidratação'],
    'Estatística T': [t_stat_oleosidade, t_stat_porosidade, t_stat_hidratacao],
    'P-Valor': [p_value_oleosidade, p_value_porosidade, p_value_hidratacao],
    'Significativo': [p_value_oleosidade < 0.05, p_value_porosidade < 0.05, p_value_hidratacao < 0.05]
}

df_resultados = pd.DataFrame(resultados)

# Criar gráfico
plt.figure(figsize=(10, 6))
plt.bar(df_resultados['Métrica'], df_resultados['Estatística T'], color=['blue', 'orange', 'green'])
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.title('Estatísticas T para Oleosidade, Porosidade e Hidratação')
plt.xlabel('Métricas')
plt.ylabel('Estatística T')
plt.ylim(-5, 5)
plt.grid(axis='y')
plt.xticks(rotation=45)
plt.show()
