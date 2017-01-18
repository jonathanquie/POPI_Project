from django.http import HttpResponse, Http404
from django.shortcuts import render
from datetime import datetime
from institut.models import *
from .forms import *

total_charges=0
ca=0
tva=0
result=0
date=0

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
    view_journees = Journees.objects.all().order_by('id').reverse()


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
    view_journees = Journees.objects.all().order_by('id').reverse()
    return render(request, 'institut/view.html',
                  {'tous_soins_corps': view_soins_corps, 'tous_soins_visages': view_soins_visage,
                   'tous_epilations': view_epilations, 'tous_charges': view_charges, 'tous_ongles': view_ongles,
                   'tous_maquillages': view_maquillage, 'tous_produits': view_produits, 'tous_journees': view_journees})



def delete(request):
    return render(request, 'institut/delete.html')


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

def delete_soin_corps(request):
    form = Delete_soin_corps(request.POST or None)
    flag_delete_soin_corps = True
    Visu_soins_corps = Soins_Corps.objects.all()

    if form.is_valid():
         del_soins_corps_name = form.cleaned_data['del_soins_corps_name']

         id = Soins_Corps.get_id(del_soins_corps_name)

         Soins_Corps(id=id).delete()

         return render(request, 'institut/accueil.html')


    return render(request, 'institut/delete.html', {'delete_SC': Visu_soins_corps, 'flag_SC': flag_delete_soin_corps})

def delete_soin_visage(request):
    form = Delete_soin_visage(request.POST or None)
    flag_delete_soin_visage = True
    Visu_soins_visage = Soins_Visages.objects.all()

    if form.is_valid():
         del_soins_visage_name = form.cleaned_data['del_soins_visage_name']

         id = Soins_Visages.get_id(del_soins_visage_name)

         Soins_Visages(id=id).delete()

         return render(request, 'institut/accueil.html')


    return render(request, 'institut/delete.html', {'delete_SV': Visu_soins_visage, 'flag_SV': flag_delete_soin_visage})


def delete_epilation(request):
    form = Delete_epilation(request.POST or None)
    flag_delete_epilation = True
    Visu_epilation = Epilations.objects.all()

    if form.is_valid():
         del_epilation_name = form.cleaned_data['del_epilation_name']

         id = Epilations.get_id(del_epilation_name)

         Epilations(id=id).delete()

         return render(request, 'institut/accueil.html')


    return render(request, 'institut/delete.html', {'delete_E': Visu_epilation, 'flag_E': flag_delete_epilation})


def delete_ongles(request):
    form = Delete_ongles(request.POST or None)
    flag_delete_ongles = True
    Visu_ongles = Ongles.objects.all()

    if form.is_valid():
         del_ongles_name = form.cleaned_data['del_ongles_name']

         id = Ongles.get_id(del_ongles_name)

         Ongles(id=id).delete()

         return render(request, 'institut/accueil.html')


    return render(request, 'institut/delete.html', {'delete_O': Visu_ongles, 'flag_O': flag_delete_ongles})


def delete_maquillage(request):
    form = Delete_maquillage(request.POST or None)
    flag_delete_maquillage = True
    Visu_maquillage = Maquillage.objects.all()

    if form.is_valid():
         del_maquillage_name = form.cleaned_data['del_maquillage_name']

         id = Maquillage.get_id(del_maquillage_name)

         Maquillage(id=id).delete()

         return render(request, 'institut/accueil.html')


    return render(request, 'institut/delete.html', {'delete_M': Visu_maquillage, 'flag_M': flag_delete_maquillage})


def delete_produit(request):
    form = Delete_produit(request.POST or None)
    flag_delete_produit = True
    Visu_produit = Produits.objects.all()

    if form.is_valid():
         del_produit_name = form.cleaned_data['del_produit_name']

         id = Produits.get_id(del_produit_name)

         Produits(id=id).delete()

         return render(request, 'institut/accueil.html')


    return render(request, 'institut/delete.html', {'delete_P': Visu_produit, 'flag_P': flag_delete_produit})


def delete_charge(request):
    form = Delete_charge(request.POST or None)
    flag_delete_charge = True
    Visu_charge = Charges.objects.all()

    if form.is_valid():
         del_charge_name = form.cleaned_data['del_charge_name']

         id = Charges.get_id(del_charge_name)

         Charges(id=id).delete()

         return render(request, 'institut/accueil.html')


    return render(request, 'institut/delete.html', {'delete_C': Visu_charge, 'flag_C': flag_delete_charge})


def delete_journee(request):
    form = Delete_journee(request.POST or None)
    flag_delete_journee = True
    Visu_journee = Journees.objects.all()

    if form.is_valid():
         del_journee_jour = form.cleaned_data['del_journee_jour']

         print("youpi : ",del_journee_jour)

         Journees(id=del_journee_jour).delete()

         return render(request, 'institut/accueil.html')


    return render(request, 'institut/delete.html', {'delete_J': Visu_journee, 'flag_J': flag_delete_journee})

def newday(request):

    return render(request, 'institut/new_day.html', {'date': datetime.now().date()})

def newday2(request):
    global date

    flag_date_selectionnee = True

    view_soins_corps = Soins_Corps.objects.all()
    view_soins_visage = Soins_Visages.objects.all()
    view_epilations = Epilations.objects.all()
    view_charges = Charges.objects.all()
    view_ongles = Ongles.objects.all()
    view_maquillage = Maquillage.objects.all()
    view_produits = Produits.objects.all()
    view_journees = Journees.objects.all()

    form = New_Day(request.POST or None)

    if form.is_valid():
        date = form.cleaned_data['datepicker']
        print("datepicker = ", date)

    return render(request, 'institut/new_day.html',
                  {'tous_soins_corps': view_soins_corps, 'tous_soins_visages': view_soins_visage,
                   'tous_epilations': view_epilations, 'tous_charges': view_charges, 'tous_ongles': view_ongles,
                   'tous_maquillages': view_maquillage, 'tous_produits': view_produits, 'tous_journees': view_journees,
                   'flag_date_selectionnee': flag_date_selectionnee})

def newday3(request):
    global total_charges
    global ca
    global tva
    global result

    i=j=k=l=m=n=0
    SC=[]
    SV=[]
    E=[]
    O=[]
    M=[]
    P=[]

    Tot=[]

    SC_tmp = request.COOKIES.get('nb_SC')
    SV_tmp = request.COOKIES.get('nb_SV')
    E_tmp = request.COOKIES.get('nb_E')
    O_tmp = request.COOKIES.get('nb_O')
    M_tmp = request.COOKIES.get('nb_M')
    P_tmp = request.COOKIES.get('nb_P')


    while i < len(SC_tmp):
        if (i % 4 == 0):
            SC.append(SC_tmp[i])
        i += 1

    while j < len(SV_tmp):
        if (j % 4 == 0):
            SV.append(SV_tmp[j])
        j += 1

    while k < len(E_tmp):
        if (k % 4 == 0):
            E.append(E_tmp[k])
        k += 1

    while l < len(O_tmp):
        if (l % 4 == 0):
            O.append(O_tmp[l])
        l += 1

    while m < len(M_tmp):
        if (m % 4 == 0):
            M.append(M_tmp[m])
        m += 1

    while n < len(P_tmp):
        if (n % 4 == 0):
            P.append(P_tmp[n])
        n += 1

    #print(SC_tmp)
    #print("SC = ",SC, "\nSV = ",SV, "\nE = ",E, "\nO = ",O, "\nM = ",M,"\nP = ",P)

    view_soins_corps = Soins_Corps.objects.all()
    view_soins_visage = Soins_Visages.objects.all()
    view_epilations = Epilations.objects.all()
    view_ongles = Ongles.objects.all()
    view_maquillage = Maquillage.objects.all()
    view_produits = Produits.objects.all()
    view_charges = Charges.objects.all()

    index_SC=0
    total_SC=0
    for soins_corps in view_soins_corps:
        #print(soins_corps.price)
        total_SC+=(float(soins_corps.price) * float(SC[index_SC]))
        if(int(SC[index_SC]) != 0):
            Tot.append(soins_corps.name)
            Tot.append(soins_corps.price)
            Tot.append(soins_corps.cost)
            Tot.append(SC[index_SC])
        index_SC+=1

    #print("total_SC = ", total_SC)

    index_SV = 0
    total_SV = 0
    for soins_visage in view_soins_visage:
        #print(soins_visage.price)
        total_SV += (float(soins_visage.price) * float(SV[index_SV]))
        if(int(SV[index_SV]) != 0):
            Tot.append(soins_visage.name)
            Tot.append(soins_visage.price)
            Tot.append(soins_visage.cost)
            Tot.append(SV[index_SV])
        index_SV += 1

    #print("total_SV = ", total_SV)

    index_E = 0
    total_E = 0
    for epilation in view_epilations:
        #print(epilation.price)
        total_E += (float(epilation.price) * float(E[index_E]))
        if(int(E[index_E]) != 0):
            Tot.append(epilation.name)
            Tot.append(epilation.price)
            Tot.append(epilation.cost)
            Tot.append(E[index_E])
        index_E += 1

    #print("total_E = ", total_E)

    index_O = 0
    total_O = 0
    for ongle in view_ongles:
        #print(ongle.price)
        total_O += (float(ongle.price) * float(O[index_O]))
        if(int(O[index_O]) != 0):
            Tot.append(ongle.name)
            Tot.append(ongle.price)
            Tot.append(ongle.cost)
            Tot.append(O[index_O])
        index_O += 1

    #print("total_O = ", total_O)

    index_M = 0
    total_M = 0
    for maquillage in view_maquillage:
        #print(maquillage.price)
        total_M += (float(maquillage.price) * float(M[index_M]))
        if(int(M[index_M]) != 0):
            Tot.append(maquillage.name)
            Tot.append(maquillage.price)
            Tot.append(maquillage.cost)
            Tot.append(M[index_M])
        index_M += 1

    #print("total_M = ", total_M)

    index_P = 0
    total_P = 0
    for produit in view_produits:
        #print(produit.price)
        total_P += (float(produit.price) * float(P[index_P]))
        if(int(P[index_P]) != 0):
            Tot.append(produit.name)
            Tot.append(produit.price)
            Tot.append(produit.cost)
            Tot.append(P[index_P])
        index_P += 1

    #print("total_P = ", total_P)
    ca = float(total_SC + total_SV + total_E + total_O + total_M + total_P)
    #print("total total = ", ca)

    total_charges=0

    for charges in view_charges:
        total_charges += float(charges.cost)/25

    #print("Total charges journalières = ", total_charges)

    tva = ca * 0.2
    #print("tva = ",tva)

    result = ca - total_charges - tva
    #print("Resultat net : ", result, "€")

    #print("\n\nTableau : ")
    #print(Tot)

    test_index=0

    print("date = ", date)

    month=date[5:7]

    if(int(month) == 1):
        month = 'Janvier'
    elif(int(month) == 2):
        month = 'Février'
    elif(int(month) == 3):
        month = 'Mars'
    elif(int(month) == 4):
        month = 'Avril'
    elif(int(month) == 5):
        month = 'Mai'
    elif(int(month) == 6):
        month = 'Juin'
    elif(int(month) == 7):
        month = 'Juillet'
    elif(int(month) == 8):
        month = 'Août'
    elif(int(month) == 9):
        month = 'Septembre'
    elif(int(month) == 10):
        month = 'Octobre'
    elif(int(month) == 11):
        month = 'Novembre'
    else:
        month = 'Décembre'

    date_conv = date[8:10] + " " +  month + " " + date[0:4]

    print("date convertie = ", date_conv)

    return render(request, 'institut/calcul.html',{'T':Tot, 'i':test_index, 'date': date_conv,
                                                   'ca':ca, 'charges':total_charges, 'tva':tva, 'result':result})

def test(request):
    return render(request, 'institut/test.html')

def saveday(request):

    Journees(jour=date, id=int(date[0:4]+date[5:7]+date[8:10]) , ca=ca, costs=total_charges, tva=tva, result=result).save()

    #print(date,ca,total_charges,tva,result)

    return render(request, 'institut/view.html')


def one_week(request):

    return HttpResponse("1 week")


def one_month(request):

    return HttpResponse("1 month")



def one_year(request):

    return HttpResponse("1 year")



def as_you_want(request):
    flag_as_you_want = 1

    return render(request, 'institut/view_table.html', {'flag_as_you_want': flag_as_you_want})
