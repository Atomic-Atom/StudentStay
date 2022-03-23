from django.urls import path
from frontend.views import IndexView, AboutUsView

urlpatterns = [
    path('', IndexView.as_view()),
    path('about-us/', AboutUsView.as_view()),
]
