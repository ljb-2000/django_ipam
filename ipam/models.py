from django.db import models

# Create your models here.


class SuperBlock(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    address_space = models.CharField(max_length=255, unique=True)
    region = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.address_space


class Subnet(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    address_space = models.CharField(max_length=255)
    vrf = models.CharField(max_length=255, blank=True)
    route_target = models.CharField(max_length=128, blank=True)
    vlan_id = models.IntegerField(blank=True)
    environment = models.CharField(max_length=255)
    region = models.CharField(max_length=255, blank=True)
    customer_name = models.CharField(max_length=255, blank=True)
    super_block = models.ForeignKey(SuperBlock)

    def __str__(self):
        return self.address_space
