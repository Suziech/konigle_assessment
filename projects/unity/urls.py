from django.urls import path
from unity import views

urlpatterns = [
    path('leads/', views.index)
]
