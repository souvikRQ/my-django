from django.urls import path
from . import views

urlpatterns = [
    path('health', views.health_view, name='health'),
    path('status', views.status_view, name='status'),
    path('api/dummy', views.dummy_view, name='dummy'),
    path('users', views.users_view, name='users'),
]
