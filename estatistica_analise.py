import pandas as pd
import numpy as np
from scipy import stats
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

# Exibir as diferenças por participante
print("Diferenças por Participante:")
print(df_teste[['Codigo', 'Diferença_Oleosidade', 'Diferença_Porosidade', 'Diferença_Hidratação']])


# Realizar o teste t pareado para oleosidade
t_stat_oleosidade, p_value_oleosidade = stats.ttest_rel(oleosidade_d0, oleosidade_d28)

# Realizar o teste t pareado para porosidade
t_stat_porosidade, p_value_porosidade = stats.ttest_rel(porosidade_d0, porosidade_d28)

# Realizar o teste t pareado para hidratação
t_stat_hidratacao, p_value_hidratacao = stats.ttest_rel(hidratacao_d0, hidratacao_d28)

# Compilar os resultados
resultados = {
    'Métrica': ['Oleosidade', 'Porosidade', 'Hidratação'],
    'Estatística T': [t_stat_oleosidade, t_stat_porosidade, t_stat_hidratacao],
    'P-Valor': [p_value_oleosidade, p_value_porosidade, p_value_hidratacao],
    'Significativo': [p_value_oleosidade < 0.05, p_value_porosidade < 0.05, p_value_hidratacao < 0.05]
}

df_resultados = pd.DataFrame(resultados)

# Exibir os resultados estatísticos
print("\nResultados Estatísticos:")
print(df_resultados)


##############


