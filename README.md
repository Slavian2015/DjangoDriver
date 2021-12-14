1. You can open SWAGGER UI to see all api end-points:
  
   ```
   http://127.0.0.1:8000/api/schema/swagger-ui/
   ```

  
1. Driver:

    ```
    + GET /drivers/driver/ - вивід списку водіїв
   + GET /drivers/driver/?created_at__gte=2021-11-10 - вивід списку водіїв, які створені після 2021-11-10
   + GET /drivers/driver/?created_at__lte=2021-11-16 - вивід списку водіїв, котрі створені до 2021-11-16

   + GET /drivers/driver/<driver_id>/ - отримання інформації по певному водію
   + POST /drivers/driver/ - створення нового водія
   + UPDATE /drivers/driver/<driver_id>/ - редагування водія
   + DELETE /drivers/driver/<driver_id>/ - видалення водія
       ```


2. Vehicle:
  
    ```
    + GET /vehicles/vehicle/ - вивід списку машин
   + GET /vehicles/vehicle/?with_drivers=yes - вивід списку машин з водіями
   + GET /vehicles/vehicle/?with_drivers=no - вивід списку машин без водіїв

   + GET /vehicles/vehicle/<vehicle_id> - отримання інформації по певній машині
   + POST /vehicles/vehicle/ - створення нової машини
   + UPDATE /vehicles/vehicle/<vehicle_id>/ - редагування машини
   + POST /vehicles/vehicle/<vehicle_id>/set_driver/ - садимо водія в машину / висаджуємо водія з машини  
   + DELETE /vehicles/vehicle/<vehicle_id>/ - видалення машини
       ```
