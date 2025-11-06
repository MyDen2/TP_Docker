class Acteur:
    id = 11

    def __init__(self, nom: str, prenom: str, age: int):
        Acteur.id +=1
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def __str__(self):
        chaine = "Informations sur cet acteur \n" + f"Nom de l'acteur : {self.nom} \n" + f"Prénom de l'acteur : {self.prenom} \n" + f"Age de l'acteur : {self.age} \n"
        return chaine