import json

rides_data = [
    {"state": "Alabama", "total_rides": 2600000, "hours": 720, "average_hourly_rides": round(2600000 / 720)},
    {"state": "Alaska", "total_rides": 800000, "hours": 720, "average_hourly_rides": round(800000 / 720)},
    {"state": "Arizona", "total_rides": 4100000, "hours": 720, "average_hourly_rides": round(4100000 / 720)},
    {"state": "Arkansas", "total_rides": 1900000, "hours": 720, "average_hourly_rides": round(1900000 / 720)},
    {"state": "California", "total_rides": 20500000, "hours": 720, "average_hourly_rides": round(20500000 / 720)},
    {"state": "Colorado", "total_rides": 3100000, "hours": 720, "average_hourly_rides": round(3100000 / 720)},
    {"state": "Connecticut", "total_rides": 2000000, "hours": 720, "average_hourly_rides": round(2000000 / 720)},
    {"state": "Delaware", "total_rides": 1000000, "hours": 720, "average_hourly_rides": round(1000000 / 720)},
    {"state": "Florida", "total_rides": 11200000, "hours": 720, "average_hourly_rides": round(11200000 / 720)},
    {"state": "Georgia", "total_rides": 5600000, "hours": 720, "average_hourly_rides": round(5600000 / 720)},
    {"state": "Hawaii", "total_rides": 900000, "hours": 720, "average_hourly_rides": round(900000 / 720)},
    {"state": "Idaho", "total_rides": 1100000, "hours": 720, "average_hourly_rides": round(1100000 / 720)},
    {"state": "Illinois", "total_rides": 6700000, "hours": 720, "average_hourly_rides": round(6700000 / 720)},
    {"state": "Indiana", "total_rides": 3600000, "hours": 720, "average_hourly_rides": round(3600000 / 720)},
    {"state": "Iowa", "total_rides": 1800000, "hours": 720, "average_hourly_rides": round(1800000 / 720)},
    {"state": "Kansas", "total_rides": 1600000, "hours": 720, "average_hourly_rides": round(1600000 / 720)},
    {"state": "Kentucky", "total_rides": 2400000, "hours": 720, "average_hourly_rides": round(2400000 / 720)},
    {"state": "Louisiana", "total_rides": 2500000, "hours": 720, "average_hourly_rides": round(2500000 / 720)},
    {"state": "Maine", "total_rides": 700000, "hours": 720, "average_hourly_rides": round(700000 / 720)},
    {"state": "Maryland", "total_rides": 3200000, "hours": 720, "average_hourly_rides": round(3200000 / 720)},
    {"state": "Massachusetts", "total_rides": 3700000, "hours": 720, "average_hourly_rides": round(3700000 / 720)},
    {"state": "Michigan", "total_rides": 5100000, "hours": 720, "average_hourly_rides": round(5100000 / 720)},
    {"state": "Minnesota", "total_rides": 3000000, "hours": 720, "average_hourly_rides": round(3000000 / 720)},
    {"state": "Mississippi", "total_rides": 1600000, "hours": 720, "average_hourly_rides": round(1600000 / 720)},
    {"state": "Missouri", "total_rides": 3200000, "hours": 720, "average_hourly_rides": round(3200000 / 720)},
    {"state": "Montana", "total_rides": 600000, "hours": 720, "average_hourly_rides": round(600000 / 720)},
    {"state": "Nebraska", "total_rides": 1000000, "hours": 720, "average_hourly_rides": round(1000000 / 720)},
    {"state": "Nevada", "total_rides": 1700000, "hours": 720, "average_hourly_rides": round(1700000 / 720)},
    {"state": "New Hampshire", "total_rides": 700000, "hours": 720, "average_hourly_rides": round(700000 / 720)},
    {"state": "New Jersey", "total_rides": 4800000, "hours": 720, "average_hourly_rides": round(4800000 / 720)},
    {"state": "New Mexico", "total_rides": 1100000, "hours": 720, "average_hourly_rides": round(1100000 / 720)},
    {"state": "New York", "total_rides": 10200000, "hours": 720, "average_hourly_rides": round(10200000 / 720)},
    {"state": "North Carolina", "total_rides": 5500000, "hours": 720, "average_hourly_rides": round(5500000 / 720)},
    {"state": "North Dakota", "total_rides": 400000, "hours": 720, "average_hourly_rides": round(400000 / 720)},
    {"state": "Ohio", "total_rides": 6100000, "hours": 720, "average_hourly_rides": round(6100000 / 720)},
    {"state": "Oklahoma", "total_rides": 2100000, "hours": 720, "average_hourly_rides": round(2100000 / 720)},
    {"state": "Oregon", "total_rides": 2300000, "hours": 720, "average_hourly_rides": round(2300000 / 720)},
    {"state": "Pennsylvania", "total_rides": 6700000, "hours": 720, "average_hourly_rides": round(6700000 / 720)},
    {"state": "Rhode Island", "total_rides": 600000, "hours": 720, "average_hourly_rides": round(600000 / 720)},
    {"state": "South Carolina", "total_rides": 2700000, "hours": 720, "average_hourly_rides": round(2700000 / 720)},
    {"state": "South Dakota", "total_rides": 500000, "hours": 720, "average_hourly_rides": round(500000 / 720)},
    {"state": "Tennessee", "total_rides": 3600000, "hours": 720, "average_hourly_rides": round(3600000 / 720)},
    {"state": "Texas", "total_rides": 15200000, "hours": 720, "average_hourly_rides": round(15200000 / 720)},
    {"state": "Utah", "total_rides": 1700000, "hours": 720, "average_hourly_rides": round(1700000 / 720)},
    {"state": "Vermont", "total_rides": 300000, "hours": 720, "average_hourly_rides": round(300000 / 720)},
    {"state": "Virginia", "total_rides": 4500000, "hours": 720, "average_hourly_rides": round(4500000 / 720)},
    {"state": "Washington", "total_rides": 4000000, "hours": 720, "average_hourly_rides": round(4000000 / 720)},
    {"state": "West Virginia", "total_rides": 900000, "hours": 720, "average_hourly_rides": round(900000 / 720)},
    {"state": "Wisconsin", "total_rides": 3000000, "hours": 720, "average_hourly_rides": round(3000000 / 720)},
    {"state": "Wyoming", "total_rides": 300000, "hours": 720, "average_hourly_rides": round(300000 / 720)},
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

