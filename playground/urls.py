from django.urls import path
from . import views

#url configuration or URLConf
urlpatterns = [
    path('hello/', views.say_hello), #path('hello/', views.say_hello) uses the same name as the function
]