from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.core.validators import RegexValidator
from django_resized import ResizedImageField

class MyUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("Vous devez entrer un nom d'utilisateur")         
        username = self.model.normalize_username(username)            
        user = self.model(username=username, password=password)
        user.set_password(password)
        user.save()
        return user
            
    def create_superuser(self, username, password=None):
        username = self.model.normalize_username(username)           
        user = self.create_user(username=username, password=password)
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user
    
permi = [
    ('Employer', 'Employer'),
    ('Administrateur', 'Administrateur'),

]
type = [
    ('Berline', 'berline'),
    ('Coupée', 'Coupée'),
    ('Hayon', 'Hayon'),
    ('Pick-up', 'Pick-up'),
    ('Crossover', 'Crossover'),
    ('SUV', 'SUV'),
    ('Fourgonettes','Fourgonettes'),
    ('Cabriolets','Cabriolets'),
    ('Roadsters','Roadsters'),
    ('Targa', 'Targa'),
    ('citadine','citadine')
]
couleur = [
    ('Rouge', 'Rouge'),
    ('Gris', 'Gris'),
    ('Blanche', 'Blanche'),
    ('Bleu', 'Bleu'),
    ('Noire', 'Noire'),
    ('Jaune', 'Jaune'),
    ('Verte', 'Verte'),
    ('Maron', 'Maron'),
    ('Violette', 'Violette'),
    ('Rose', 'Rose'),
    ('Beige', 'Beige'),
    ('Silver', 'Silver'),    
]
carburant = [
    ('Diesel', 'Diesel'),
    ('Essence','Essence'),
    ('Electrique','Electrique'),
    ('Hybride','Hybride')
]

    
class MyUser(AbstractBaseUser): 
    username = models.CharField(unique=True, max_length=30, blank=False)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    permission = models.CharField(choices= permi, max_length=15, default="commercial", null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username
    
    USERNAME_FIELD = "username"
    objects = MyUserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Voiture(models.Model):
    titre = models.CharField(max_length=50)
    kilometrage = models.IntegerField()
    photo = ResizedImageField(size=[250, 350], quality=85, upload_to='photo', null=True, blank=True)
    prix  = models.IntegerField()
    année = models.DateField( auto_now=False, auto_now_add=False, null=True, blank=True)
    marque = models.ForeignKey('compte.Marque', on_delete=models.SET_NULL, max_length=20, null=True, blank=True)
    modele = models.ForeignKey('compte.Modele', on_delete=models.SET_NULL, max_length=20, null=True, blank=True)
    couleur = models.CharField(choices=couleur, max_length=20)
    typee = models.CharField(choices=type, max_length=20) 
    carburant = models.CharField(choices=carburant,max_length=50)

    def __str__(self):
        return self.titre


class Marque(models.Model):   
    nom = models.CharField(max_length=20, unique=True)  

    def __str__(self):
        return f"{self.nom}"

class Modele(models.Model): 
    marque = models.ForeignKey(Marque, on_delete=models.SET_NULL,  max_length=20, null=True, blank=True)
    nom = models.CharField(max_length=20)

    def __str__(self):
        return self.nom   
    
class Facture(models.Model):
    nom = models.ManyToManyField('compte.service',max_length=50)
    
    def __str__(self):
        return self.nom  
    
class Service(models.Model):
    nom = models.CharField(max_length=50)
    prix = models.IntegerField()

    def __str__(self):
        return self.nom   

class Contact(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(max_length=60)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.nom  

class Livre_dor(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    commentaire = models.CharField(max_length=500)
    note = models.IntegerField()
    verifier = models.BooleanField(default=False)

    def __str__(self):
        return self.nom  