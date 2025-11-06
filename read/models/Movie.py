class Movie():
    id = 31

    def init(self, titre: str, annee_production: int, genre: str, age_limite: int):
        Movie.id += 1
        self.titre = titre
        self.annee_production = annee_production
        self.genre = genre
        self.age_limite = age_limite

    def __str__(self):
        print("Informations sur ce film")
        print(f"Titre : {self.titre}")
        print(f"Année de production : {self.annee_production}")
        print(f"Genre : {self.genre}")
        print(f"Age limite : {self.age_limite}")