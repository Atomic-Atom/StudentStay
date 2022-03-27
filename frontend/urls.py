from frontend import views
from django.urls import path

urlpatterns = [
    path('', views.IndexView.as_view(), name='home-page'),
    path('property/<int:pk>/', views.PropertyView.as_view(), name='property-view'),
]
