import plotly.graph_objects as go

def import_location_data():
    raw = []
    with open("location.txt", "r") as f:
        raw = f.readlines()
    
    time, lon, lat  = [], [], []
    temp_t, temp_lon, temp_lat = [], [], []
    colors, names = [], []

    for line in raw:
        s_line = line.split(" ")

        if line.strip().startswith("x"):
            time.append(temp_t)
            lon.append(temp_lon)
            lat.append(temp_lat)

            colors.append(generate_colors(int(s_line[1]), s_line[2]))
            names.append(s_line[3])

            temp_t = []
            temp_lon = []
            temp_lat = []

        else:
            temp_t.append(s_line[0])
            temp_lon.append(float(s_line[1]))
            temp_lat.append(float(s_line[2]))

    if len(temp_lat) > 0:
        time.append(temp_t)
        lon.append(temp_lon)
        lat.append(temp_lat)

        last = ["Green"]
        if len(temp_lat) - 2 > 0: last.append("Blue" * (len(temp_lat) - 2))
        if len(temp_lat) != 1: last.append("Red")
        colors.append(last)
    
    return time, lon, lat, colors, names

def generate_colors(num, color):
    colors = []
    for i in range(num):
        colors.append(color)
    return colors

def create_globe_plot():
    # Read in location data, and create colors for the markers
    time, lon, lat, colors, names = import_location_data()

    # Add location datapoints
    globe = go.Figure()
    for i in range(len(time)):
        globe.add_trace(go.Scattergeo(lat=lat[i], lon=lon[i], text=time[i], mode="markers+lines", marker=dict(color=colors[i])))
    globe.update_traces(marker_size=10, line=dict(color='Blue'))

    # Create the globe
    globe.update_geos(projection_type="orthographic", showcountries=True)
    globe.update_layout(margin={"r":100,"t":100,"l":100,"b":100})

    return globe