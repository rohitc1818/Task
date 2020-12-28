from django.contrib import admin
from gooApp.models import Info

# Register your models here.
class InfoAdmin(admin.ModelAdmin):
    list_display = ['image','phone','Email','bio','name']
    list_editable = ['phone','bio','name']

admin.site.register(Info,InfoAdmin)
