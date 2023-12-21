import dash
from dash import dcc, html
import plotly.graph_objects as go
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

# Load performance data
file_path = 'data/performance.csv'
df = pd.read_csv(file_path)

# Color real body based on close and open values
colors = ['red' if close < open else 'green' for close, open in zip(df['close'], df['open'])]

# Data for league stats
df_leagues = pd.read_excel('data/league_stats.xlsx')

# Format strings for display 
strings = {}
for i in range(len(df_leagues)):
    league = df_leagues.loc[i,'League']
    win = df_leagues.loc[i,'Win']
    loss = df_leagues.loc[i,'Loss']
    push = df_leagues.loc[i,'Push']
    winrate = df_leagues.loc[i,'Win%']
    earnings = df_leagues.loc[i,'Earnings']
    # earnings = '${:,.2f}'.format(earnings)
    str_name = f'str_{league}'
    if league == 'all':
        strings[str_name] = f'{win}-{loss}-{push} | {winrate} | {earnings}'
    else:
        strings[str_name] = f'{win}-{loss}-{push}'


# Create Dash app
app = dash.Dash(__name__)

server = app.server

# Define layout
app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.H1(children='SKYFOX'),

                html.H2(children=strings['str_all']),

                dcc.Graph(
                    id='candlestick-chart',
                    figure={
                        'data': [
                            go.Candlestick(
                                x=df['Date'],
                                open=df['open'],
                                high=df['high'],
                                low=df['low'],
                                close=df['close'],
                                increasing=dict(line=dict(color='green')),
                                decreasing=dict(line=dict(color='red')),
                                name='Candlesticks'
                            ),
                        ],
                        'layout': {
                            'title': 'Skyfox Fund Performance',
                            'xaxis': {'rangeslider': {'visible': False}},
                            # 'yaxis': {'title': 'Price'},
                            'height': 500,
                            'width': 1200,
                            # 'paper_bgcolor': '#1E1E1E',
                            # 'plot_bgcolor': '#1E1E1E',
                            # 'font': {'color': 'white'},
                        },
                    },
                    style={'backgroundColor': '#121212'}
                ),
                
                html.P(
                    children=[
                        html.Strong(children='NFL', style={'font-size': '1em'}),
                        html.Br(),
                        html.Span(strings['str_NFL']),
                        html.Br(),
                        html.Strong(children='MLB', style={'font-size': '1em'}),
                        html.Br(),
                        html.Span(strings['str_MLB']),
                        html.Br(),
                        html.Strong(children='NHL', style={'font-size': '1em'}),
                        html.Br(),
                        html.Span(strings['str_NHL']),
                        html.Br(),
                        html.Strong(children='NBA', style={'font-size': '1em'}),
                        html.Br(),
                        html.Span(strings['str_NBA']),
                        html.Br(),
                        html.Strong(children='WNBA', style={'font-size': '1em'}),
                        html.Br(),
                        html.Span(strings['str_WNBA']),
                        html.Br(),
                        html.Strong(children='CFB', style={'font-size': '1em'}),
                        html.Br(),
                        html.Span(strings['str_CFB']),
                        html.Br(),
                        html.Strong(children='CBB', style={'font-size': '1em'}),
                        html.Br(),
                        html.Span(strings['str_CBB']),
                    ],
                    style={'text-align': 'center', 'color': 'black', 'margin-top': '20px'}
                ),
            ]
        )
    ],
    style={'textAlign': 'center', 'margin': 'auto', 'width': '1200px'}
)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
