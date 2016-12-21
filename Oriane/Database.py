import sqlite3
import functools


class NewDatabase():
    def __init__(self):
        conn = sqlite3.connect('popi.db')

        cursor = conn.cursor()

        # ===========================#
        #	TABLE Soins du visage 	#
        # ===========================#

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Soins_Visages(
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                name TEXT,
                price FLOAT,
                cost FLOAT
            )
            """)

        # ===========================#
        #	TABLE Soins du corps 	#
        # ===========================#

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Soins_Corps(
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                name TEXT,
                price FLOAT,
                cost FLOAT
            )
            """)

        # ===========================#
        #	TABLE Epilations	 	#
        # ===========================#

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Epilations(
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                name TEXT,
                price FLOAT,
                cost FLOAT
            )
            """)

        # ===========================#
        #	TABLE Ongles		 	#
        # ===========================#

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Ongles(
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                name TEXT,
                price FLOAT,
                cost FLOAT
            )
            """)

        # ===========================#
        #	TABLE Maquillage	 	#
        # ===========================#

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Maquillage(
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                name TEXT,
                price FLOAT,
                cost FLOAT
            )
            """)

        # ===========================#
        #	TABLE Produits		 	#
        # ===========================#

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Produits(
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                name TEXT,
                price FLOAT,
                cost FLOAT
            )
            """)

        # ===========================#
        #	TABLE Charges		 	#
        # ===========================#

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Charges(
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                name TEXT,
                cost FLOAT
            )
            """)

        # ===========================#
        #	TABLE Journées		 	#
        # ===========================#

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Journees(
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                jour TIMESTAMP,
                ca FLOAT,
                costs FLOAT,
                result FLOAT
            )
            """)

        conn.commit()
        conn.close()


class NewEntry():
    def __init__(self):
        # entry = input("Renseigner un nouveau service ? (y : oui / n : non) ")
        # if(entry == 'y' or entry =='Y'):
        conn = sqlite3.connect('popi.db')
        cursor = conn.cursor()
        while True:
            Type = int(input(
                "\nQuel type de nouveau service ?\n1 - Soins du visage\n2 - Soins du corps\n3 - Epilations\n4 - Ongles\n5 - Maquillage\n6 - Nouveau produit\n7 - Charges\n\nNuméro : "))
            # print(Type)
            if (Type == 1 or Type == 2 or Type == 3 or Type == 4 or Type == 5 or Type == 6 or Type == 7 or Type == 8):
                break

        if (Type == 1):
            self.New_Soin_Visage()
        elif (Type == 2):
            self.New_Soin_Corps()
        elif (Type == 3):
            self.New_Epilation()
        elif (Type == 4):
            self.New_Ongles()
        elif (Type == 5):
            self.New_Maquillage()
        elif (Type == 6):
            self.New_Produit()
        elif (Type == 7):
            self.New_Charge()
        else:
            print("Commande inconnue !")

    def New_Soin_Visage(self):
        Tab = []
        Nom = input("\nNom du soin : ")
        Tab.append(Nom)
        Prix = float(input("Tarif du soin : "))
        Tab.append(Prix)
        Cout_revient = float(input("Coût de revient du soin : "))
        Tab.append(Cout_revient)

        conn = sqlite3.connect('popi.db')
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO Soins_Visages(name,price,cost) VALUES(?,?,?)""", Tab)

        conn.commit()
        conn.close()

    def New_Soin_Corps(self):
        Tab = []
        Nom = input("\nNom du soin : ")
        Tab.append(Nom)
        Prix = float(input("Tarif du soin : "))
        Tab.append(Prix)
        Cout_revient = float(input("Coût de revient du soin : "))
        Tab.append(Cout_revient)

        conn = sqlite3.connect('popi.db')
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO Soins_Corps(name,price,cost) VALUES(?,?,?)""", Tab)

        conn.commit()
        conn.close()

    def New_Epilation(self):
        Tab = []
        Nom = input("\nNom de l'épilation : ")
        Tab.append(Nom)
        Prix = float(input("Tarif de l'épilation : "))
        Tab.append(Prix)
        Cout_revient = float(input("Coût de revient de l'épilation : "))
        Tab.append(Cout_revient)

        conn = sqlite3.connect('popi.db')
        cursor = conn.cursor()

        cursor.execute("""INSERT INTO Epilations(name,price,cost) VALUES(?,?,?)""", Tab)

        conn.commit()
        conn.close()

    def New_Ongles(self):
        Tab = []
        Nom = input("\nNom du service : ")
        Tab.append(Nom)
        Prix = float(input("Tarif du service : "))
        Tab.append(Prix)
        Cout_revient = float(input("Coût de revient du service : "))
        Tab.append(Cout_revient)

        conn = sqlite3.connect('popi.db')
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO Ongles(name,price,cost) VALUES(?,?,?)""", Tab)

        conn.commit()
        conn.close()

    def New_Maquillage(self):
        Tab = []
        Nom = input("\nNom du service : ")
        Tab.append(Nom)
        Prix = float(input("Tarif du service : "))
        Tab.append(Prix)
        Cout_revient = float(input("Coût de revient du service : "))
        Tab.append(Cout_revient)

        conn = sqlite3.connect('popi.db')
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO Maquillage(name,price,cost) VALUES(?,?,?)""", Tab)

        conn.commit()
        conn.close()

    def New_Produit(self):
        Tab = []
        Nom = input("\nNom du produit : ")
        Tab.append(Nom)
        Prix = float(input("Prix de vente du produit : "))
        Tab.append(Prix)
        Cout_revient = float(input("Coût de revient du produit : "))
        Tab.append(Cout_revient)

        conn = sqlite3.connect('popi.db')
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO Produits(name,price,cost) VALUES(?,?,?)""", Tab)

        conn.commit()
        conn.close()

    def New_Charge(self):
        Tab = []
        Nom = input("\nNom de la charge : ")
        Tab.append(Nom)
        Cout = float(input("Cout de la charge : "))
        Tab.append(Cout)

        conn = sqlite3.connect('popi.db')
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO Charges(name,cost) VALUES(?,?)""", Tab)

        conn.commit()
        conn.close()


class ViewDatabases():
    def __init__(self):
        # entry = input("Voir une table ? (y : oui / n : non) ")
        # if(entry == 'y' or entry =='Y'):
        conn = sqlite3.connect('popi.db')
        cursor = conn.cursor()

        while True:
            Type = int(input(
                "\nQuelle table ?\n1 - Soins du visage\n2 - Soins du corps\n3 - Epilations\n4 - Ongles\n5 - Maquillage\n6 - Produits\n7 - Charges\n8 - Renseigner la journée\n\nNuméro : "))
            # print(Type)
            if (Type == 1 or Type == 2 or Type == 3 or Type == 4 or Type == 5 or Type == 6 or Type == 7 or Type == 8):
                break

        if (Type == 1):
            self.View_Soin_Visage()
        elif (Type == 2):
            self.View_Soin_Corps()
        elif (Type == 3):
            self.View_Epilation()
        elif (Type == 4):
            self.View_Ongles()
        elif (Type == 5):
            self.View_Maquillage()
        elif (Type == 6):
            self.View_Produit()
        elif (Type == 7):
            self.View_Charge()
        else:
            self.View_Journee()

    def View_Soin_Visage(self):
        conn = sqlite3.connect('popi.db')
        cursor = conn.cursor()

        cursor.execute("""SELECT name,price,cost FROM Soins_Visages """)
        rows = cursor.fetchall()

        conn.close()

        print(rows)

    def View_Soin_Corps(self):
        conn = sqlite3.connect('popi.db')
        cursor = conn.cursor()

        cursor.execute("""SELECT name,price,cost FROM Soins_Corps """)
        rows = cursor.fetchall()

        conn.close()

        print(rows)

    def View_Epilation(self):
        conn = sqlite3.connect('popi.db')
        cursor = conn.cursor()

        cursor.execute("""SELECT name,price,cost FROM Epilations """)
        rows = cursor.fetchall()

        conn.close()

        print(rows)

    def View_Ongles(self):
        conn = sqlite3.connect('popi.db')
        cursor = conn.cursor()

        cursor.execute("""SELECT name,price,cost FROM Ongles """)
        rows = cursor.fetchall()

        conn.close()

        print(rows)

    def View_Maquillage(self):
        conn = sqlite3.connect('popi.db')
        cursor = conn.cursor()

        cursor.execute("""SELECT name,price,cost FROM Maquillage """)
        rows = cursor.fetchall()

        conn.close()

        print(rows)

    def View_Produit(self):
        conn = sqlite3.connect('popi.db')
        cursor = conn.cursor()

        cursor.execute("""SELECT name,price,cost FROM Produits """)
        rows = cursor.fetchall()

        conn.close()

        print(rows)

    def View_Charge(self):
        conn = sqlite3.connect('popi.db')
        cursor = conn.cursor()

        cursor.execute("""SELECT name,cost FROM Charges """)
        rows = cursor.fetchall()

        conn.close()

        print(rows)

    def View_Journee(self):
        conn = sqlite3.connect('popi.db')
        cursor = conn.cursor()

        cursor.execute("""SELECT jour,result FROM Journees """)
        rows = cursor.fetchall()

        conn.close()

        print(rows)


class DeleteElement():
    def __init__(self):
        # entry = input("Supprimer un élément ? (y : oui / n : non) ")
        # if(entry == 'y' or entry =='Y'):
        conn = sqlite3.connect('popi.db')
        cursor = conn.cursor()

        while True:
            Type = int(input(
                "\nDans quelle table ?\n1 - Soins du visage\n2 - Soins du corps\n3 - Epilations\n4 - Ongles\n5 - Maquillage\n6 - Produits\n7 - Charges\n8 - Renseigner la journée\n\nNuméro : "))
            # print(Type)
            if (Type == 1 or Type == 2 or Type == 3 or Type == 4 or Type == 5 or Type == 6 or Type == 7 or Type == 8):
                break

        if (Type == 1):
            self.Delete_Soin_Visage()
        elif (Type == 2):
            self.Delete_Soin_Corps()
        elif (Type == 3):
            self.Delete_Epilation()
        elif (Type == 4):
            self.Delete_Ongles()
        elif (Type == 5):
            self.Delete_Maquillage()
        elif (Type == 6):
            self.Delete_Produit()
        elif (Type == 7):
            self.Delete_Charge()
        else:
            self.Delete_Journee()

    def Delete_Soin_Visage(self):
        Element = input("Quel est l'élément à supprimer dans les soins visages ? ")

        conn = sqlite3.connect('popi.db')
        cursor = conn.cursor()

        cursor.execute("""DELETE FROM Soins_Visages WHERE name=? """, (Element,))

        conn.commit()
        conn.close()

    def Delete_Soin_Corps(self):
        Element = input("Quel est l'élément à supprimer dans les soins corps ? ")

        conn = sqlite3.connect('popi.db')
        cursor = conn.cursor()

        cursor.execute("""DELETE FROM Soins_Corps WHERE name=? """, (Element,))

        conn.commit()
        conn.close()

    def Delete_Epilation(self):
        Element = input("Quel est l'élément à supprimer dans les épilations ? ")

        conn = sqlite3.connect('popi.db')
        cursor = conn.cursor()

        cursor.execute("""DELETE FROM Epilations WHERE name=? """, (Element,))

        conn.commit()
        conn.close()

    def Delete_Ongles(self):
        Element = input("Quel est l'élément à supprimer dans les ongles ? ")

        conn = sqlite3.connect('popi.db')
        cursor = conn.cursor()

        cursor.execute("""DELETE FROM Ongles WHERE name=? """, (Element,))

        conn.commit()
        conn.close()

    def Delete_Maquillage(self):
        Element = input("Quel est l'élément à supprimer dans les maquillages ? ")

        conn = sqlite3.connect('popi.db')
        cursor = conn.cursor()

        cursor.execute("""DELETE FROM Maquillage WHERE name=? """, (Element,))

        conn.commit()
        conn.close()

    def Delete_Produit(self):
        Element = input("Quel est le produit à supprimer ? ")

        conn = sqlite3.connect('popi.db')
        cursor = conn.cursor()

        cursor.execute("""DELETE FROM Produits WHERE name=? """, (Element,))

        conn.commit()
        conn.close()

    def Delete_Charge(self):
        Element = input("Quelle est la charge à supprimer ? ")

        conn = sqlite3.connect('popi.db')
        cursor = conn.cursor()

        cursor.execute("""DELETE FROM Charges WHERE name=? """, (Element,))

        conn.commit()
        conn.close()

    def Delete_Journee(self):
        Element = input("Quelle est la journée à supprimer ? ")

        conn = sqlite3.connect('popi.db')
        cursor = conn.cursor()

        cursor.execute("""DELETE FROM Journees WHERE jour=? """, (Element,))

        conn.commit()
        conn.close()


class NewDay():
    Gain = 0
    Couts = 0

    def __init__(self):
        Nb_Serv = int(input("Combien de services aujourd'hui ? "))
        i = 0
        while i < Nb_Serv:
            Type_Serv = int(input(
                "\nQuelle catégorie ?\n\n1 - Soins du visage\n2 - Soins du corps\n3 - Epilations\n4 - Ongles\n5 - Maquillage\n6 - Produits\n"))

            if (Type_Serv == 1):
                self.Add_Soin_Visage()
            elif (Type_Serv == 2):
                self.Add_Soin_Corps()
            elif (Type_Serv == 3):
                self.Add_Epilation()
            elif (Type_Serv == 4):
                self.Add_Ongles()
            elif (Type_Serv == 5):
                self.Add_Maquillage()
            elif (Type_Serv == 6):
                self.Add_Produit()
            else:
                print("Mauvais numéro")
            i += 1

        print("Gain total = ", self.Gain)
        print("Cout total = ", self.Couts)
        self.Add_Day()

    def Add_Soin_Visage(self):
        conn = sqlite3.connect('popi.db')
        cursor = conn.cursor()

        Element = input("Quel est l'élément à ajouter pour cette journée (soins visages) ? ")

        cursor.execute("""SELECT price,cost FROM Soins_Visages WHERE name=? """, (Element,))
        rows = cursor.fetchall()

        if not rows:
            print("Liste vide")
        else:
            #print("Prix = ", rows[0][0])
            #print("Cout = ", rows[0][1])

            self.Gain = self.Gain + rows[0][0]
            print("Gain indiv = ", self.Gain)
            self.Couts = self.Couts + rows[0][1]

        conn.commit()
        conn.close()

    def Add_Soin_Corps(self):
        conn = sqlite3.connect('popi.db')
        cursor = conn.cursor()

        Element = input("Quel est l'élément à ajouter pour cette journée (soins corps) ? ")

        cursor.execute("""SELECT price,cost FROM Soins_Corps WHERE name=? """, (Element,))
        rows = cursor.fetchall()

        if not rows:
            print("Liste vide")
        else:
            # print("Prix = ", rows[0][0])
            # print("Cout = ", rows[0][1])

            self.Gain = self.Gain + rows[0][0]
            print("Gain indiv = ", self.Gain)
            self.Couts = self.Couts + rows[0][1]

        conn.commit()
        conn.close()

    def Add_Epilation(self):
        conn = sqlite3.connect('popi.db')
        cursor = conn.cursor()

        Element = input("Quel est l'élément à ajouter pour cette journée (épilations) ? ")

        cursor.execute("""SELECT price,cost FROM Epilations WHERE name=? """, (Element,))
        rows = cursor.fetchall()

        if not rows:
            print("Liste vide")
        else:
            # print("Prix = ", rows[0][0])
            # print("Cout = ", rows[0][1])

            self.Gain = self.Gain + rows[0][0]
            print("Gain indiv = ", self.Gain)
            self.Couts = self.Couts + rows[0][1]

        conn.commit()
        conn.close()

    def Add_Ongles(self):
        conn = sqlite3.connect('popi.db')
        cursor = conn.cursor()

        Element = input("Quel est l'élément à ajouter pour cette journée (Ongles) ? ")

        cursor.execute("""SELECT price,cost FROM Ongles WHERE name=? """, (Element,))
        rows = cursor.fetchall()

        if not rows:
            print("Liste vide")
        else:
            # print("Prix = ", rows[0][0])
            # print("Cout = ", rows[0][1])

            self.Gain = self.Gain + rows[0][0]
            print("Gain indiv = ", self.Gain)
            self.Couts = self.Couts + rows[0][1]

        conn.commit()
        conn.close()

    def Add_Maquillage(self):
        conn = sqlite3.connect('popi.db')
        cursor = conn.cursor()

        Element = input("Quel est l'élément à ajouter pour cette journée (Maquillage) ? ")

        cursor.execute("""SELECT price,cost FROM Maquillage WHERE name=? """, (Element,))
        rows = cursor.fetchall()

        if not rows:
            print("Liste vide")
        else:
            # print("Prix = ", rows[0][0])
            # print("Cout = ", rows[0][1])

            self.Gain = self.Gain + rows[0][0]
            print("Gain indiv = ", self.Gain)
            self.Couts = self.Couts + rows[0][1]

        conn.commit()
        conn.close()

    def Add_Produit(self):
        conn = sqlite3.connect('popi.db')
        cursor = conn.cursor()

        Element = input("Quel est l'élément à ajouter pour cette journée (Produits) ? ")

        cursor.execute("""SELECT price,cost FROM Produits WHERE name=? """, (Element,))
        rows = cursor.fetchall()

        if not rows:
            print("Liste vide")
        else:
            # print("Prix = ", rows[0][0])
            # print("Cout = ", rows[0][1])

            self.Gain = self.Gain + rows[0][0]
            print("Gain indiv = ", self.Gain)
            self.Couts = self.Couts + rows[0][1]

        conn.commit()
        conn.close()

    def Add_Day(self):
        Charge_journaliere = 0
        somme = 0
        j = 0
        Tab=[]

        conn = sqlite3.connect('popi.db')
        cursor = conn.cursor()

        cursor.execute("""SELECT cost FROM Charges """)
        row = [item[0] for item in cursor.fetchall()]

        #print("Charges = ",row)

        while j < len(row):
            somme = somme + float((row[j]))
            j += 1

        #print("somme =  ", somme)
        Charge_journaliere = float(somme / 25)
        print("\nCouts fixes = ", Charge_journaliere)
        print("CA de la journée = ",self.Gain)
        Tab.append(self.Gain)
        print("Couts variables = ",self.Couts)

        Couts_totaux = Charge_journaliere+self.Couts
        Tab.append(Couts_totaux)
        Resultat_net = self.Gain - Couts_totaux
        Tab.append(Resultat_net)

        print("Couts totaux = ",Couts_totaux)
        print("\nResultat net = ", Resultat_net)

        cursor.execute("""INSERT INTO Journees(ca,costs,result) VALUES(?,?,?)""", Tab)

        conn.commit()
        conn.close()
