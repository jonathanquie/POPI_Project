from django import forms

class New_soin_corps(forms.Form):
    soin_corps_name = forms.CharField(label="Nom du soin", max_length=100)
    soin_corps_price = forms.CharField(label="Prix de vente du soin")
    soin_corps_cost = forms.CharField(label="Coût de revient du soin")