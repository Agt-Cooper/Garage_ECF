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
        fields = ['nom','prenom','commentaire','note']
        widgets = {
            'commentaire' : forms.Textarea(
                attrs={
                    'placeholder':"Vous pouvez rentrer jusqu'à 70 caractères.",
                    'rows' : 5,
                    'cols' : 35,
                }
            ),          
        }
