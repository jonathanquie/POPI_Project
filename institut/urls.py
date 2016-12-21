from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^accueil$', views.home),
    url(r'^view/(\d+)$', views.view_table),
    url(r'^add/(\d+)$', views.new_soin_corps, name="test"),
    url(r'^date$', views.date_actuelle),
    url(r'^View$', views.view),
    url(r'^Add$', views.add),
    url(r'^Delete$', views.delete),
    url(r'^New$', views.new),
    url(r'^about$', views.about),
]