from django.urls import path
from .views import Click_view #previous option if home_page_view(request) method was called from viewes.py
from .views import HomePageView
from .views import Color_action

urlpatterns = [
    path("click/", Click_view, name="click"),  # see comment
    path("colorAction/", Color_action, name="color_action"),
    path("", HomePageView.as_view(), name="home"),
]
