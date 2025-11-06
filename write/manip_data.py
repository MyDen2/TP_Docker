from exceptions.InvalidAgeLimitException import InvalidAgeLimitException
from exceptions.InvalidYearException import InvalidYearException
from models.Movie import Movie
from models.Acteur import Acteur
import csv

def demander_infos_film(): 
    #exceptions pour titre et genre à ajouter plus tard
    titre = input("Quel est le titre du film ?")
    annee_production = input("Quel est la date de production du film ?")
    if not annee_production.isnumeric():
        raise InvalidYearException("La date doit être un nombre")
    genre = input("Quel est le genre du film ?")
    age_limite = input("Quel est l'âge limite du film ?")
    if not age_limite.isnumeric():
        raise InvalidAgeLimitException("La date doit être un nombre")
    movie = Movie(titre, annee_production, genre, age_limite)
    return movie

def ajouter_un_film():
    
    try : 
        new_movie = demander_infos_film()
    except InvalidYearException as e : 
        print(e)
    except InvalidAgeLimitException as e : 
        print(e)
    #exceptions pour titre et genre à ajouter plus tard

    # Nouvelle ligne à ajouter
    nouvelle_ligne = [f"{new_movie.id}", f"{new_movie.titre}", f"{new_movie.annee_production}", f"{new_movie.genre}", f"{new_movie.age_limite}"]

    # Ouvrir le fichier en mode ajout ('a') et écrire la ligne
    with open("data/movies.csv", mode='a', newline='', encoding='utf-8') as fichier:
        writer = csv.writer(fichier)
        writer.writerow(nouvelle_ligne)

def demander_id_film_a_modifier() -> int:
    id = input("Quel est l'id du film à modifier ?")
    if not id.isnumeric():
        raise Exception("L'id doit être un nombre")
    with open('data/movies.csv', "r") as f:
        data = list(csv.reader(f))
        print("Nb de lignes dans le fichier :", len(data))
        nb_films = len(data) - 1
    
    if 0 > int(id) > nb_films : 
        raise Exception("L'id ne correspond à aucun film") 
    
    return id


def modifier_un_film():

    try : 
        id = demander_id_film_a_modifier()
        try : 
            movie = demander_infos_film()    
        except InvalidYearException as e : 
            print(e)
        except InvalidAgeLimitException as e : 
            print(e)
    except Exception as e: 
        print(e)
    # Lire et modifier une ligne spécifique
    with open("data/movies.csv", mode='r', newline='', encoding='utf-8') as fichier:
        lignes = list(csv.reader(fichier))  # Charger toutes les lignes dans une liste

        lignes[int(id)][1] = movie.titre
        lignes[int(id)][2] = movie.annee_production
        lignes[int(id)][3] = movie.genre
        lignes[int(id)][4] = movie.age_limite


    # Réécrire le fichier avec les modifications
    with open("data/movies.csv", mode='w', newline='', encoding='utf-8') as fichier:
        writer = csv.writer(fichier)
        writer.writerows(lignes)

def supprimer_un_film(): 
    try : 
        id = demander_id_film_a_modifier()
    except Exception as e: 
        print(e)


    with open("data/movies.csv", "r", newline="", encoding="utf-8") as fichier:
        lignes = list(csv.reader(fichier))

    with open("data/movies.csv", "w", newline="", encoding="utf-8") as fichier:
        writer = csv.writer(fichier)
        for index, ligne in enumerate(lignes):
            if index != int(id):  # Exclure la ligne à supprimer
                writer.writerow(ligne)

def demander_infos_acteur():

    nom = input("Quel est le nom de l'acteur ?")
    prenom = input("Quel est le prénom de l'acteur ?")
    age = input("Quel est l'âge de l'acteur ?")
    if not age.isnumeric():
        raise InvalidAgeLimitException("L'âge doit être un nombre")
    acteur = Acteur(nom, prenom, age)
    return acteur


def ajouter_un_acteur():
    try : 
        new_actor = demander_infos_acteur()
    except InvalidAgeLimitException as e : 
        print(e)

    # Nouvelle ligne à ajouter
    nouvelle_ligne = [f"{new_actor.id}", f"{new_actor.nom}", f"{new_actor.prenom}", f"{new_actor.age}"]

    # Ouvrir le fichier en mode ajout ('a') et écrire la ligne
    with open("data/actors.csv", mode='a', newline='', encoding='utf-8') as fichier:
        writer = csv.writer(fichier)
        writer.writerow(nouvelle_ligne)

def associer_un_acteur_a_un_film():
    pass

def choix():
    print("---- Les actions ? ---- ")
    print("1- Ajouter un film")
    print("2- Modifier un film")
    print("3- Supprimer un film")
    print("4- Quitter")
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
            ajouter_un_film()
        case 2 : 
            modifier_un_film()
        case 3 : 
            supprimer_un_film()
        case 4 : 
            ajouter_un_acteur()
        case 5 : 
            exit()
        case _ : 
            print("Ce choix n'existe pas ! ")
        
