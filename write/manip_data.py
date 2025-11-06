from exceptions import InvalidAgeLimitException, InvalidYearException
from models import Movie
import csv

def demander_infos_film(self) -> Movie: 
    #exceptions pour titre et genre à ajouter plus tard
    titre = input("Quel est le titre du film à ajouter ?")
    annee_production = input("Quel est le titre du film à ajouter ?")
    if int(annee_production):
        raise InvalidYearException("La date doit être un nombre")
    genre = input("Quel est le titre du film à ajouter ?")
    age_limite = input("Quel est le titre du film à ajouter ?")
    if int(age_limite):
        raise InvalidAgeLimitException("La date doit être un nombre")
    return Movie(titre, annee_production, genre, age_limite)

def ajouter_un_film(self):
    
    try : 
        new_movie = demander_infos_film()
    except InvalidYearException as e : 
        print(e)
    except InvalidAgeLimitException as e : 
        print(e)
    #exceptions pour titre et genre à ajouter plus tard
    fichier = open("data/movies.csv", "wt", newline="", encoding="utf-8")
    ecrivainCSV = csv.writer(fichier, delimiter="|")                    
    ecrivainCSV.writerow(["id", "titre", "annee_production", "genre", "age_limite"])               
    ecrivainCSV.writerow([f"{new_movie.id}", f"{new_movie.titre}", f"{new_movie.annee_production}", f"{new_movie.genre}", f"{new_movie.age_limite}"])            
    fichier.close()

