# TP_Docker

🏗️ 1. Récupération du projet
📦 Cloner le repository
# Cloner le repository depuis GitHub
git clone https://github.com/MyDen2/TP_Docker.git


🪜 Structure finale attendue
tp/
├── docker-compose.yml
├── read/
│   ├── Dockerfile
│   ├── data/
│   │   └── movies.csv
│   ├── models/
│   │   └── Movie.py
│   └── read_data.py
└── write/
    ├── Dockerfile
    ├── data/
    │   └── movies.csv
    ├── exceptions/
    │   ├── InvalidAgeLimitException.py
    │   ├── InvalidGenreException.py
    │   ├── InvalidTitleException.py
    │   └── InvalidYearException.py
    ├── models/
    │   └── Movie.py
    └── manip_data.py

🧱 2. Dockerisation du projet
🐳 Dockerfile – Read
# read/Dockerfile
FROM python:latest

WORKDIR home/myriam

COPY . .

# RUN pip install flask

EXPOSE 5000

CMD ["tail", "-f", "/dev/null"]

🐳 Dockerfile – Write
# write/Dockerfile
FROM python:latest

WORKDIR home/myriam

COPY . .

EXPOSE 5000

CMD ["tail", "-f", "/dev/null"]

⚙️ 3. Docker Compose
services:

  read_service:
    # L'image docker à utiliser pour ce service (ici, la version officiel de mysql)
    container_name: read_python
    build:
      context: ./read
      dockerfile: Dockerfile
    # Politique de rédémarrage du conteneur. "always" signifie que le conteneur redémarrera automatique si il venait à s'arreter. 
    # Montages de volume pour persister les données entre le redémarrages des conteneurs.
    volumes: 
      - data_volume:/home/myriam/data

  write_service:
    container_name: write_python
    build:
      context: ./write
      dockerfile: Dockerfile
    volumes: 
      - data_volume:/home/myriam/data

# Déclarations des volumes utilisé dans les services
volumes:
  # Volume nommée "db_data" pour stocker les données de la bdd MySql
  data_volume:


Le volume partagé data_volume permet aux deux conteneurs d’avoir accès au même fichier movies.csv.

🎬 4. Classe Movie
📄 models/Movie.py
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

🚨 5. Exceptions personnalisées
📄 Exemple : InvalidTitleException.py
class InvalidTitleException(Exception):
    pass
   


Même logique pour :

InvalidYearException

InvalidGenreException

InvalidAgeLimitException

✏️ 6. Script d’écriture – manip_data.py
Fonctionnalités
➕ Ajouter un film
def ajouter_un_film():
    

✏️ Modifier un film
def modifier_un_film():
    

❌ Supprimer un film
def supprimer_un_film():
  

📖 7. Script de lecture – read_data.py
🔍 Récupérer un film par son titre
def recuperer_un_film_grace_au_titre():

👶 Filtrer par âge limite
def recuperer_liste_films_grace_limite_age():

🎭 Filtrer par genre
def recuperer_liste_films_grace_genre():
   

📅 Filtrer entre deux années
def recuperer_liste_entre_deux_annees():
    

🧪 8. Tests Docker
🏗️ Construire les images
docker compose build

▶️ Lancer les conteneurs
docker compose up

📋 Exemple d’exécution
➕ Ajouter un film (conteneur write)
docker compose run write
Titre : Inception
Année de production : 2010
Genre : Science-Fiction
Âge limite : 13
✅ Film ajouté : 31 - Inception (2010) | Science-Fiction | Âge limite : 13+

🔍 Lire les films (conteneur read)
docker compose run read
>>> recuperer_liste_films_grace_genre()
31,Inception,2010,Science-Fiction,13

🧾 9. Validation et Git Workflow
Étape	Action	Commandes
🔧	Créer une branche pour une fonctionnalité	git checkout -b feature/ajout-film
💾	Ajouter et valider	git add . && git commit -m "Ajout fonction ajouter_film"
🔁	Fusionner dans main	git checkout main && git merge feature/ajout-film
🚀	Pousser vers GitHub	git push origin main
🧭 10. Résumé
Élément	Fonction
manip_data.py	Gérer le fichier CSV (CRUD)
read_data.py	Lire et filtrer les films
Dockerfile	Construire les conteneurs Python
docker-compose.yml	Lancer les deux conteneurs avec un volume partagé
exceptions	Gérer les erreurs utilisateurs
models/Movie.py	Définir la structure des films
