from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('BornesHorsRue', views.BornesHorsRue),
    path('fd', views.fetchdata),
    path('fd/<slug:db>', views.fetchdata),
]