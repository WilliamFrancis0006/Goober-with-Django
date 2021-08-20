from django.urls import path
from . import views

urlpatterns = [
    #Testing
    #path("<int:id>", views.index, name="index"),
    
    #Home Path
    path("", views.index, name="index"),
    
    #Visible Goober Paths
    path("cyberStaff/", views.cyberStaff, name="cyberStaff"),
    path("RARC2021/", views.RARC2021, name="RARC2021"),
]

