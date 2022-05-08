 
import re
from django import forms
from .models import *


required ="s'il vous plait veuillez renmplir tous les champs !!!"

 
 

class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['nom', 'phone', 'date_commande', 'numero_commande',
                  'ligne_un', 'ligne_un_qte','ligne_un_prix_unitaire','ligne_un_prix_total',
                  'ligne_deux', 'ligne_deux_qte','ligne_deux_prix_unitaire','ligne_deux_prix_total',
                  'ligne_trois', 'ligne_trois_qte','ligne_trois_prix_unitaire','ligne_trois_prix_total',
                  'ligne_quatre', 'ligne_quatre_qte','ligne_quatre_prix_unitaire','ligne_quatre_prix_total',
                  'ligne_cinq', 'ligne_cinq_qte','ligne_cinq_prix_unitaire','ligne_cinq_prix_total',
                  'ligne_six', 'ligne_six_qte','ligne_six_prix_unitaire','ligne_six_prix_total',
                  'ligne_sept', 'ligne_sept_qte','ligne_sept_prix_unitaire','ligne_sept_prix_total',
                  'ligne_huit', 'ligne_huit_qte','ligne_huit_prix_unitaire','ligne_huit_prix_total',
                  'total', 'Paie','type_commande'
                  ]
        labels = {
            'nom': 'Nom Complet'
        }
        
    def __init__(self, *args, **kwargs):
        super(CommandeForm, self).__init__(*args, **kwargs)
        self.fields['type_commande'].empty_label = 'Select'
        #self.fields['numero_commande'].required = False
        
   
        
        
    def clean_nom(self):
        nom = self.cleaned_data.get('nom')
        if not nom:
            raise forms.ValidationError(required)
        return nom
    
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone:
            raise forms.ValidationError(required)
        return phone
        
    def clean_date_commande(self):
        date_commande = self.cleaned_data.get('date_commande')
        if not date_commande:
            raise forms.ValidationError(required)
        return date_commande
    
    
    def clean_numero_commande(self):
        numero_commande = self.cleaned_data.get('numero_commande')
        if not numero_commande:
            raise forms.ValidationError(required)
        return numero_commande

    def clean_ligne_un(self):
        ligne_un = self.cleaned_data.get('ligne_un')
        if not ligne_un:
            raise forms.ValidationError(required)
        return ligne_un
    
    def clean_ligne_un_qte(self):
        ligne_un_qte = self.cleaned_data.get('ligne_un_qte')
        if not ligne_un_qte:
            raise forms.ValidationError(required)   
        return ligne_un_qte
    
    
    def clean_ligne_un_prix_unitaire(self):
        ligne_un_prix_unitaire = self.cleaned_data.get('ligne_un_prix_unitaire')
        if not ligne_un_prix_unitaire:
            raise forms.ValidationError(required)     
        return ligne_un_prix_unitaire
    
    
    def clean_ligne_un_prix_total(self):
        ligne_un_prix_total = self.cleaned_data.get('ligne_un_prix_total')
        if not ligne_un_prix_total:
            raise forms.ValidationError(required)    
        return ligne_un_prix_total
    
        
class CommandeSearchForm(forms.ModelForm):
    generer_commande = forms.BooleanField(required=False) 
    class Meta:
        model = Commande
        fields = ['nom', 'numero_commande','generer_commande']
        
       
class CommandeEditeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields =  ['nom', 'phone', 'date_commande', 'numero_commande',
                  'ligne_un', 'ligne_un_qte','ligne_un_prix_unitaire','ligne_un_prix_total',
                  'ligne_deux', 'ligne_deux_qte','ligne_deux_prix_unitaire','ligne_deux_prix_total',
                  'ligne_trois', 'ligne_trois_qte','ligne_trois_prix_unitaire','ligne_trois_prix_total',
                  'ligne_quatre', 'ligne_quatre_qte','ligne_quatre_prix_unitaire','ligne_quatre_prix_total',
                  'ligne_cinq', 'ligne_cinq_qte','ligne_cinq_prix_unitaire','ligne_cinq_prix_total',
                   'ligne_six', 'ligne_six_qte','ligne_six_prix_unitaire','ligne_six_prix_total',
                  'ligne_sept', 'ligne_sept_qte','ligne_sept_prix_unitaire','ligne_sept_prix_total',
                  'ligne_huit', 'ligne_huit_qte','ligne_huit_prix_unitaire','ligne_huit_prix_total',
                  'total', 'Paie','type_commande'
                  ]     

    
    def clean_ligne_un(self):
        ligne_un = self.cleaned_data.get('ligne_un')
        if not ligne_un:
            raise forms.ValidationError(required)
        return ligne_un
        
        
    def clean_ligne_un_qte(self):
        ligne_un_qte = self.cleaned_data.get('ligne_un_qte')
        if not ligne_un_qte:
            raise forms.ValidationError(required)   
        return ligne_un_qte
    
    def clean_ligne_un_prix_unitaire(self):
        ligne_un_prix_unitaire = self.cleaned_data.get('ligne_un_prix_unitaire')
        if not ligne_un_prix_unitaire:
            raise forms.ValidationError(required)
        return ligne_un_prix_unitaire