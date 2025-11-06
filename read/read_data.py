import csv

def recuperer_un_film_grace_au_titre():
    titre = input("Quel est le titre du film ?").lower()
    #exception à mettre
    
    with open("data/movies.csv", mode='r', encoding='utf-8') as fichier:
        lecteur = csv.reader(fichier)
        #for index, ligne in enumerate(lecteur, start=1):
        for ligne in enumerate(lecteur, start=1):
            if ligne[1].lower() == titre:
                print(f"ID : {ligne[0]}")
                print(f"Titre : {ligne[1]}")
                print(f"Année de production : {ligne[2]}")
                print(f"Genre : {ligne[3]}")
                print(f"Age conseillé : {ligne[4]}")
                break
