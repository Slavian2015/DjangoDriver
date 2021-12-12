from django.db import models
from django.core.exceptions import ValidationError
import re


# creating a validator function
def validate_plate_number(numberplate):
    r = re.compile('[A-Z]{2}[ \t]{1}[0-9]{4}[ \t]{1}[A-Z]{2}')
    if r.match(numberplate):
        return numberplate
    else:
        raise ValidationError("This field accepts numberplate of format 'AA 1234 OO' only")


class Driver(models.Model):

    # id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Vehicle(models.Model):

    # id = models.IntegerField(primary_key=True)
    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE)

    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    plate_number = models.CharField(max_length=200,
                                    validators=[validate_plate_number])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

