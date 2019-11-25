
from django.urls import path,include
from .views import main_func
urlpatterns = [
    path('keiba-sisuu-teikyou/',main_func,name='main')

]