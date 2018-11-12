from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index),
  url(r'^change_gold$', views.generate_word),
  url(r'^clear_session$', views.reset),
]