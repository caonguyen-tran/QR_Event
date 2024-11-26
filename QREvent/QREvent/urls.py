from django.urls import path, include

urlpatterns = [
    path('', include('QREvent_app.urls')),
]