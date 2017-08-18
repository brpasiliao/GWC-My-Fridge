from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.recipe_list, name='recipe_list'),
]
