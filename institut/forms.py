from django import forms

class New_soin_corps(forms.Form):
    soin_corps_name = forms.CharField(label="Nom du soin", max_length=100)
    soin_corps_price = forms.CharField(label="Prix de vente du soin")
    soin_corps_cost = forms.CharField(label="Coût de revient du soin")

class New_soin_visage(forms.Form):
    soin_visage_name = forms.CharField(label="Nom du soin", max_length=100)
    soin_visage_price = forms.CharField(label="Prix de vente du soin")
    soin_visage_cost = forms.CharField(label="Coût de revient du soin")

class New_epilation(forms.Form):
    epilation_name = forms.CharField(label="Nom de l'épilation", max_length=100)
    epilation_price = forms.CharField(label="Prix de vente de l'épilation")
    epilation_cost = forms.CharField(label="Coût de revient de l'épilation")

class New_ongles(forms.Form):
    ongles_name = forms.CharField(label="Nom du soin ongles", max_length=100)
    ongles_price = forms.CharField(label="Prix de vente du soin ongles")
    ongles_cost = forms.CharField(label="Coût de revient du soin ongles")

class New_maquillage(forms.Form):
    maquillage_name = forms.CharField(label="Nom du soin maquillage", max_length=100)
    maquillage_price = forms.CharField(label="Prix de vente du soin maquillage")
    maquillage_cost = forms.CharField(label="Coût de revient du soin maquillage")

class New_produit(forms.Form):
    produit_name = forms.CharField(label="Nom du produit", max_length=100)
    produit_price = forms.CharField(label="Prix de vente du produit")
    produit_cost = forms.CharField(label="Coût de revient du produit")

class New_charge(forms.Form):
    charge_name = forms.CharField(label="Nom de la charge", max_length=100)
    charge_cost = forms.CharField(label="Coût de la charge")

class New_day(forms.Form):
    day_ca = forms.CharField(label="CA de la journee")
    day_costs = forms.CharField(label="CA de la journee")
    day_tva = forms.CharField(label="CA de la journee")
    day_result = forms.CharField(label="CA de la journee")

class Delete_soin_corps(forms.Form):
    del_soins_corps_name = forms.CharField(label="Nom du soin", max_length=100)

class Delete_soin_visage(forms.Form):
    del_soins_visage_name = forms.CharField(label="Nom du soin", max_length=100)

class Delete_epilation(forms.Form):
    del_epilation_name = forms.CharField(label="Nom du soin", max_length=100)

class Delete_ongles(forms.Form):
    del_ongles_name = forms.CharField(label="Nom du soin", max_length=100)

class Delete_maquillage(forms.Form):
    del_maquillage_name = forms.CharField(label="Nom du soin", max_length=100)

class Delete_produit(forms.Form):
    del_produit_name = forms.CharField(label="Nom du soin", max_length=100)

class Delete_charge(forms.Form):
    del_charge_name = forms.CharField(label="Nom du soin", max_length=100)

class Delete_journee(forms.Form):
    del_journee_jour = forms.CharField(label="Nom du soin", max_length=100)

class New_Day(forms.Form):
    datepicker = forms.CharField(label="Nouvelle journée")

class New_Day_SC(forms.Form):
    nb_SC = forms.IntegerField()

class Tri_Journees_Personnalise(forms.Form):
    Start_date = forms.DateField()
    End_date = forms.DateField()

class New_RDV(forms.Form):
    datepickerrdv = forms.CharField(label="jour", max_length=100)
    description = forms.CharField(label="categorie", max_length=100)
    title = forms.CharField(label="client", max_length=100)
    heure_start = forms.CharField(label="heure de debut", max_length=100)
    heure_end = forms.CharField(label="heure de fin", max_length=100)

class Save_Day(forms.Form):
    remise = forms.CharField(label="jour", max_length=100)