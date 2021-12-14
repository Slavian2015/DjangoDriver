from django.db import models
from django.core.exceptions import ValidationError
import re
from datetime import datetime


def validate_plate_number(numberplate):
    r = re.compile('[A-Z]{2}[ \t]{1}[0-9]{4}[ \t]{1}[A-Z]{2}')
    if r.match(numberplate):
        return numberplate
    else:
        raise ValidationError("This field accepts numberplate of format 'AA 1234 OO' only")


class Driver(models.Model):

    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    created_at = models.DateField(default=datetime.now().strftime("%d.%m.%Y"))
    updated_at = models.DateTimeField(auto_now=True)


class Vehicle(models.Model):

    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    with_drivers = models.CharField(max_length=20, default="no")
    plate_number = models.CharField(max_length=200,
                                    validators=[validate_plate_number])
    created_at = models.DateField(default=datetime.now().strftime("%d.%m.%Y"))
    updated_at = models.DateTimeField(auto_now=True)

