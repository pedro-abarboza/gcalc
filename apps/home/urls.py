from django.urls import path
from .views.index import Home

urlpatterns = [
    path('', Home.as_view(), name='home'),
]