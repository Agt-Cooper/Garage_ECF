from django.contrib import admin
from compte.models import *
from django.contrib.auth.models import Group

admin.site.site_header="Garage V.Parrot"
admin.site.register(MyUser)
admin.site.unregister(Group)

@admin.register(Modele, Marque, Facture, Voiture, Service, Contact, Livre_dor)
class PersonAdmin(admin.ModelAdmin):
    pass
# Register your models here.
