from django.urls import path
from .views import base, translate_text


urlpatterns = [
    path('', base, name='base'),
    path('translate/', translate_text, name='translate_text'),
]