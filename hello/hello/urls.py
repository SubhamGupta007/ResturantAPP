
from django.contrib import admin
from django.urls import path, include
admin.site.site_header = "ICE-cream Portal"
admin.site.site_title = "Ice-cream Portal"
admin.site.index_title = "Welcome to SUBHAM iCECREAM"
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('home.urls'))
]
