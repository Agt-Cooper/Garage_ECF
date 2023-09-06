from django.shortcuts import render, redirect
from django.contrib.auth import logout
from compte.form import *
from compte.models import *
from django.db.models import Q



def index(request):
    avis = Livre_dor.objects.all() 
    print(avis)
    context={
        'avis' : avis,
        'navbar': 'index'}
    return render(request, 'index.html',context)

def catalogue(request):   
    voiture = Voiture.objects.all() 
    context={'navbar': 'catalogue',
            'voiture' : voiture,
            }
    return render(request, 'catalogue.html',context)

def catalogue2(request):   
    voiture = Voiture.objects.all() 
    context={'navbar': 'catalogue',
            'voiture' : voiture,
            }
    return render(request, 'catalogue2.html',context)


def contact(request):
    form = ContactForm()   
    if request.method == "POST":
        print(request.POST)
        form = ContactForm(request.POST)  
        if form.is_valid():
            form.save()            
            return redirect('index')
        else:
            print(form.errors)            
            form = ContactForm()    
    context={'navbar': 'contact',
            'form' : form,             
            }    
    return render(request, 'contact.html',context)

def login(request):
    context={'navbar': 'login'}
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    return redirect('index')

def annonce(request):
    form = AnnonceForm()   
    if request.method == "POST":
        form = AnnonceForm(request.POST, request.FILES)    
        if form.is_valid():
            form.save()            
            return redirect('catalogue2')
        else:
            print(form.errors)            
            form = AnnonceForm()    
    context={'navbar': 'annonce',
            'form' : form,              
            }
    return render(request, 'annonce.html', context)

def update_annonce(request, pk):
    annonce = Voiture.objects.get(pk=pk)
    form = AnnonceForm(request.POST or None, request.FILES or None, instance=annonce)
    if request.method == "POST":
        print(request.POST)
        form = AnnonceForm(request.POST or None, request.FILES or None, instance=annonce)  
        if form.is_valid():
            form.save()            
            return redirect('index')         
    context={'navbar': 'annonce',
            'form' : form,                          
            }
    return render(request, 'annonce2.html', context)

def delete_annonce(request, pk):   
    Voiture.objects.filter(id=pk).delete()
    voiture = Voiture.objects.all()
    context = {
        'navbar': 'annonce',
        'voiture' : voiture,
    }
    return render(request,'catalogue2.html', context)

def cherche_voiture(request):
    cherche = request.POST.get('cherche')
    voitures = Voiture.objects.filter(Q(kilometrage__icontains=cherche)|
                                    Q(prix__icontains=cherche) |
                                    Q(année__icontains=cherche)|
                                    Q(titre__icontains=cherche))
                                    #    Q(modele__icontains=cherche))
    context = {
        'voiture' : voitures
    }
    return render(request,'catalogue.html', context)

    

def livre(request):
    form = Livre_dorForm
    if request.method == "POST":
        form = Livre_dorForm(request.POST, request.FILES)    
        if form.is_valid():
            form.save()            
            return redirect('catalogue2')
        else:
            print(form.errors)            
            form = Livre_dorForm()    
    context={'navbar': 'annonce',
            'form' : form,              
            }
    return render(request, 'livre.html', context)