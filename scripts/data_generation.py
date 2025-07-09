import json

rides_data = [
    {"state": "Alabama", "total_rides": 2600000},
    {"state": "Alaska", "total_rides": 800000},
    {"state": "Arizona", "total_rides": 4100000},
    {"state": "Arkansas", "total_rides": 1900000},
    {"state": "California", "total_rides": 20500000},
    {"state": "Colorado", "total_rides": 3100000},
    {"state": "Connecticut", "total_rides": 2000000},
    {"state": "Delaware", "total_rides": 1000000},
    {"state": "Florida", "total_rides": 11200000},
    {"state": "Georgia", "total_rides": 5600000},
    {"state": "Hawaii", "total_rides": 900000},
    {"state": "Idaho", "total_rides": 1100000},
    {"state": "Illinois", "total_rides": 6700000},
    {"state": "Indiana", "total_rides": 3600000},
    {"state": "Iowa", "total_rides": 1800000},
    {"state": "Kansas", "total_rides": 1600000},
    {"state": "Kentucky", "total_rides": 2400000},
    {"state": "Louisiana", "total_rides": 2500000},
    {"state": "Maine", "total_rides": 700000},
    {"state": "Maryland", "total_rides": 3200000},
    {"state": "Massachusetts", "total_rides": 3700000},
    {"state": "Michigan", "total_rides": 5100000},
    {"state": "Minnesota", "total_rides": 3000000},
    {"state": "Mississippi", "total_rides": 1600000},
    {"state": "Missouri", "total_rides": 3200000},
    {"state": "Montana", "total_rides": 600000},
    {"state": "Nebraska", "total_rides": 1000000},
    {"state": "Nevada", "total_rides": 1700000},
    {"state": "New Hampshire", "total_rides": 700000},
    {"state": "New Jersey", "total_rides": 4800000},
    {"state": "New Mexico", "total_rides": 1100000},
    {"state": "New York", "total_rides": 10200000},
    {"state": "North Carolina", "total_rides": 5500000},
    {"state": "North Dakota", "total_rides": 400000},
    {"state": "Ohio", "total_rides": 6100000},
    {"state": "Oklahoma", "total_rides": 2100000},
    {"state": "Oregon", "total_rides": 2300000},
    {"state": "Pennsylvania", "total_rides": 6700000},
    {"state": "Rhode Island", "total_rides": 600000},
    {"state": "South Carolina", "total_rides": 2700000},
    {"state": "South Dakota", "total_rides": 500000},
    {"state": "Tennessee", "total_rides": 3600000},
    {"state": "Texas", "total_rides": 15200000},
    {"state": "Utah", "total_rides": 1700000},
    {"state": "Vermont", "total_rides": 300000},
    {"state": "Virginia", "total_rides": 4500000},
    {"state": "Washington", "total_rides": 4000000},
    {"state": "West Virginia", "total_rides": 900000},
    {"state": "Wisconsin", "total_rides": 3000000},
    {"state": "Wyoming", "total_rides": 300000}
]

def write_data(data):
    filepath = "C:/Users/LENOVO/Documents/denzel-projects/DataVisualization/data/rides_data.json"
    with open(filepath, 'w') as f:
        try:
            json.dump(data, f, indent=4)
            print(f"Data loaded into {filepath} successfully!")
        except Exception as e:
            print(f"Error during writing file: {e}")

write_data(rides_data)

