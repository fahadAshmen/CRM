from django.urls import path
from accounts import views



urlpatterns = [
    path('home/',views.home, name= 'home'),
    path('',views.index, name= 'index'),
    path('register/',views.register, name='register'),
    path('logout/',views.logout_user, name= 'logout'),
]
