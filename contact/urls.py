from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('person/<int:pk>', views.contact_detail, name='contact_detail'),
    path('person/new', views.contact_new, name='contact_new'),
]
