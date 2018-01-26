from django.contrib import admin
from form_basic.models import Reguser
# Register your models here.


class ReguserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')

admin.site.register(Reguser, ReguserAdmin)