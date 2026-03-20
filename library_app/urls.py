from django.urls import path, include

urlpatterns = [
    path('', include('registration.urls')),
]
