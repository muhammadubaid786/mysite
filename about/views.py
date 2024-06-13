from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def about(request):
    # View code here...
    t = loader.get_template("about.html")
    return HttpResponse(t.render())