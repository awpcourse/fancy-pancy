from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render

class HomeView(TemplateView):

    def get(self, request):
        return render(request, "home.html", {})