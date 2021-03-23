from django.urls import path
from .views import TestExample

urlpatterns = [
    path('start/', TestExample.as_view())
]
