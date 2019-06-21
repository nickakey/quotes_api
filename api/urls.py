from django.urls import path, include
from rest_framework import routers
from .views import QuoteViewSet

router = routers.DefaultRouter()

router.register(r'quotes', QuoteViewSet)

urlpatterns = [
    path('', include(router.urls))
]
