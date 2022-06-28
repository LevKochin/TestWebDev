from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('vpndashboard/<int:vpnid>/', include('vpnDashboard.urls')),
    path('admin/', admin.site.urls),
]
