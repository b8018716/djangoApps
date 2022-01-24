from django.urls import path
from users import views as user_views

from . import views

urlpatterns =[

    path('',views.home, name='bookreporting-home'),
    path('about/',views.about, name='bookreporting-about'),
    path('register/', user_views.register, name='register'),
]