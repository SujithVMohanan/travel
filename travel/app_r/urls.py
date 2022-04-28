from django.urls import path
from . import views
urlpatterns = [
    path('reg', views.register, name='register'),
    path('log', views.login, name='login'),
    path('logout', views.logout, name='logout')
]