
'''
This is the previous, easiest option how to show html response
'''
from django.http import HttpResponse

def Click_view(request):
   print('click')
   return HttpResponse('')

def Color_action(request):
   print('color')
   if request.method == 'POST':
       color = request.POST.get('color')
       print(color)
   return HttpResponse('')

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"

