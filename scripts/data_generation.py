import json
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

# Load DataFrames from CSV files
df = pd.read_csv('../data/rides_data.csv')
coords_df = pd.read_csv('../data/state_coordinates.csv')

# Merge rides data with coordinates on state_abbrev
df = df.merge(coords_df[['state_abbrev', 'lat', 'lon']], on='state_abbrev', how='left')

# Dashboard 1: Choropleth Map
fig_map = px.choropleth(
    df,
    locations='state_abbrev',
    color='total_rides',
    locationmode='USA-states',
    scope="usa",
    title='Total Rides by State - Interactive Choropleth Map',
    color_continuous_scale='Viridis',
    hover_name='state',
    hover_data={
        'total_rides': ':,',
        'average_hourly_rides': ':,',
        'state_abbrev': False
    },
    labels={'total_rides': 'Total Rides', 'average_hourly_rides': 'Avg Hourly Rides'}
)

fig_map.update_layout(
    title_font_size=20,
    title_x=0.5,
    geo=dict(
        showframe=False,
        showcoastlines=True,
        projection_type='albers usa'
    ),
    height=600,
    width=1000
)

# Dashboard 2: Interactive Histogram with additional features
fig_hist = px.histogram(
    df,
    x='total_rides',
    nbins=20,
    title='Distribution of Total Rides Across States',
    labels={'total_rides': 'Total Rides', 'count': 'Number of States'},
    color_discrete_sequence=['#636EFA']
)

fig_hist.update_layout(
    title_font_size=20,
    title_x=0.5,
    xaxis_title='Total Rides',
    yaxis_title='Number of States',
    showlegend=False,
    height=500,
    width=800
)

# Add hover information to histogram
fig_hist.update_traces(
    hovertemplate='<b>Range:</b> %{x}<br><b>Number of States:</b> %{y}<extra></extra>'
)

# Create a combined dashboard with subplots
fig_combined = make_subplots(
    rows=2, cols=1,
    row_heights=[0.7, 0.3],
    subplot_titles=('Total Rides by State - Choropleth Map', 'Distribution of Total Rides'),
    specs=[[{"type": "geo"}], [{"type": "xy"}]]
)

# Add choropleth to subplot
fig_combined.add_trace(
    go.Choropleth(
        locations=df['state_abbrev'],
        z=df['total_rides'],
        locationmode='USA-states',
        colorscale='Viridis',
        text=df['state'],
        hovertemplate='<b>%{text}</b><br>Total Rides: %{z:,}<extra></extra>',
        colorbar=dict(title="Total Rides", len=0.5, y=0.8)
    ),
    row=1, col=1
)

# Add histogram to subplot
fig_combined.add_trace(
    go.Histogram(
        x=df['total_rides'],
        nbinsx=20,
        name='States',
        marker_color='#636EFA',
        hovertemplate='<b>Range:</b> %{x}<br><b>Number of States:</b> %{y}<extra></extra>'
    ),
    row=2, col=1
)

fig_combined.update_layout(
    title_text="US Rides Data Interactive Dashboard",
    title_font_size=24,
    title_x=0.5,
    height=1000,
    showlegend=False
)

fig_combined.update_geos(
    showframe=False,
    showcoastlines=True,
    projection_type='albers usa',
    scope="usa"
)

fig_combined.update_xaxes(title_text="Total Rides", row=2, col=1)
fig_combined.update_yaxes(title_text="Number of States", row=2, col=1)

# Create a comprehensive 4-panel dashboard
fig_full_dashboard = make_subplots(
    rows=2, cols=2,
    subplot_titles=(
        'Total Rides by State - Choropleth Map',
        'Geographic Distribution - Scatter Plot',
        'Distribution of Total Rides - Histogram',
        'Top 10 States by Total Rides - Bar Chart'
    ),
    specs=[
        [{"type": "geo", "colspan": 1}, {"type": "geo", "colspan": 1}],
        [{"type": "xy", "colspan": 1}, {"type": "xy", "colspan": 1}]
    ],
    horizontal_spacing=0.1,
    vertical_spacing=0.15
)

# Add choropleth map
fig_full_dashboard.add_trace(
    go.Choropleth(
        locations=df['state_abbrev'],
        z=df['total_rides'],
        locationmode='USA-states',
        colorscale='Viridis',
        text=df['state'],
        hovertemplate='<b>%{text}</b><br>Total Rides: %{z:,}<extra></extra>',
        showscale=False,
        name='Choropleth'
    ),
    row=1, col=1
)

# Add scatter geo plot
fig_full_dashboard.add_trace(
    go.Scattergeo(
        lon=df['lon'],
        lat=df['lat'],
        text=df['state'],
        mode='markers',
        marker=dict(
            size=df['total_rides']/500000,
            color=df['total_rides'],
            colorscale='Plasma',
            sizemode='diameter',
            sizemin=4,
            line=dict(width=1, color='#ffffff'),
            colorbar=dict(
                title="Total Rides", 
                x=1.02, 
                len=0.4, 
                y=0.75,
                # titlefont=dict(color='#ffffff'),
                tickfont=dict(color='#ffffff')
            )
        ),
        hovertemplate='<b>%{text}</b><br>Total Rides: %{marker.color:,}<extra></extra>',
        name='Scatter'
    ),
    row=1, col=2
)

# Add histogram with dark theme colors
fig_full_dashboard.add_trace(
    go.Histogram(
        x=df['total_rides'],
        nbinsx=15,
        name='Distribution',
        marker_color='#00d4ff',
        marker_line_color='#ffffff',
        marker_line_width=1,
        hovertemplate='<b>Range:</b> %{x}<br><b>Count:</b> %{y}<extra></extra>'
    ),
    row=2, col=1
)

# Add bar chart for top 10 states with dark theme colors
top_10_df = df.nlargest(10, 'total_rides')
fig_full_dashboard.add_trace(
    go.Bar(
        x=top_10_df['total_rides'],
        y=top_10_df['state'],
        orientation='h',
        name='Top 10',
        marker_color='#ff6b6b',
        marker_line_color='#ffffff',
        marker_line_width=1,
        hovertemplate='<b>%{y}</b><br>Total Rides: %{x:,}<extra></extra>'
    ),
    row=2, col=2
)

# Update layout for the full dashboard with dark theme
fig_full_dashboard.update_layout(
    title_text="US Rides Data - Comprehensive Interactive Dashboard",
    title_font_size=24,
    title_x=0.5,
    height=1000,
    width=1600,
    showlegend=False,
    template="plotly_dark",
    paper_bgcolor='#1e1e1e',
    plot_bgcolor='#2d2d2d',
    font=dict(color='#ffffff', family="Arial, sans-serif"),
    title_font_color='#ffffff'
)

# Update geo subplots with dark theme
fig_full_dashboard.update_geos(
    showframe=False,
    showcoastlines=True,
    projection_type='albers usa',
    scope="usa",
    bgcolor='#2d2d2d',
    showland=True,
    landcolor='#3a3a3a',
    showocean=True,
    oceancolor='#1a1a1a',
    showcountries=True,
    countrycolor='#555555'
)

# Update axes with dark theme styling
fig_full_dashboard.update_xaxes(
    title_text="Total Rides", 
    row=2, col=1,
    gridcolor='#444444',
    zerolinecolor='#666666',
    title_font_color='#ffffff'
)
fig_full_dashboard.update_yaxes(
    title_text="Number of States", 
    row=2, col=1,
    gridcolor='#444444',
    zerolinecolor='#666666',
    title_font_color='#ffffff'
)
fig_full_dashboard.update_xaxes(
    title_text="Total Rides", 
    row=2, col=2,
    gridcolor='#444444',
    zerolinecolor='#666666',
    title_font_color='#ffffff'
)
fig_full_dashboard.update_yaxes(
    title_text="State", 
    row=2, col=2,
    gridcolor='#444444',
    zerolinecolor='#666666',
    title_font_color='#ffffff'
)

# Save single comprehensive dashboard
def save_dashboard():
    fig_full_dashboard.write_html("../output/rides_comprehensive_dashboard.html")

# Additional interactive scatter plot with state coordinates (bonus visualization)
fig_scatter = px.scatter_geo(
    df,
    lat='lat',
    lon='lon',
    color='total_rides',
    size='total_rides',
    hover_name='state',
    hover_data={
        'total_rides': ':,',
        'average_hourly_rides': ':,',
        'lat': False,
        'lon': False
    },
    title='Total Rides by State - Geographic Scatter Plot',
    size_max=50,
    scope='usa',
    color_continuous_scale='Plasma'
)

fig_scatter.update_layout(
    title_font_size=20,
    title_x=0.5,
    height=600,
    width=1000
)

# Execute the save function
if __name__ == "__main__":
    save_dashboard()