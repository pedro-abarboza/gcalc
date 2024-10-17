from django.urls import include, path
from rest_framework import routers

from tutorial.quickstart import views

from oauth2_provider import urls as oauth2_urls

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    path('oauth/', include(oauth2_urls)),
]
urlpatterns += router.urls