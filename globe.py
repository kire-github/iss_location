import plotly.graph_objects as go

def import_location_data():
    with open("location.txt", "r") as f:
        raw_lines = f.readlines()
    
    time, lon, lat  = [], [], []
    colors, line_colors, names = [], [], []

    temp_t, temp_lon, temp_lat = [], [], []

    def finalize(line, marker, name):
        time.append(temp_t)
        lon.append(temp_lon)
        lat.append(temp_lat)

        line_colors.append(line)
        colors.append(marker)
        names.append(name)

    for line in raw_lines:
        s_line = line.strip().split(" ")

        if line.strip().startswith("x"):
            finalize(s_line[2], generate_colors(int(s_line[1]), s_line[2]), s_line[3])
            temp_t, temp_lon, temp_lat = [], [], []

        else:
            temp_t.append(s_line[0])
            temp_lon.append(float(s_line[1]))
            temp_lat.append(float(s_line[2]))

    if len(temp_lat) > 0:
        last = []
        if len(temp_lat) - 2 > 0: last = ["Blue"] * (len(temp_lat) - 2)
        last.insert(0, "Green")
        if len(temp_lat) != 1: last.append("Red")

        finalize("Blue", last, "Current")
    
    return time, lon, lat, colors, line_colors, names

def generate_colors(num, color):
    colors = []
    for i in range(num):
        colors.append(color)
    return colors

def create_globe_plot():
    # Read in location data, and create colors for the markers
    time, lon, lat, colors, line_colors, names = import_location_data()

    # Add location datapoints
    globe = go.Figure()
    for i in range(len(time)):
        globe.add_trace(go.Scattergeo(lat=lat[i], lon=lon[i], text=time[i], mode="markers+lines", marker=dict(color=colors[i]), name=names[i], line=dict(color=line_colors[i]), marker_size=10))

    # Create the globe
    globe.update_geos(projection_type="orthographic", showcountries=True)
    globe.update_layout(margin={"r":100,"t":100,"l":100,"b":100})

    return globe