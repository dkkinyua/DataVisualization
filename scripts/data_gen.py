import numpy as np
import pandas as pd

# Rides data
rides_data = [
    {"state": "Alabama", "total_rides": 2600000, "hours": 720, "average_hourly_rides": np.round(2600000 / 720)},
    {"state": "Alaska", "total_rides": 800000, "hours": 720, "average_hourly_rides": np.round(800000 / 720)},
    {"state": "Arizona", "total_rides": 4100000, "hours": 720, "average_hourly_rides": np.round(4100000 / 720)},
    {"state": "Arkansas", "total_rides": 1900000, "hours": 720, "average_hourly_rides": np.round(1900000 / 720)},
    {"state": "California", "total_rides": 20500000, "hours": 720, "average_hourly_rides": np.round(20500000 / 720)},
    {"state": "Colorado", "total_rides": 3100000, "hours": 720, "average_hourly_rides": np.round(3100000 / 720)},
    {"state": "Connecticut", "total_rides": 2000000, "hours": 720, "average_hourly_rides": np.round(2000000 / 720)},
    {"state": "Delaware", "total_rides": 1000000, "hours": 720, "average_hourly_rides": np.round(1000000 / 720)},
    {"state": "Florida", "total_rides": 11200000, "hours": 720, "average_hourly_rides": np.round(11200000 / 720)},
    {"state": "Georgia", "total_rides": 5600000, "hours": 720, "average_hourly_rides": np.round(5600000 / 720)},
    {"state": "Hawaii", "total_rides": 900000, "hours": 720, "average_hourly_rides": np.round(900000 / 720)},
    {"state": "Idaho", "total_rides": 1100000, "hours": 720, "average_hourly_rides": np.round(1100000 / 720)},
    {"state": "Illinois", "total_rides": 6700000, "hours": 720, "average_hourly_rides": np.round(6700000 / 720)},
    {"state": "Indiana", "total_rides": 3600000, "hours": 720, "average_hourly_rides": np.round(3600000 / 720)},
    {"state": "Iowa", "total_rides": 1800000, "hours": 720, "average_hourly_rides": np.round(1800000 / 720)},
    {"state": "Kansas", "total_rides": 1600000, "hours": 720, "average_hourly_rides": np.round(1600000 / 720)},
    {"state": "Kentucky", "total_rides": 2400000, "hours": 720, "average_hourly_rides": np.round(2400000 / 720)},
    {"state": "Louisiana", "total_rides": 2500000, "hours": 720, "average_hourly_rides": np.round(2500000 / 720)},
    {"state": "Maine", "total_rides": 700000, "hours": 720, "average_hourly_rides": np.round(700000 / 720)},
    {"state": "Maryland", "total_rides": 3200000, "hours": 720, "average_hourly_rides": np.round(3200000 / 720)},
    {"state": "Massachusetts", "total_rides": 3700000, "hours": 720, "average_hourly_rides": np.round(3700000 / 720)},
    {"state": "Michigan", "total_rides": 5100000, "hours": 720, "average_hourly_rides": np.round(5100000 / 720)},
    {"state": "Minnesota", "total_rides": 3000000, "hours": 720, "average_hourly_rides": np.round(3000000 / 720)},
    {"state": "Mississippi", "total_rides": 1600000, "hours": 720, "average_hourly_rides": np.round(1600000 / 720)},
    {"state": "Missouri", "total_rides": 3200000, "hours": 720, "average_hourly_rides": np.round(3200000 / 720)},
    {"state": "Montana", "total_rides": 600000, "hours": 720, "average_hourly_rides": np.round(600000 / 720)},
    {"state": "Nebraska", "total_rides": 1000000, "hours": 720, "average_hourly_rides": np.round(1000000 / 720)},
    {"state": "Nevada", "total_rides": 1700000, "hours": 720, "average_hourly_rides": np.round(1700000 / 720)},
    {"state": "New Hampshire", "total_rides": 700000, "hours": 720, "average_hourly_rides": np.round(700000 / 720)},
    {"state": "New Jersey", "total_rides": 4800000, "hours": 720, "average_hourly_rides": np.round(4800000 / 720)},
    {"state": "New Mexico", "total_rides": 1100000, "hours": 720, "average_hourly_rides": np.round(1100000 / 720)},
    {"state": "New York", "total_rides": 10200000, "hours": 720, "average_hourly_rides": np.round(10200000 / 720)},
    {"state": "North Carolina", "total_rides": 5500000, "hours": 720, "average_hourly_rides": np.round(5500000 / 720)},
    {"state": "North Dakota", "total_rides": 400000, "hours": 720, "average_hourly_rides": np.round(400000 / 720)},
    {"state": "Ohio", "total_rides": 6100000, "hours": 720, "average_hourly_rides": np.round(6100000 / 720)},
    {"state": "Oklahoma", "total_rides": 2100000, "hours": 720, "average_hourly_rides": np.round(2100000 / 720)},
    {"state": "Oregon", "total_rides": 2300000, "hours": 720, "average_hourly_rides": np.round(2300000 / 720)},
    {"state": "Pennsylvania", "total_rides": 6700000, "hours": 720, "average_hourly_rides": np.round(6700000 / 720)},
    {"state": "Rhode Island", "total_rides": 600000, "hours": 720, "average_hourly_rides": np.round(600000 / 720)},
    {"state": "South Carolina", "total_rides": 2700000, "hours": 720, "average_hourly_rides": np.round(2700000 / 720)},
    {"state": "South Dakota", "total_rides": 500000, "hours": 720, "average_hourly_rides": np.round(500000 / 720)},
    {"state": "Tennessee", "total_rides": 3600000, "hours": 720, "average_hourly_rides": np.round(3600000 / 720)},
    {"state": "Texas", "total_rides": 15200000, "hours": 720, "average_hourly_rides": np.round(15200000 / 720)},
    {"state": "Utah", "total_rides": 1700000, "hours": 720, "average_hourly_rides": np.round(1700000 / 720)},
    {"state": "Vermont", "total_rides": 300000, "hours": 720, "average_hourly_rides": np.round(300000 / 720)},
    {"state": "Virginia", "total_rides": 4500000, "hours": 720, "average_hourly_rides": np.round(4500000 / 720)},
    {"state": "Washington", "total_rides": 4000000, "hours": 720, "average_hourly_rides": np.round(4000000 / 720)},
    {"state": "West Virginia", "total_rides": 900000, "hours": 720, "average_hourly_rides": np.round(900000 / 720)},
    {"state": "Wisconsin", "total_rides": 3000000, "hours": 720, "average_hourly_rides": np.round(3000000 / 720)},
    {"state": "Wyoming", "total_rides": 300000, "hours": 720, "average_hourly_rides": np.round(300000 / 720)},
]

# State abbreviations mapping
state_abbrev = {
    "Alabama": "AL", "Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR", "California": "CA",
    "Colorado": "CO", "Connecticut": "CT", "Delaware": "DE", "Florida": "FL", "Georgia": "GA",
    "Hawaii": "HI", "Idaho": "ID", "Illinois": "IL", "Indiana": "IN", "Iowa": "IA",
    "Kansas": "KS", "Kentucky": "KY", "Louisiana": "LA", "Maine": "ME", "Maryland": "MD",
    "Massachusetts": "MA", "Michigan": "MI", "Minnesota": "MN", "Mississippi": "MS", "Missouri": "MO",
    "Montana": "MT", "Nebraska": "NE", "Nevada": "NV", "New Hampshire": "NH", "New Jersey": "NJ",
    "New Mexico": "NM", "New York": "NY", "North Carolina": "NC", "North Dakota": "ND", "Ohio": "OH",
    "Oklahoma": "OK", "Oregon": "OR", "Pennsylvania": "PA", "Rhode Island": "RI", "South Carolina": "SC",
    "South Dakota": "SD", "Tennessee": "TN", "Texas": "TX", "Utah": "UT", "Vermont": "VT",
    "Virginia": "VA", "Washington": "WA", "West Virginia": "WV", "Wisconsin": "WI", "Wyoming": "WY"
}

# State coordinates
state_coords = {
    "Alabama": {"lat": 32.806671, "lon": -86.79113}, "Alaska": {"lat": 61.370716, "lon": -152.404419},
    "Arizona": {"lat": 33.729759, "lon": -111.431221}, "Arkansas": {"lat": 34.969704, "lon": -92.373123},
    "California": {"lat": 36.116203, "lon": -119.681564}, "Colorado": {"lat": 39.059811, "lon": -105.311104},
    "Connecticut": {"lat": 41.597782, "lon": -72.755371}, "Delaware": {"lat": 39.318523, "lon": -75.507141},
    "Florida": {"lat": 27.766279, "lon": -81.686783}, "Georgia": {"lat": 33.040619, "lon": -83.643074},
    "Hawaii": {"lat": 21.094318, "lon": -157.498337}, "Idaho": {"lat": 44.240459, "lon": -114.478828},
    "Illinois": {"lat": 40.349457, "lon": -88.986137}, "Indiana": {"lat": 39.849426, "lon": -86.258278},
    "Iowa": {"lat": 42.011539, "lon": -93.210526}, "Kansas": {"lat": 38.526600, "lon": -96.726486},
    "Kentucky": {"lat": 37.668140, "lon": -84.670067}, "Louisiana": {"lat": 31.169546, "lon": -91.867805},
    "Maine": {"lat": 44.323535, "lon": -69.765261}, "Maryland": {"lat": 39.063946, "lon": -76.802101},
    "Massachusetts": {"lat": 42.230171, "lon": -71.530106}, "Michigan": {"lat": 43.326618, "lon": -84.536095},
    "Minnesota": {"lat": 45.694454, "lon": -93.900192}, "Mississippi": {"lat": 32.741646, "lon": -89.678696},
    "Missouri": {"lat": 38.572954, "lon": -92.189283}, "Montana": {"lat": 47.052952, "lon": -109.633040},
    "Nebraska": {"lat": 41.492537, "lon": -99.901813}, "Nevada": {"lat": 38.313515, "lon": -117.055374},
    "New Hampshire": {"lat": 43.452492, "lon": -71.563896}, "New Jersey": {"lat": 40.298904, "lon": -74.521011},
    "New Mexico": {"lat": 34.840515, "lon": -106.248482}, "New York": {"lat": 42.165726, "lon": -74.948051},
    "North Carolina": {"lat": 35.630066, "lon": -79.806419}, "North Dakota": {"lat": 47.528912, "lon": -99.784012},
    "Ohio": {"lat": 40.388783, "lon": -82.764915}, "Oklahoma": {"lat": 35.565342, "lon": -96.928917},
    "Oregon": {"lat": 44.572021, "lon": -122.070938}, "Pennsylvania": {"lat": 40.590752, "lon": -77.209755},
    "Rhode Island": {"lat": 41.680893, "lon": -71.51178}, "South Carolina": {"lat": 33.856892, "lon": -80.945007},
    "South Dakota": {"lat": 44.299782, "lon": -99.438828}, "Tennessee": {"lat": 35.747845, "lon": -86.692345},
    "Texas": {"lat": 31.054487, "lon": -97.563461}, "Utah": {"lat": 40.150032, "lon": -111.862434},
    "Vermont": {"lat": 44.045876, "lon": -72.710686}, "Virginia": {"lat": 37.769337, "lon": -78.169968},
    "Washington": {"lat": 47.400902, "lon": -121.490494}, "West Virginia": {"lat": 38.491226, "lon": -80.954570},
    "Wisconsin": {"lat": 44.268543, "lon": -89.616508}, "Wyoming": {"lat": 42.755966, "lon": -107.302490}
}

# Create DataFrame
df = pd.DataFrame(rides_data)

# Add state abbreviations
df['state_abbrev'] = df['state'].map(state_abbrev)

# Create DataFrame for coordinates
coords_data = [
    {"state": state, "state_abbrev": state_abbrev[state], "lat": coords["lat"], "lon": coords["lon"]}
    for state, coords in state_coords.items()
]
coords_df = pd.DataFrame(coords_data)

# Save to CSV files
df.to_csv('rides_data.csv', index=False)
coords_df.to_csv('state_coordinates.csv', index=False)