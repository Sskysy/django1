from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^add/', views.add, name='add'),
    url(r'^add_action/', views.add_action, name='add_action'),

]