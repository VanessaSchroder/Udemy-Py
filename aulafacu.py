import pandas as pd

# lista de dados

dados = {
    " Alunos ": ['Matheus', 'Gabi', 'Thiago', 'Erik', 'Yan'],
    'P1': [8.0, 9.0, 10.0, 8.2 , 9.0],
    'P2': [8.0, 9.0, 10.0, 8.2 , 9.0]
    
}


#DataFrame
df = pd.DataFrame(dados)

#Calcular Média

df['Media'] = df [['P1', 'P2']].mean(axis=1)

df['Situacao'] = df ['Media'].apply(lambda x:'Aprovado' if x>=7 else 'Reprovado')

print(df)