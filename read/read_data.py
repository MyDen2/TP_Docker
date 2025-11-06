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

def recuperer_liste_films_grace_limite_age():
    liste_films = []
    age_limite = input("Quel est l'âge limite ?")
    if not age_limite.isnumeric():
        raise Exception("L'âge doit être un nombre !")
    
    with open("data/movies.csv", mode='r', encoding='utf-8') as fichier:
        lecteur = csv.reader(fichier)
        for index, ligne in enumerate(lecteur):
            if not ligne[4].isnumeric():
                pass
            else :
                if int(ligne[4]) <= int(age_limite):
                    liste_films.append(ligne)
    print(liste_films)
            
def recuperer_liste_films_grace_genre():
    liste_films_genre =[]
    genre = input("Quel est le genre ?")
    
    with open("data/movies.csv", mode='r', encoding='utf-8') as fichier:
        lecteur = csv.reader(fichier)
        for index, ligne in enumerate(lecteur):
            if ligne[3].lower() == genre.lower():
                liste_films_genre.append(ligne)
    print(liste_films_genre)
