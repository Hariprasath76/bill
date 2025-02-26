from django.db import models
from django.utils.timezone import localtime,now
def get_local_time():
    return localtime(now())

# Create your models here.

class CustomerCarRequest(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    profession = models.CharField(max_length=20, blank=True, null=True)
    preferred_brand = models.CharField(max_length=10, blank=True, null=True)
    brand_name = models.CharField(max_length=20, blank=True, null=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    fuel_type = models.CharField(max_length=50, blank=True, null=True)
    transmission = models.CharField(max_length=50, blank=True, null=True)
    drive_type = models.CharField(max_length=50, blank=True, null=True)
    seat_capacity = models.CharField(max_length=50, blank=True, null=True)
    usage_of_car = models.CharField(max_length=50, blank=True, null=True)
    body_type = models.CharField(max_length=50, blank=True, null=True)
    price_start = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    price_end = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    status = models.IntegerField(default=1,db_comment='1 - request, 2 - callback, 3 - success,4 - unsuccess')
    created_at = models.TextField(default=get_local_time)
    updated_at = models.TextField(default=get_local_time)

    class Meta:
        managed = False
        db_table = 'customer_car_request'

