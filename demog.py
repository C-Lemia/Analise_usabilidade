import pandas as pd
import numpy as np
import os
import openpyxl

def criar_dados_demograficos():
    n_participantes = 30
    idades = np.random.randint(25, 66, size=n_participantes)
    phototipos = np.random.choice(['I', 'II', 'III', 'IV', 'V', 'VI'], size=n_participantes)
    generos = np.random.choice(['Masculino', 'Feminino'], size=n_participantes)
    tipos_cabelo = np.random.choice(['Liso', 'Ondulado', 'Cacheado', 'Crespo'], size=n_participantes)
    codigos = [f'P{i+1}' for i in range(n_participantes)]

    # Criar DataFrame demográfico
    df_demografico = pd.DataFrame({
        'Codigo': codigos,
        'Idade': idades,
        'Phototipo': phototipos,
        'Genero': generos,
        'Tipo_Cabelo': tipos_cabelo
    })
    return df_demografico

def criar_dados_teste():
    n_participantes = 30
    np.random.seed(60)
    dias = ['D0', 'D14', 'D28']
    oleosidade = np.random.uniform(0, 50, size=(n_participantes, 3))
    porosidade = np.random.uniform(0, 50, size=(n_participantes, 3))
    hidratacao = np.random.uniform(0, 50, size=(n_participantes, 3))
    codigos = [f'P{i+1}' for i in range(n_participantes)]

    # Criar DataFrame com os resultados dos testes
    df_teste = pd.DataFrame({
        'Codigo': np.repeat(codigos, len(dias)),
        'Dia': np.tile(dias, n_participantes),
        'Oleosidade': oleosidade.flatten(),
        'Porosidade': porosidade.flatten(),
        'Hidratacao': hidratacao.flatten()
    })
    
    # Reorganizar o DataFrame para ter colunas para cada dia
    df_comparacao = df_teste.pivot(index='Codigo', columns='Dia', values=['Oleosidade', 'Porosidade', 'Hidratacao'])
    df_comparacao.columns = ['_'.join(col).strip() for col in df_comparacao.columns.values]  # Ajustar o nome das colunas
    return df_comparacao

# Unir os dados demográficos com os dados de teste para gerar o arquivo final conforme solicitado

# Primeiro criar os dados demográficos e de teste
df_demografico = criar_dados_demograficos()
df_comparacao = criar_dados_teste()

# Unir os DataFrames de demográficos e comparação para ter uma visão única com todas as colunas
df_final = pd.merge(df_demografico, df_comparacao, on='Codigo')

# Verificar se o caminho existe, caso contrário, criar o diretório
caminho_excel_final = r"C:\Users\camil\OneDrive\Área de Trabalho\Estudos TI\analisecl\comparacao_teste_completa.xlsx"
diretorio = os.path.dirname(caminho_excel_final)

if not os.path.exists(diretorio):
    os.makedirs(diretorio)

# Tentar salvar o arquivo Excel e capturar qualquer erro
try:
    df_final.to_excel(caminho_excel_final, index=False, engine='openpyxl')  # Usar engine openpyxl
    print(f"Arquivo salvo com sucesso em: {caminho_excel_final}")
except Exception as e:
    print(f"Erro ao salvar o arquivo: {e}")

# Exibir os primeiros dados para verificação
print(df_final.head())