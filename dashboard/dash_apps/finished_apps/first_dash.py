import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

from django_plotly_dash import DjangoDash

# example
df = pd.DataFrame({
    "Categories": ["A", "B", "C"],
    "Values": [100, 200, 300]
})

fig = px.bar(df, x="Categories", y="Values", title="My first dash app.")
fig.update_layout(
    height=600,
    width=1000  
)
# for starting the app
app = DjangoDash('FirstDashApp', serve_locally= False)

app.layout = html.Div(
    style={'width': '100%', 'height': '100%', 'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center'},
    children=[
        html.H1("Dash entegration with MMRecVis!"),
        dcc.Graph(
            figure=fig,
            style={'width': '90vw', 'height': '80vh'}  
        )
    ]
)
