from django.db import models


class Charges(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=42)
    cost = models.FloatField()


    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard et dans l'administration
        """
        return self.name

class Epilations(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=42)
    price = models.FloatField()
    cost = models.FloatField()


    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard et dans l'administration
        """
        return self.name

class Maquillage(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=42)
    price = models.FloatField()
    cost = models.FloatField()


    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard et dans l'administration
        """
        return self.name

class Ongles(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=42)
    price = models.FloatField()
    cost = models.FloatField()


    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard et dans l'administration
        """
        return self.name

class Produits(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=42)
    price = models.FloatField()
    cost = models.FloatField()


    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard et dans l'administration
        """
        return self.name

class Soins_Corps(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=42)
    price = models.FloatField()
    cost = models.FloatField()


    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard et dans l'administration
        """
        return self.name

class Soins_Visages(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=42)
    price = models.FloatField()
    cost = models.FloatField()


    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard et dans l'administration
        """
        return self.name

class Journees(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    jour = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de la journée")
    ca = models.FloatField()
    costs = models.FloatField()
    result = models.FloatField()


    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard et dans l'administration
        """
        return self.jour
