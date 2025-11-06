class Movie:
    id = 30

    def __init__(self, titre: str, annee_production: int, genre: str, age_limite: int):
        Movie.id += 1
        self.titre = titre
        self.annee_production = annee_production
        self.genre = genre
        self.age_limite = age_limite

    def __str__(self):
        chaine = "Informations sur ce film \n" + f"ID du film : {self.id} \n" + f"Titre : {self.titre} \n" + f"Année de production : {self.annee_production} \n" + f"Genre : {self.genre} \n" + f"Age limite : {self.age_limite} \n" 
        return chaine