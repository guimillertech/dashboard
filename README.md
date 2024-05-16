

# Evolução dos Status dos Serviços

Este repositório contém um exemplo de código em Python que cria um gráfico interativo usando `plotly` para visualizar a evolução dos status dos serviços ao longo do tempo. Este gráfico é útil para prestadores de serviço que desejam monitorar o progresso dos seus serviços em diferentes estados, como "Em Andamento", "Em Revisão", "Entregue", "Finalizado" e "Cancelado".

## Objetivo

O objetivo deste projeto é fornecer uma ferramenta visual para prestadores de serviço que utilizam o iServApp, um marketplace de serviços freelancers. A ferramenta permite monitorar a evolução dos serviços com base em diferentes status e oferece uma visão clara do desempenho e progresso ao longo do tempo.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para processar os dados e criar o gráfico.
- **Pandas**: Biblioteca utilizada para manipulação e análise de dados.
- **Plotly**: Biblioteca utilizada para criar gráficos interativos.

## Instalação

Para executar este projeto localmente, siga as etapas abaixo:

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/evolucao-status-servicos.git
   cd evolucao-status-servicos
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):

   ```bash
   python -m venv env
   source env/bin/activate   # No Windows, use `env\Scripts\activate`
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

   O arquivo `requirements.txt` deve conter:
   ```txt
   pandas
   plotly
   ```

## Uso

Execute o script `status_chart.py` para gerar o gráfico interativo:

```bash
python status_chart.py
```

### Exemplo de Código

O arquivo `status_chart.py` contém o seguinte código:

```python
import pandas as pd
import plotly.express as px

# Dados fictícios
data = {
    'date': pd.date_range(start='2023-01-01', periods=30, freq='D'),
    'status': ['Em Andamento', 'Em Revisão', 'Entregue', 'Finalizado', 'Cancelado'] * 6,
    'count': [5, 15, 25, 35, 45, 55, 10, 20, 30, 40, 50, 60, 15, 25, 35, 45, 55, 65, 20, 30, 40, 50, 60, 70, 25, 35, 45, 55, 65, 75]
}

df = pd.DataFrame(data)

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
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---
