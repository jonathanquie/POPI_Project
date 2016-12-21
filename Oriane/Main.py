import Database

while True:
	Type = input("\n\nQuelle opération désirez-vous ?\nAjout d'un élément : Tapez N\nVoir les éléments : Tapez V\nSupprimer un élément : Tapez S\nNouvelle Journée : Tapez J\n\nQuitter le programme : Tapez Q\n\n")
	Database.NewDatabase()
	if(Type == 'N' or Type == 'n'):
		Database.NewEntry()
	elif(Type == 'V' or Type == 'v'):
		Database.ViewDatabases()
	elif(Type == 'S' or Type == 's'):
		Database.DeleteElement()
	elif(Type == 'J' or Type == 'j'):
		Database.NewDay()	
	elif(Type == 'q' or Type == 'Q'):
		break
	else:
		print("Commande inconnue, veuillez recommencer.\n")

