from django.db import models

class customer(models.Model):
    n_comp = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=20)
    prenom = models.CharField(max_length=30)
    nom = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)

