import json
import csv

# Ouverture du fichier json des adresses visitées exportées via Google Maps
f=open("D:/USERS/Poirier_Lu/Desktop/adresses.json", encoding="utf8")

# Chargement du fichier json avec la fonction json.load
data=json.load(f)

# Affichage des différentes clés de la bibliothèque
data.keys()

# On récupère les valeurs de la clé "features" qu'on insère dans une liste
features = data["features"]

### Quelques print
# Affichage des clés de la sous clé "properties"
print(features[0]["properties"].keys())
# Affichage des valeurs de la clé "Location" contenue dans la clé "properties"
print(features[0]["properties"]["Location"].values())
# Affichage de la première valeur de la liste
print(features[0])

### On veut récupérer les valeurs des clés : Title, Latitude, Longitude

coordinates=[element["geometry"]["coordinates"] for element in features]
coordinates

titles=[element["properties"]["Title"] for element in features]

# Dans la liste des titles, on va remplacer les "," par "", car le "," est notre séparateur dans csv
titles_news=[]
for i in titles:
    titles_new=i.replace(",","")
    titles_news.append(titles_new)

# Liste qui concatène les titres et coordonnées
concat=[]
for i in range(len(titles)):
    concat.append([titles[i]] + coordinates[i])
concat

# On ne récupère que les valeurs dont les objets sont situés dans un carré autour de la ville
liste_finale=[]
for i in range(len(concat)):
    if concat[i][1]>4.2 and concat[i][1]<4.5 and concat[i][2]>50.7 and concat[i][2]<50.9:
        liste_finale.append(concat[i])

### Export de la liste en csv

# Définition des entêtes 
fields = ['Title', 'lon', 'lat'] 
    
# Enregistrement des entêtes et de la liste
with open('D:/USERS/Poirier_Lu/Desktop/adresses.csv', 'w', newline='') as f:
    # using csv.writer method from CSV package
    write = csv.writer(f, delimiter=';')
    write.writerow(fields)
    write.writerows(liste_finale)
