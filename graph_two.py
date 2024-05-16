import pandas as pd
import plotly.express as px

# Dados fictícios
data = {
    'date': pd.date_range(start='2023-01-01', periods=30, freq='D'),
    'status': ['Em Andamento', 'Em Revisão', 'Entregue', 'Finalizado', 'Cancelado'] * 6,
    'count': [5, 15, 7, 35, 10, 55, 10, 20, 30, 40, 50, 60, 15, 25, 35, 45, 55, 65, 20, 30, 40, 50, 60, 70, 25, 35, 45, 55, 65, 75]
}

df = pd.DataFrame(data)

# Verifique os dados
print(df.head())

# Cria o gráfico interativo com todos os status em uma única linha do tempo
fig = px.line(df, x='date', y='count', color='status', title='Evolução dos Status dos Serviços')

# Atualize o layout da figura
fig.update_layout(
    xaxis_title='Data',
    yaxis_title='Quantidade',
    legend_title='Status'
)

# Mostre o gráfico
fig.show()
