from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'simple', views.SimpleViewSet)

urlpatterns = [
    #path("", views.index, name="index"),
    #path("page3", views.page3, name="page3"),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]