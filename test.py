import truck_telemetry

truck_telemetry.init()
data = truck_telemetry.get_data()
print(data["speed"])
