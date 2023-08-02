from django.urls import path 
from . import views

urlpatterns=[
    path('',views.contact),
    # path('contact/',views.contact,name="savecontact")
]
