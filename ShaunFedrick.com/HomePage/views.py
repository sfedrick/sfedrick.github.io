from django.shortcuts import render
from django.http import HttpResponse 
from django.template.loader import render_to_string
# Create your views here.

def home(request):
    #updates page is the home page
    home_var=render_to_string("aboutme.html")
    return render(request,"headerfooter.html",{'content':home_var})
def updates(request):
    #updates page is the home page
    updates_var=render_to_string("updates.html")
    return render(request,"headerfooter.html",{'content':updates_var,'updates_active':True})
def aboutme(request):
    about_var=render_to_string("aboutme.html")
    return render(request,"headerfooter.html",{'content':about_var,'aboutme_active':True})
def portfolio(request):
    portfolio_var=render_to_string("portfolio.html")
    return render(request,"headerfooter.html",{'content':portfolio_var,'portfolio_active':True})

def art(request):
    art_var=render_to_string("art.html")
    return render(request,"headerfooter.html",{'content':art_var,'art_active':True})

def resume(request):
    resume_var=render_to_string("resume.html")
    return render(request,"headerfooter.html",{'content':resume_var,'resume_active':True})