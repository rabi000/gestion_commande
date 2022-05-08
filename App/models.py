from django.db import models

 
# Create your models here.
class Commande(models.Model):
    
    commentaires = models.TextField( max_length=1000, default='', blank=True, null=True)
    nom = models.CharField('Nom', max_length=120, default='',null=True, blank=True)
    phone = models.CharField('phone', max_length=120,default='', null=True, blank=True)
    numero_commande = models.IntegerField('Numero Commnande',blank=True, null=True)
    date_commande = models.DateField( auto_now_add=False, auto_now=False, null=True, blank=True)
    
    
    
    ligne_un = models.CharField('Ligne 1', max_length=120,default='', null=True, blank=True)
    ligne_un_qte = models.IntegerField('Quantite',default='0', null=True, blank=True)
    ligne_un_prix_unitaire = models.IntegerField('Prix Unitaire (D)',default='0', null=True, blank=True)
    ligne_un_prix_total = models.IntegerField('Ligne Total (D)',default='0', null=True, blank=True)
    
    ligne_deux = models.CharField('Ligne 2', max_length=120,default='', null=True, blank=True)
    ligne_deux_qte = models.IntegerField('Quantite',default='0', null=True, blank=True)
    ligne_deux_prix_unitaire = models.IntegerField('Prix Unitaire (D)',default='0', null=True, blank=True)
    ligne_deux_prix_total = models.IntegerField('Ligne Total (D)',default='0', null=True, blank=True)
    
    ligne_trois = models.CharField('Ligne 3', max_length=120,default='', null=True, blank=True)
    ligne_trois_qte = models.IntegerField('Quantite',default='0', null=True, blank=True)
    ligne_trois_prix_unitaire = models.IntegerField('Prix Unitaire (D)',default='0', null=True, blank=True)
    ligne_trois_prix_total = models.IntegerField('Ligne Total (D)',default='0', null=True, blank=True)
    
    
    ligne_quatre = models.CharField('Ligne 4', max_length=120,default='', null=True, blank=True)
    ligne_quatre_qte = models.IntegerField('Quantite',default='0', null=True, blank=True)
    ligne_quatre_prix_unitaire = models.IntegerField('Prix Unitaire (D)',default='0', null=True, blank=True)
    ligne_quatre_prix_total = models.IntegerField('Ligne Total (D)',default='0', null=True, blank=True)
    
    
    ligne_cinq = models.CharField('Ligne 5', max_length=120,default='', null=True, blank=True)
    ligne_cinq_qte = models.IntegerField('Quantite',default='0', null=True, blank=True)
    ligne_cinq_prix_unitaire = models.IntegerField('Prix Unitaire (D)',default='0', null=True, blank=True)
    ligne_cinq_prix_total = models.IntegerField('Ligne Total (D)',default='0', null=True, blank=True)
    
    
     
    ligne_six = models.CharField('Ligne 6', max_length=120,default='', null=True, blank=True)
    ligne_six_qte = models.IntegerField('Quantite',default='0', null=True, blank=True)
    ligne_six_prix_unitaire = models.IntegerField('Prix Unitaire (D)',default='0', null=True, blank=True)
    ligne_six_prix_total = models.IntegerField('Ligne Total (D)',default='0', null=True, blank=True)
    
     
    ligne_sept = models.CharField('Ligne 7', max_length=120,default='', null=True, blank=True)
    ligne_sept_qte = models.IntegerField('Quantite',default='0', null=True, blank=True)
    ligne_sept_prix_unitaire = models.IntegerField('Prix Unitaire (D)',default='0', null=True, blank=True)
    ligne_sept_prix_total = models.IntegerField('Ligne Total (D)',default='0', null=True, blank=True)
    
     
    ligne_huit = models.CharField('Ligne 8', max_length=120,default='', null=True, blank=True)
    ligne_huit_qte = models.IntegerField('Quantite',default='0', null=True, blank=True)
    ligne_huit_prix_unitaire = models.IntegerField('Prix Unitaire (D)',default='0', null=True, blank=True)
    ligne_huit_prix_total = models.IntegerField('Ligne Total (D)',default='0', null=True, blank=True)
    
    total = models.IntegerField('Total',default='0', null=True, blank=True)
    balance = models.IntegerField('balance',default=0, null=True,blank=True)
    creer = models.DateTimeField(auto_now_add=True, auto_now=False)
    derniere_modification = models.DateTimeField(auto_now_add=False, auto_now=True)
    Paie = models.BooleanField(default=False)
    CHOIX_TYPE_COMMANDE = (
        ('Reception','Reception'),
        ('Commande','Commande'),        
    ) 
    
    type_commande = models.CharField(max_length=50, default='', null=True, blank=True, choices= CHOIX_TYPE_COMMANDE)
    def __str__(self):
        return self.nom
    
     
