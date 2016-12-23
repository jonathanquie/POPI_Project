from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^accueil$', views.home, name='accueil'),
    url(r'^view/(\d+)$', views.view_table),
    url(r'^add1$', views.new_soin_corps, name='new_soin_corps'),
    url(r'^add2$', views.new_soin_visage, name='new_soin_visage'),
    url(r'^add3$', views.new_epilation, name='new_epilation'),
    url(r'^add4$', views.new_ongles, name='new_ongles'),
    url(r'^add5$', views.new_maquillage, name='new_maquillage'),
    url(r'^add6$', views.new_produit, name='new_produit'),
    url(r'^add7$', views.new_charge, name='new_charge'),
    url(r'^date$', views.date_actuelle),
    url(r'^View$', views.view),
    url(r'^Add$', views.add),
    url(r'^Delete$', views.delete),
    url(r'^New$', views.new),
    url(r'^about$', views.about),
    url(r'^contact$', views.contact),
]