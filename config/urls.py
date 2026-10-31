from django.contrib import admin
from django.urls import path
from api.views import status_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/status/", status_view),
]