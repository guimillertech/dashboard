import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Dados fictícios
data = {
    'date': pd.date_range(start='2023-01-01', periods=30, freq='D'),
    'status': ['Em Andamento', 'Em Revisão', 'Entregue', 'Finalizado', 'Cancelado'] * 6,
    'count': [5, 15, 25, 35, 45, 55, 10, 20, 30, 40, 50, 60, 15, 25, 35, 45, 55, 65, 20, 30, 40, 50, 60, 70, 25, 35, 45, 55, 65, 75]
}

df = pd.DataFrame(data)

# Verifique os dados
print(df.head())

# Cria uma figura de subplots para mostrar a evolução dos status
fig = make_subplots(rows=5, cols=1, shared_xaxes=True, subplot_titles=("Em Andamento", "Em Revisão", "Entregue", "Finalizado", "Cancelado"))

statuses = df['status'].unique()
for i, status in enumerate(statuses, start=1):
    filtered_df = df[df['status'] == status]
    fig.add_trace(
        go.Scatter(x=filtered_df['date'], y=filtered_df['count'], mode='lines+markers', name=status),
        row=i, col=1
    )

# Atualize o layout da figura
fig.update_layout(
    height=1000,
    title_text="Evolução dos Status dos Serviços",
    xaxis_title="Data",
    yaxis_title="Quantidade"
)

# Mostre o gráfico
fig.show()
