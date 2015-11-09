from django.contrib import admin
from .models import SuperBlock
from .models import Subnet

# Register your models here.

admin.site.register(SuperBlock)
admin.site.register(Subnet)
