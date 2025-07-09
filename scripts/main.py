import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load the datasets
locations_df = pd.read_csv("../data/uber_data_locations.csv")
counts_df = pd.read_csv("../data/uber_data_counts.csv")

# Create a subplot with 1 row and 2 columns, specifying types
fig = make_subplots(rows=1, cols=2,
                    specs=[[{'type': 'map'}, {'type': 'xy'}]],
                    subplot_titles=("Uber Pickups Locations by Hour", "Uber Pickups Count per Hour"))

# Add scatter map for locations
fig.add_trace(go.Scattermap(
    lat=locations_df['latitude'],
    lon=locations_df['longitude'],
    mode='markers',
    marker=dict(
        size=10,
        color=locations_df['hour'],
        colorscale='Viridis',
        showscale=True,
        colorbar=dict(title='Hour')
    ),
    text=locations_df['date'].astype(str) + ', Hour: ' + locations_df['hour'].astype(str),
    hoverinfo='text'
), row=1, col=1)

# Add bar chart for counts
fig.add_trace(go.Bar(
    x=counts_df['hour'],
    y=counts_df['count']
), row=1, col=2)

# Update map layout
fig.update_layout(
    map1=dict(
        style="open-street-map",
        center=dict(lat=40.7, lon=-74),
        zoom=10
    ),
    height=600,
    width=1200,
    title_text="Uber Data Dashboards"
)

# Save the combined dashboard to a single HTML file
fig.write_html("uber_combined_dashboard.html")