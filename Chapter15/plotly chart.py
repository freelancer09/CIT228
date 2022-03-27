import plotly.graph_objects as go
from plotly import offline

men = [37.9,46.5,37.6,25.6]
women = [35.4,43.3,37.8,22.7]
total=[36.6,44.9,37.7,24.1]
age_range=["Over 20","20-39","40-59","Over 60"]

fig = go.Figure()
fig.add_trace(go.Bar(
    x=age_range,
    y=men,
    name='Men',
    marker_color='green'
))
fig.add_trace(go.Bar(
    x=age_range,
    y=women,
    name='Women',
    marker_color='red'
))
fig.add_trace(go.Bar(
    x=age_range,
    y=total,
    name='Total',
    marker_color='blue'
))

layout=fig.update_layout(
    title='Fast Food Consumption Per Day',
    title_font_color='blue',
    title_font_size=20,
    xaxis_tickfont_size=14,
    yaxis=dict(
        title='Percentages',
        titlefont_size=16,
        tickfont_size=14,
    ),
    xaxis=dict(
        title='2013-2016',
        titlefont_size=16,
        tickfont_size=14, 
    ),    
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15,
    bargroupgap=0.1
)

offline.plot({'data': fig, 'layout':layout}, filename='plotly.html')