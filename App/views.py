import imp
from django.shortcuts import render, redirect
from .forms import *
from .models import*
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
#reportlab
from django.contrib import messages
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import Image


# Create your views here.

def home(request):
    title = 'Liste des commandes'
    commande = Commande.objects.all()
    total_commande = commande.count()
    context = {'title': title, 'commande':commande,'total_commande':total_commande}
    return render(request, 'home.html',context)

@login_required(login_url='login') 
def add_commande(request):
    form = CommandeForm()
    commande_total = Commande.objects.count()
    commande = Commande.objects.order_by('-date_commande')[:6]
    if request.method =='POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Commande ajoutée avec succès')
            return HttpResponseRedirect('listes_commande')
                
    context = {'form': form, 'title':'Ajouter une nouvelle commande','commande_total': commande_total, 'commande': commande}            
    return render(request, 'add_commande.html', context)

@login_required(login_url='login')
def listes_commande(request):
    title = 'Liste des commandes'
    commande = Commande.objects.all()
    form = CommandeSearchForm(request.POST)
    
    context = {'title': title, 'commande':commande,'form':form}
    
    if request.method == 'POST':
        commande = Commande.objects.filter(numero_commande__icontains= form['numero_commande'].value(),
                                           nom__icontains=form['nom'].value())
         
        
        context = {'title': title, 'commande':commande, 'form':form}
    
    
    
    
        if form['generer_commande'].value() == True:
            instance = commande
            data_file = instance
            numero_commande = len(commande)
            message = str(numero_commande) + " invoices successfully generated."
            messages.success(request, message)

            def import_data(data_file):
                commande_data = data_file
                for row in commande_data:
                    type_commande = row.type_commande
                    numero_commande = row.numero_commande
                    date_commande = row.date_commande
                    nom = row.nom
                    phone = row.phone

                    ligne_un = row.ligne_un
                    ligne_un_qte = row.ligne_un_qte
                    ligne_un_prix_unitaire = row.ligne_un_prix_unitaire
                    ligne_un_prix_total = row.ligne_un_prix_total

                    ligne_deux = row.ligne_deux
                    ligne_deux_qte = row.ligne_deux_qte
                    ligne_deux_prix_unitaire = row.ligne_deux_prix_unitaire
                    ligne_deux_prix_total = row.ligne_deux_prix_total

                    ligne_trois = row.ligne_trois
                    ligne_trois_qte = row.ligne_trois_qte
                    ligne_trois_prix_unitaire = row.ligne_trois_prix_unitaire
                    ligne_trois_prix_total = row.ligne_trois_prix_total

                    ligne_quatre = row.ligne_quatre
                    ligne_quatre_qte = row.ligne_quatre_qte
                    ligne_quatre_prix_unitaire = row.ligne_quatre_prix_unitaire
                    ligne_quatre_prix_total = row.ligne_quatre_prix_total

                    ligne_cinq = row.ligne_cinq
                    ligne_cinq_qte = row.ligne_cinq_qte
                    ligne_cinq_prix_unitaire = row.ligne_cinq_prix_unitaire
                    ligne_cinq_prix_total = row.ligne_cinq_prix_total

                    ligne_six = row.ligne_six
                    ligne_six_qte = row.ligne_six_qte
                    ligne_six_prix_unitaire = row.ligne_six_prix_unitaire
                    ligne_six_prix_total = row.ligne_six_prix_total

                    ligne_sept = row.ligne_sept
                    ligne_sept_qte = row.ligne_sept_qte
                    ligne_sept_prix_unitaire = row.ligne_sept_prix_unitaire
                    ligne_sept_prix_total = row.ligne_sept_prix_total

                    ligne_huit = row.ligne_huit
                    ligne_huit_qte = row.ligne_huit_qte
                    ligne_huit_prix_unitaire = row.ligne_huit_prix_unitaire
                    ligne_huit_prix_total = row.ligne_huit_prix_total

                    
                    total = row.total
                    pdf_file_nom = str(numero_commande) + '_' + str(nom) + '.pdf'
                    generer_commande(str(nom), str(numero_commande),
                        str(ligne_un), str(ligne_un_qte), str(ligne_un_prix_unitaire), 
                        str(ligne_un_prix_total), str(ligne_deux), str(ligne_deux_qte),
                        str(ligne_deux_prix_unitaire), str(ligne_deux_prix_total), str(ligne_trois),
                        str(ligne_trois_qte), str(ligne_trois_prix_unitaire),
                        str(ligne_trois_prix_total), str(ligne_quatre), str(ligne_quatre_qte),
                        str(ligne_quatre_prix_unitaire), str(ligne_quatre_prix_total),  str(ligne_cinq),
                        str(ligne_cinq_qte), str(ligne_cinq_prix_unitaire),
                        str(ligne_cinq_prix_total), str(ligne_six), str(ligne_six_qte),
                        str(ligne_six_prix_unitaire), str(ligne_six_prix_total), str(ligne_sept),
                        str(ligne_sept_qte), str(ligne_sept_prix_unitaire),
                        str(ligne_sept_prix_total), str(ligne_huit), str(ligne_huit_qte),
                        str(ligne_huit_prix_unitaire), str(ligne_huit_prix_total),
                        str(total), str(phone), str(date_commande), str(type_commande), pdf_file_nom)

            def generer_commande(nom, numero_commande, 
                                ligne_un, ligne_un_qte, ligne_un_prix_unitaire, ligne_un_prix_total, 
                                ligne_deux, ligne_deux_qte, ligne_deux_prix_unitaire, ligne_deux_prix_total, 
                                ligne_trois, ligne_trois_qte, ligne_trois_prix_unitaire, ligne_trois_prix_total, 
                                ligne_quatre,ligne_quatre_qte,ligne_quatre_prix_unitaire,ligne_quatre_prix_total, 
                                ligne_cinq, ligne_cinq_qte, ligne_cinq_prix_unitaire, ligne_cinq_prix_total, 
                                ligne_six, ligne_six_qte, ligne_six_prix_unitaire, ligne_six_prix_total, 
                                ligne_sept, ligne_sept_qte, ligne_sept_prix_unitaire, ligne_sept_prix_total, 
                                ligne_huit, ligne_huit_qte, ligne_huit_prix_unitaire, ligne_huit_prix_total, 
                                total, phone, date_commande, type_commande, pdf_file_nom):
                    
                c = canvas.Canvas(pdf_file_nom)

                # image of seal
               # logo = 'logoarb.png'
               # c.drawImage(logo, 50, 700, width=500, height=120)

                c.setFont('Helvetica', 12, leading=None)
                # if invoice_type == 'Receipt':
                # 	c.drawCentredString(400, 660, "Receipt Number #:")
                # elif invoice_type == 'Proforma Invoice':
                # 	c.drawCentredString(400, 660, "Proforma Invoice #:")
                # else:
                c.drawCentredString(400, 660, str(type_commande) + ':')
                c.setFont('Helvetica', 12, leading=None)
                numero_commande_string = str('0000' + numero_commande)
                c.drawCentredString(490, 660, numero_commande_string)


                c.setFont('Helvetica', 12, leading=None)
                c.drawCentredString(409, 640, "Date:")
                c.setFont('Helvetica', 12, leading=None)
               # c.drawCentredString(492, 641, commande_data)


                c.setFont('Helvetica', 12, leading=None)
                c.drawCentredString(397, 620, "Amount:")
                c.setFont('Helvetica-Bold', 12, leading=None)
                c.drawCentredString(484, 622, 'D'+total)


                c.setFont('Helvetica', 12, leading=None)
                c.drawCentredString(80, 660, "To:")
                c.setFont('Helvetica', 12, leading=None)
                c.drawCentredString(150, 660, nom)

                c.setFont('Helvetica', 12, leading=None)
                c.drawCentredString(98, 640, "Phone #:")
                c.setFont('Helvetica', 12, leading=None)
                c.drawCentredString(150, 640, phone)     

                c.setFont('Helvetica-Bold', 14, leading=None)
                c.drawCentredString(310, 580, str(type_commande))
                c.drawCentredString(110, 560, "Particulars:")
                c.drawCentredString(295, 510, "__________________________________________________________")
                c.drawCentredString(295, 480, "__________________________________________________________")
                c.drawCentredString(295, 450, "__________________________________________________________")
                c.drawCentredString(295, 420, "__________________________________________________________")
                c.drawCentredString(295, 390, "__________________________________________________________")
                c.drawCentredString(295, 360, "__________________________________________________________")
                c.drawCentredString(295, 330, "__________________________________________________________")
                c.drawCentredString(295, 300, "__________________________________________________________")
                c.drawCentredString(295, 270, "__________________________________________________________")
                c.drawCentredString(295, 240, "__________________________________________________________")
                c.drawCentredString(295, 210, "__________________________________________________________")

                c.setFont('Helvetica-Bold', 12, leading=None)
                c.drawCentredString(110, 520, 'ITEMS')     
                c.drawCentredString(220, 520, 'QUANTITÉ')     
                c.drawCentredString(330, 520, 'PRIX UNITAIRE')     
                c.drawCentredString(450, 520, 'LIGNE TOTAL')  


                c.setFont('Helvetica', 12, leading=None)
                c.drawCentredString(110, 490, ligne_un)     
                c.drawCentredString(220, 490, ligne_un_qte)     
                c.drawCentredString(330, 490, ligne_un_prix_unitaire)     
                c.drawCentredString(450, 490, ligne_un_prix_total)     

                if ligne_deux != '':
                    c.setFont('Helvetica', 12, leading=None)
                    c.drawCentredString(110, 460, ligne_deux)     
                    c.drawCentredString(220, 460, ligne_deux_qte)     
                    c.drawCentredString(330, 460, ligne_deux_prix_unitaire)     
                    c.drawCentredString(450, 460, ligne_deux_prix_total)     

                if ligne_trois != '':
                    c.setFont('Helvetica', 12, leading=None)
                    c.drawCentredString(110, 430, ligne_trois)     
                    c.drawCentredString(220, 430, ligne_trois_qte)     
                    c.drawCentredString(330, 430, ligne_trois_prix_unitaire)     
                    c.drawCentredString(450, 430, ligne_trois_prix_total)     

                if ligne_quatre != '':
                    c.setFont('Helvetica', 12, leading=None)
                    c.drawCentredString(110, 400,ligne_quatre)     
                    c.drawCentredString(220, 400,ligne_quatre_qte)     
                    c.drawCentredString(330, 400,ligne_quatre_prix_unitaire)     
                    c.drawCentredString(450, 400,ligne_quatre_prix_total)     

                if ligne_cinq != '':
                    c.setFont('Helvetica', 12, leading=None)
                    c.drawCentredString(110, 370, ligne_cinq)     
                    c.drawCentredString(220, 370, ligne_cinq_qte)     
                    c.drawCentredString(330, 370, ligne_cinq_prix_unitaire)     
                    c.drawCentredString(450, 370, ligne_cinq_prix_total)     

                if ligne_six != '':
                    c.setFont('Helvetica', 12, leading=None)
                    c.drawCentredString(110, 340, ligne_six)     
                    c.drawCentredString(220, 340, ligne_six_qte)     
                    c.drawCentredString(330, 340, ligne_six_prix_unitaire)     
                    c.drawCentredString(450, 340, ligne_six_prix_total)     

                if ligne_sept != '':
                    c.setFont('Helvetica', 12, leading=None)
                    c.drawCentredString(110, 310, ligne_sept)     
                    c.drawCentredString(220, 310, ligne_sept_qte)     
                    c.drawCentredString(330, 310, ligne_sept_prix_unitaire)     
                    c.drawCentredString(450, 310, ligne_sept_prix_total)     

                if ligne_huit != '':
                    c.setFont('Helvetica', 12, leading=None)
                    c.drawCentredString(110, 280, ligne_huit)     
                    c.drawCentredString(220, 280, ligne_huit_qte)     
                    c.drawCentredString(330, 280, ligne_huit_prix_unitaire)     
                    c.drawCentredString(450, 280, ligne_huit_prix_total)     

            
                # TOTAL
                c.setFont('Helvetica-Bold', 20, leading=None)
                c.drawCentredString(400, 140, "TOTAL:")
                c.setFont('Helvetica-Bold', 20, leading=None)
                c.drawCentredString(484, 140, 'D'+total) 


                # SIGN
                c.setFont('Helvetica-Bold', 12, leading=None)
                c.drawCentredString(150, 140, "Signed:__________________")
                c.setFont('Helvetica-Bold', 12, leading=None)
                c.drawCentredString(170, 120, 'Manager') 


                c.showPage()
                #print 'writing'
                c.save()

            import_data(data_file)
#Add generate invoice checkbox in search form

#class CommandeSearchForm(forms.ModelForm):
#	generer_commande = forms.BooleanField(required=False)
#	class Meta:
#		model = Commande
#		fields = ['generer_commande']    

    return render(request, 'listes_commande.html', context)



@login_required(login_url='login')
def edite_commande(request,pk):
    commande = Commande.objects.get(id=pk)
    form = CommandeForm(instance=commande)
    if request.method == 'POST':
        form = CommandeEditeForm(request.POST, instance=commande)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/listes_commande')
    context = {'form': form}    
    return render(request, 'edites_commande.html', context)

@login_required(login_url='login')    
def delete_commande(request, pk):
    commande = Commande.objects.get(id=pk)
    if request.method == 'POST':
        commande.delete()
        return redirect('/listes_commande')
    return render(request, 'delete_commande.html')