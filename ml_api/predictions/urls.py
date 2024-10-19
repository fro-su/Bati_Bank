from django.urls import path
from .views import predict_default

urlpatterns = [
    path('predict/', predict_default, name='predict_default'),
]
