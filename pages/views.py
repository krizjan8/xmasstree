
'''
This is the previous, easiest option how to show html response
'''
#from django.http import HttpResponse

#def home_page_view(request):
#   return HttpResponse("Ahoj")

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"