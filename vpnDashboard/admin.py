from django.contrib import admin

from .models import vpn
from .models import profile
from .models import device


class vpnAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'creationTime', 'coordinates')
    list_display_links = ('name', 'status')
    search_fields = ('name', 'isOnline', 'status',)


admin.site.register(profile)
admin.site.register(vpn, vpnAdmin)
admin.site.register(device)
