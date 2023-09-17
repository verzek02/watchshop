from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.watch.urls')),
    path('', include('apps.user.urls')),
]