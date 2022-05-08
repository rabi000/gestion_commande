from django.contrib import admin
from .forms import CommandeForm
from .models import *


# Register your models here.
class CommandeAdmin(admin.ModelAdmin):
    form = CommandeForm
    list_filter =  [ 'nom']
    list_display =  ['numero_commande', 'nom','date_commande','phone']
    search_fields = ['numero_commande', 'nom']

admin.site.register(Commande, CommandeAdmin)


 
    