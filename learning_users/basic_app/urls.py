from django.urls import path
from basic_app import views

#TEMPLATE URLS!
app_name = 'basic_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
]

