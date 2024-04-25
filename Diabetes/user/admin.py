from django.contrib import admin
from .models import Info, HealthData


class HealthAdmin(admin.ModelAdmin):
    readonly_fields = ('timestamp',)


admin.site.register(Info)
admin.site.register(HealthData,HealthAdmin)
# Register your models here.
