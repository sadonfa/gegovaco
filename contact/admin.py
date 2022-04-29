from django.contrib import admin
from contact.models import Contact

# Register your models here.


class ContAdmin(admin.ModelAdmin):
    list_filter = ('id',)
    list_display = ('name', 'mail', 'phone', 'mess', 'created_at')

admin.site.register(Contact, ContAdmin)