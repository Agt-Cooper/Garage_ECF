from compte.models import Contact, Livre_dor, Voiture, Facture
from django import forms
import os


def delete_previous_picture(previous,new):
    if previous != new:
        os.remove(previous)
        return True
    return False  


class DateInput(forms.DateInput):
    input_type = 'date'

class ContactForm(forms.ModelForm):    
    class Meta:
        model = Contact
        fields = '__all__'
        
class AnnonceForm(forms.ModelForm):
    class Meta:
        model = Voiture
        fields =[
        'titre', 
        'kilometrage', 
        'prix',
        'photo',
        'année',
        'marque', 
        'modele', 
        'couleur', 
        'typee',  
        'carburant',]
        widgets = {
            'année' : DateInput
        }



class Livre_dorForm(forms.ModelForm):
    class Meta:
        model = Livre_dor
        fields = '__all__'
        
class factureForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields = '__all__'


