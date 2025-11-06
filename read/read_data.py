import csv

def recuperer_un_film_grace_au_titre():
    titre = input("Quel est le titre du film ?").lower()
    #exception à mettre
    
    with open("data/movies.csv", mode='r', encoding='utf-8') as fichier:
        lecteur = csv.reader(fichier)
        #for index, ligne in enumerate(lecteur, start=1):
        for index, ligne in enumerate(lecteur, start=1):
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

def recuperer_liste_entre_deux_annees():
    liste_films_annees =[]
    annee1 = input("Quel est la première année ?")
    annee2 = input("Quel est la deuxième année ?")
    if (not annee1.isnumeric()) | (not annee2.isnumeric()):
        raise Exception("Les années doivent être un nombre !")
    
    with open("data/movies.csv", mode='r', encoding='utf-8') as fichier:
        lecteur = csv.reader(fichier)
        for index, ligne in enumerate(lecteur):
            if not ligne[2].isnumeric():
                pass
            else: 
                if annee1 <= ligne[2] <= annee2:
                    liste_films_annees.append(ligne)
    print(liste_films_annees)


def choix():
    print("---- Les actions ? ---- ")
    print("1- Récupérer un film grâce au titre")
    print("2- Récupérer une liste de films grâce à une limite d'âge")
    print("3- Récupérer une liste de films grâce au genre")
    print("4- Récupérer une liste de films grâce à deux dates")
    print("5- Quitter")
    reponse = input("Quel est votre choix ?")
    if not reponse.isnumeric():
        raise Exception("Le choix doit etre un nombre ")
    return int(reponse)

while True:
    reponse = 0
    try : 
        reponse = choix()
    except Exception as e: 
        print(e)
    
    match reponse: 
        case 1 : 
            recuperer_un_film_grace_au_titre()
        case 2 : 
            recuperer_liste_films_grace_limite_age()
        case 3 : 
            recuperer_liste_films_grace_genre()
        case 4 : 
            recuperer_liste_entre_deux_annees()
        case 5 : 
            exit()
        case _ : 
            print("Ce choix n'existe pas ! ")