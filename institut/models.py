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

    def get_id(name):

        test = Charges.objects.get(name=name)

        print(test.name, test.id)

        return test.id

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

    def get_id(name):

        test = Epilations.objects.get(name=name)

        print(test.name, test.id)

        return test.id

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

    def get_id(name):

        test = Maquillage.objects.get(name=name)

        print(test.name, test.id)

        return test.id

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

    def get_id(name):

        test = Ongles.objects.get(name=name)

        print(test.name, test.id)

        return test.id

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

    def get_id(name):

        test = Produits.objects.get(name=name)

        print(test.name, test.id)

        return test.id

class Soins_Corps(models.Model):
    id = models.IntegerField(primary_key=True,auto_created=True)
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

    def get_id(name):

        test = Soins_Corps.objects.get(name=name)

        print(test.name, test.id)

        return test.id

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

    def get_id(name):

        test = Soins_Visages.objects.get(name=name)

        print(test.name, test.id)

        return test.id

class Journees(models.Model):
    jour = models.DateField(primary_key=True)
    id = models.IntegerField(auto_created=True)
    ca = models.FloatField()
    costs = models.FloatField()
    tva = models.FloatField()
    result = models.FloatField()


    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard et dans l'administration
        """
        return self.jour

    def get_id(jour):

        test = Journees.objects.get(jour=jour)

        print(test.jour, test.id)

        return test.id