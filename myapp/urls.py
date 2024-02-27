from django.urls import path
from .views import *
app_name='myapp'

urlpatterns = [
    path('register/',register,name='register'),
    path('home/',home,name='home'),
    path('logout/',logout_view,name='logout'),
    path('login/',login_view,name='login'),

]
