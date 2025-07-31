from django_plotly_dash import DjangoDash
from dash import dcc, html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import pandas as pd
import os

app = DjangoDash("AdvancedDashApp")

mapbox_access_token = "pk.eyJ1IjoicGxvdGx5bWFwYm94IiwiYSI6ImNrOWJqb2F4djBnMjEzbG50amg0dnJieG4ifQ.Zme1-Uzoi75IaFbieBDl3A"

state_map = {
    "NY": "New York",
    "CA": "California"
   
}

state_list = list(state_map.keys())

data_dict = {}
for state in state_list:
    csv_path = os.path.join("dashboard", "data", "processed", f"df_{state}_lat_lon.csv")
    state_data = pd.read_csv(csv_path)
    data_dict[state] = state_data


app.layout = html.Div([
    html.H2("🧠 Medical Provider Charges (Advanced Dash App)"),
    
    html.Div([
        html.Label("Select State:"),
        dcc.Dropdown(
            id='state-select',
            options=[{'label': s, 'value': s} for s in state_list],
            value='NY'
        )
    ], style={'width': '30%', 'margin-bottom': '20px'}),

    dcc.Graph(id='basic-map'),
])


@app.callback(
    Output("basic-map", "figure"),
    Input("state-select", "value")
)
def update_map(state):
    if state not in data_dict:
        return go.Figure()  
    
    df = data_dict[state]
    df = df.dropna(subset=['lat', 'lon'])  

    fig = go.Figure(go.Scattermapbox(
        lat=df["lat"],
        lon=df["lon"],
        mode="markers",
        marker=dict(size=8, color='blue'),
        text=df["Provider Name"]
    ))

    fig.update_layout(
        mapbox=dict(
            accesstoken=mapbox_access_token,
            center={"lat": df["lat"].mean(), "lon": df["lon"].mean()},
            zoom=5,
            style="light"
        ),
        margin={"r": 0, "t": 0, "l": 0, "b": 0}
    )

    return fig
