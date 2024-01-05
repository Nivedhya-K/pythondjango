from django.contrib import admin


from .models import Cakes
from .models import Place
# Register your models here.
admin.site.register(Cakes)
admin.site.register(Place)
