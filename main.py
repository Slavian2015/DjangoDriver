from datetime import datetime

d = []

for i in range(1, 10):
    data_d = {
        "model": "driver_api.driver",
        "pk": i,
        "fields": {
            "first_name": f"driver_name_{i}",
            "last_name": f"driver_name2_{i}",
            "created_at": f"{datetime.now()}",
            "updated_at": f"{datetime.now()}",
        }
    }
    data_v = {
        "model": "driver_api.Vehicle",
        "pk": i,
        "fields": {
            "driver_id": i,
            "make": "Ford",
            "model": f"KUGA_{i}",
            "plate_number": f"AA 123{i} OO",
            "created_at": f"{datetime.now()}",
            "updated_at": f"{datetime.now()}",
        }
    }

    d.append(data_d)
    d.append(data_v)

print(d)