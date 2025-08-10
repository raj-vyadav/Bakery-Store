from django.contrib import admin
from django.urls import path, include
from bakery_app.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('bakery_app.urls')),
    path('', home, name='home')
]
