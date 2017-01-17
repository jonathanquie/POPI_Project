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
    url(r'^about$', views.about),
    url(r'^contact$', views.contact),
    url(r'^delete$', views.delete),
    url(r'^delete1$', views.delete_soin_corps, name='delete_soin_corps'),
    url(r'^delete2$', views.delete_soin_visage, name='delete_soin_visage'),
    url(r'^delete3$', views.delete_epilation, name='delete_epilation'),
    url(r'^delete4$', views.delete_ongles, name='delete_ongles'),
    url(r'^delete5$', views.delete_maquillage, name='delete_maquillage'),
    url(r'^delete6$', views.delete_produit, name='delete_produit'),
    url(r'^delete7$', views.delete_charge, name='delete_charge'),
    url(r'^delete8$', views.delete_journee, name='delete_journee'),
    url(r'^newday$', views.newday, name='newday'),
    url(r'^newday2$', views.newday2, name='newday2'),
    url(r'^newday3$', views.newday3, name='newday3'),
    url(r'^test$', views.test, name='test'),
    url(r'^saveday$', views.saveday, name='saveday'),

]