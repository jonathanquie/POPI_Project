from django.http import HttpResponse, Http404
from django.shortcuts import render
from datetime import datetime
from institut.models import Epilations, Charges, Ongles, Soins_Corps, Soins_Visages, Maquillage, Produits, Journees
from .forms import New_soin_corps, New_charge, New_epilation, New_maquillage, New_ongles, New_produit, New_soin_visage

def home(request):
    return render(request, 'institut/accueil.html')

def view_table(request, id_article):
    view_soins_corps = Soins_Corps.objects.all()
    view_soins_visage = Soins_Visages.objects.all()
    view_epilations = Epilations.objects.all()
    view_charges = Charges.objects.all()
    view_ongles = Ongles.objects.all()
    view_maquillage = Maquillage.objects.all()
    view_produits = Produits.objects.all()
    view_journees = Journees.objects.all()


    if int(id_article) < 9:
          if(id_article=='1'):
              return render(request, 'institut/view_table.html', {'id': id_article, 'visu1': view_soins_corps})
          elif(id_article=='2'):
              return render(request, 'institut/view_table.html', {'id': id_article, 'visu2': view_soins_visage})
          elif(id_article=='3'):
              return render(request, 'institut/view_table.html', {'id': id_article, 'visu3': view_epilations})
          elif(id_article=='4'):
              return render(request, 'institut/view_table.html', {'id': id_article, 'visu4': view_ongles})
          elif(id_article=='5'):
              return render(request, 'institut/view_table.html', {'id': id_article, 'visu5': view_maquillage})
          elif(id_article=='6'):
              return render(request, 'institut/view_table.html', {'id': id_article, 'visu6': view_produits})
          elif(id_article=='7'):
              return render(request, 'institut/view_table.html', {'id': id_article, 'visu7': view_charges})
          else:
              return render(request, 'institut/view_table.html', {'id': id_article, 'visu8': view_journees})
    else:
         raise Http404



def add_table(request, id_article):
    if int(id_article) <8:
        return render(request, 'institut/add_table.html', {'id': id_article})
    else:
        raise Http404



def date_actuelle(request):
    return render(request, 'institut/date.html', {'date': datetime.now()})

def view(request):
    view_soins_corps = Soins_Corps.objects.all()
    view_soins_visage = Soins_Visages.objects.all()
    view_epilations = Epilations.objects.all()
    view_charges = Charges.objects.all()
    view_ongles = Ongles.objects.all()
    view_maquillage = Maquillage.objects.all()
    view_produits = Produits.objects.all()
    view_journees = Journees.objects.all()
    return render(request, 'institut/view.html',
                  {'tous_soins_corps': view_soins_corps, 'tous_soins_visages': view_soins_visage,
                   'tous_epilations': view_epilations, 'tous_charges': view_charges, 'tous_ongles': view_ongles,
                   'tous_maquillages': view_maquillage, 'tous_produits': view_produits, 'tous_journees': view_journees})



def add(request):
    return render(request, 'institut/add.html')

def delete(request):
    return render(request, 'institut/delete.html')

def new(request):
    return render(request, 'institut/new_day.html')

def about(request):
    return render(request, 'institut/about.html')

def contact(request):
    return render(request, 'institut/contact.html')



def new_soin_corps(request):
    form = New_soin_corps(request.POST or None)

    if form.is_valid():
        soin_corps_name = form.cleaned_data['soin_corps_name']
        soin_corps_price = form.cleaned_data['soin_corps_price']
        soin_corps_cost = form.cleaned_data['soin_corps_cost']

        envoi = True

        Soins_Corps(name=soin_corps_name, price=soin_corps_price, cost=soin_corps_cost).save()

    return render(request, 'institut/add_soin_corps.html', locals())


def new_soin_visage(request):
    form = New_soin_visage(request.POST or None)

    if form.is_valid():
        soin_visage_name = form.cleaned_data['soin_visage_name']
        soin_visage_price = form.cleaned_data['soin_visage_price']
        soin_visage_cost = form.cleaned_data['soin_visage_cost']

        envoi = True


        Soins_Visages(name=soin_visage_name, price=soin_visage_price, cost=soin_visage_cost).save()

        return render(request, 'institut/add_soin_visage.html', locals())


def new_epilation(request):
    form = New_epilation(request.POST or None)

    if form.is_valid():
        epilation_name = form.cleaned_data['epilation_name']
        epilation_price = form.cleaned_data['epilation_price']
        epilation_cost = form.cleaned_data['epilation_cost']

        envoi = True

        Epilations(name=epilation_name, price=epilation_price, cost=epilation_cost).save()

    return render(request, 'institut/add_epilation.html', locals())


def new_ongles(request):
    form = New_ongles(request.POST or None)

    if form.is_valid():
        ongles_name = form.cleaned_data['ongles_name']
        ongles_price = form.cleaned_data['ongles_price']
        ongles_cost = form.cleaned_data['ongles_cost']

        envoi = True

        Ongles(name=ongles_name, price=ongles_price, cost=ongles_cost).save()

    return render(request, 'institut/add_ongles.html', locals())


def new_maquillage(request):
    form = New_maquillage(request.POST or None)

    if form.is_valid():
        maquillage_name = form.cleaned_data['maquillage_name']
        maquillage_price = form.cleaned_data['maquillage_price']
        maquillage_cost = form.cleaned_data['maquillage_cost']

        envoi = True

        Maquillage(name=maquillage_name, price=maquillage_price, cost=maquillage_cost).save()

    return render(request, 'institut/add_maquillage.html', locals())


def new_produit(request):
    form = New_produit(request.POST or None)

    if form.is_valid():
        produit_name = form.cleaned_data['produit_name']
        produit_price = form.cleaned_data['produit_price']
        produit_cost = form.cleaned_data['produit_cost']

        envoi = True

        Produits(name=produit_name, price=produit_price, cost=produit_cost).save()

    return render(request, 'institut/add_produit.html', locals())

def new_charge(request):
    form = New_charge(request.POST or None)

    if form.is_valid():
        charge_name = form.cleaned_data['charge_name']
        charge_cost = form.cleaned_data['charge_cost']

        envoi = True

        Charges(name=charge_name, cost=charge_cost).save()

    return render(request, 'institut/add_charge.html', locals())