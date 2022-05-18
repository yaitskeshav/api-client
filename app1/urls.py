from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('BornesHorsRue', views.BornesHorsRue),
    # path('fd', views.fetchdata),
    path('fd/<slug:db>/<slug:password>', views.fetchdata),
    
    path('fd/<slug:db>/<slug:password>/', views.fetchdata),

    path('fd/<slug:db>/<slug:password>/<slug:count>', views.fetchdata),
    path('fd/<slug:db>/<slug:password>/<slug:initial>/<slug:final>', views.fetchdata),
    # path('fd/', views.fetchdata),
    # path('fd', views.fetchdata),
    # path('fd/<slug:db>', views.fetchdata),
]