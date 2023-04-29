from django.urls import path
from . import views 


urlpatterns=[
    path('',views.home),
    path('updates',views.updates),
    path('aboutme',views.aboutme),
    path('portfolio',views.portfolio),
    path('art',views.art),
    path('resume',views.resume)
]
