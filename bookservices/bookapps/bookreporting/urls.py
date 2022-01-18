from django.urls import path

from . import views

urlpatterns =[

    path('',views.home, name='bookreporting-home'),
    path('about/',views.about, name='bookreporting-about')
]