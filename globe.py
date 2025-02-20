import plotly.graph_objects as go
from IPython.display import display, clear_output
from threading import Timer

def import_location_data():
    time, lon, lat = [], [], []
    with open("location.txt", "r") as f:
        for line in f:
            data = line.split(" ")
            time.append(data[0])
            lon.append(float(data[1]))
            lat.append(float(data[2]))
    
    return time, lon, lat

def create_globe_plot():
    # Read in location data, and create colors for the markers
    time, lon, lat = import_location_data()
    colors = ['Green'] + ['Blue'] * (len(lon) - 2) + ['Red']

    # Add location datapoints
    globe = go.Figure(go.Scattergeo(lat=lat, lon=lon, text=time, mode="markers+lines", marker=dict(color=colors)))
    globe.update_traces(marker_size=10, line=dict(color='Blue'))

    # Create the globe
    globe.update_geos(projection_type="orthographic")
    globe.update_layout(margin={"r":100,"t":100,"l":100,"b":100})

    return globe

create_globe_plot().show()