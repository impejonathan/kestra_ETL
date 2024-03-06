import os
from dotenv import load_dotenv
import pyodbc

# Charger les variables d'environnement
load_dotenv()

server = os.getenv('DB_SERVER')
database = os.getenv('DB_DATABASE')
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')

driver= '{ODBC Driver 17 for SQL Server}'

cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

# Copier les données de la table Produit à Produit_clone
cursor.execute("SET IDENTITY_INSERT Produit_clone ON")
cursor.execute("""
INSERT INTO Produit_clone (ID_Produit, URL_Produit, Prix, Info_generale, Descriptif, Note, Date_scrap, Marque)
SELECT ID_Produit, URL_Produit, Prix, Info_generale, Descriptif, Note, Date_scrap, Marque FROM Produit
""")
cursor.execute("SET IDENTITY_INSERT Produit_clone OFF")

# Copier les données de la table Caracteristiques à Caracteristiques_clone
cursor.execute("SET IDENTITY_INSERT Caracteristiques_clone ON")
cursor.execute("""
INSERT INTO Caracteristiques_clone (ID_Caracteristique, Consommation, Indice_Pluie, Bruit, Saisonalite, Type_Vehicule, Runflat, ID_Produit)
SELECT ID_Caracteristique, Consommation, Indice_Pluie, Bruit, Saisonalite, Type_Vehicule, Runflat, ID_Produit FROM Caracteristiques
""")
cursor.execute("SET IDENTITY_INSERT Caracteristiques_clone OFF")

# Copier les données de la table Dimensions à Dimensions_clone
cursor.execute("SET IDENTITY_INSERT Dimensions_clone ON")
cursor.execute("""
INSERT INTO Dimensions_clone (ID_Dimension, Largeur, Hauteur, Diametre, Charge, Vitesse, ID_Produit)
SELECT ID_Dimension, Largeur, Hauteur, Diametre, Charge, Vitesse, ID_Produit FROM Dimensions
""")
cursor.execute("SET IDENTITY_INSERT Dimensions_clone OFF")

# Valider les modifications
cnxn.commit()

# Fermer la connexion
cnxn.close()
