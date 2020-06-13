from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('email/<email>', views.email, name='email'),

    path('about', views.about, name='about'),
    path('patients', views.patients, name='patients'),
    path('news', views.news, name='news'),
    path('services', views.services, name='services'),
    path('contect', views.contect, name='contect'),
    path('team', views.team, name='team'),
    path('private-policy', views.private_policy, name='private-policy'),
    path('membership', views.membership, name='membership'),
]
