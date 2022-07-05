'''

    Esse programa foi desenvolvido como solução para o desafio apresentado pela empresa ATX
    AUTOMATION.
    O código funciona de maneira totalmente automática, podendo alterar a tabela sem a
    necessidade de alterar o código em si. Fique a vontade para adicionar mais pessoas e
    culinária na tabela.

    Desenvolvido por Gustavo Yoshimi Yamashita

'''

import pandas as pd

# Lendo o arquivo excell
df = pd.read_excel("tabela.xlsx")

lista_culinaria = []

# Descobrindo e Separando os grupos de comida
for x in range(len(df)):
    nome = df['Culinária_preferida'][x]
    if not(nome in lista_culinaria):
        lista_culinaria.append(nome)
print(f"Existe esses gostos culinários nessa tabela: {lista_culinaria}")

soma = 0
media = 0
list_idade = []

# Separando o grupo de pessoas automaticamente e calculando a média
for x in range(len(lista_culinaria)):
    print("//////////////////////////////////////////\n")
    print(f"Iniciando: {lista_culinaria[x]}")

    # Criando uma nova tabela de acordo o tipo de gosto culinário
    df_mask = df['Culinária_preferida'] == lista_culinaria[x]
    df_filtrada= df[df_mask]
    print(df_filtrada)

    # Calculando a média
    soma = 0
    for y in range(len(df_filtrada)):
        idade = df_filtrada['Idades'].iloc[y]
        soma += idade
    media = soma / (len(df_filtrada))
    print(f"Média das idades: {media}\n")

# Outras informações
print("Outras informações...")
print(f"Número de pessoas na tabela: {len(df)}")
print(f"Número de gostos na tabela: {len(lista_culinaria)}")
print(f"Gostos existentes: {lista_culinaria}")


