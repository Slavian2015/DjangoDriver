from datetime import datetime

d = []
now = datetime.now().strftime('%d-%m-%Y')

for i in range(1, 3):
    data_d = {
        "model": "driver_api.driver",
        "pk": i,
        "fields": {
            "first_name": f"driver_name_{i}",
            "last_name": f"driver_name2_{i}",
            "created_at": f"{now}",
            "updated_at": f"{now}",
        }
    }
    data_v = {
        "model": "driver_api.Vehicle",
        "pk": i,
        "fields": {
            "with_drivers": "no",
            "make": "Ford",
            "model": f"KUGA_{i}",
            "plate_number": f"AA 123{i} OO",
            "created_at": f"{now}",
            "updated_at": f"{now}",
        }
    }

    d.append(data_d)
    d.append(data_v)

print(d)
"""
[{"model": "driver_api.driver", "pk": 1,
  "fields": {"first_name": "driver_name_1", "last_name": "driver_name2_1", "created_at": "2021-11-9", "updated_at": "2021-11-9"}},
  {"model": "driver_api.Vehicle", "pk": 1,
    "fields": {"with_drivers": "yes", "make": "Ford", "model": "KUGA_1", "plate_number": "AA 1231 OO", "created_at": "2021-12-14", "updated_at": "2021-12-14"}},
  {"model": "driver_api.driver", "pk": 2,
    "fields": {"first_name": "driver_name_2", "last_name": "driver_name2_2", "created_at": "2021-11-16", "updated_at": "2021-11-16"}},
  {"model": "driver_api.Vehicle", "pk": 2,
    "fields": {"with_drivers": "no", "make": "Ford", "model": "KUGA_2", "plate_number": "AA 1232 OO", "created_at": "2021-12-14", "updated_at": "2021-12-14"}}]
"""


"""
[{"model": "driver_api.driver", "pk": 1, 
"fields": {"first_name": "driver_name_1", "last_name": "driver_name2_1", "created_at": "14-12-2021", "updated_at": "14-12-2021"}}, 
{"model": "driver_api.Vehicle", "pk": 1, 
"fields": {"with_drivers": "no", "make": "Ford", "model": "KUGA_1", "plate_number": "AA 1231 OO", "created_at": "14-12-2021", "updated_at": "14-12-2021"}}, 
{"model": "driver_api.driver", "pk": 2, 
"fields": {"first_name": "driver_name_2", "last_name": "driver_name2_2", "created_at": "14-12-2021", "updated_at": "14-12-2021"}}, 
{"model": "driver_api.Vehicle", "pk": 2, 
"fields": {"with_drivers": "no", "make": "Ford", "model": "KUGA_2", "plate_number": "AA 1232 OO", "created_at": "14-12-2021", "updated_at": "14-12-2021"}}]

"""