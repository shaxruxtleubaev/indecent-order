from django.urls import path

from .views import (
    About_usAPIView,
    ModelsAPIView,
    ClientRequestAPIView,
    Model_requestAPIView
)

urlpatterns = [
    path('about_us/', About_usAPIView.as_view(), name='about_us'),
    path('models/', ModelsAPIView.as_view(), name='models'),
    path('client_request/create/', ClientRequestAPIView.as_view(), name='clien_request'),
    path('model_request/create/', Model_requestAPIView.as_view(), name='model_request')
]