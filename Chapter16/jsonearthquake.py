import json
import plotly.graph_objects as go
from plotly import offline

filename = 'march2022.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

fig = go.Figure()
fig.add_trace(go.Scattergeo(
    lon=lons,
    lat=lats,
    hovertext=mag
))
layout = fig.update_layout(
    title='Global Earthquakes March 2022'
)
offline.plot({'data': fig, 'layout':layout}, filename='march2022.html')