from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^add/', views.add, name='add'),
    url(r'^add_action/', views.add_action, name='add_action'),
    url(r'^ag/', views.add_ag, name='add_ag'),
    url(r'^add_ag_action/', views.add_ag_action, name='add_ag_action'),
    url(r'^am/', views.add_am, name='add_am'),
    url(r'^add_am_action/', views.add_am_action, name='add_am_action'),
    url(r'^agent/', views.agent, name='agent'),
    url(r'^medium/', views.medium, name='medium')

 
]

