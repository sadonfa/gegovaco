from django.contrib import admin
from services.models import Services

# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_filter = ('id',)
    list_display = ('name', 'description', 'created_at')

admin.site.register(Services, PageAdmin)

admin.site.site_header = "Portal Gegova"
admin.site.site_title = "Portal Gegova"
admin.site.index_title = "Panel De Gestion"
