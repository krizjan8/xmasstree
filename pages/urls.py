from django.urls import path
#from .views import home_page_view #previous option if home_page_view(request) method was called from viewes.py
from .views import HomePageView

urlpatterns = [
   # path("", home_page_view, name="home"),  # see comment
    path("", HomePageView.as_view(), name="home"),
]
