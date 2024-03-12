from django.urls import path, include
from rest_framework import routers
from collect.views import *

router = routers.SimpleRouter()
router.register('collect', CollectViewSet, 'collect')


urlpatterns = [
    path('', include(router.urls)),
]