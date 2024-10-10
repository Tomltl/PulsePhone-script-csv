import pandas as pd

# Chargement des fichiers CSV
fichier1 = pd.read_csv('Mobile_Phones_Best_Sellers.csv')
fichier2 = pd.read_csv('Mobile_Phones_2020.csv')

# Renommer les colonnes du fichier 2 pour correspondre à celles du fichier 1
fichier2.rename(columns={'Phone': 'model', 'Company': 'manufacturer', 'Sold(million)': 'units_sold_m'}, inplace=True)

# Ajouter les colonnes manquantes dans fichier2 avec les valeurs par défaut
fichier2['form'] = 'Touchscreen'       # Remplir 'form' avec 'Touchscreen'
fichier2['smartphone'] = 'Yes'         # Remplir 'smartphone' avec 'Yes'
fichier2['year'] = 2020                # Remplir 'year' avec 2020

# Supprimer la colonne "No" qui est associée à 'smartphone' dans fichier2 (si elle existe)
if 'No' in fichier2.columns:
    fichier2 = fichier2.drop(columns=['No'])

# Fusion des deux fichiers CSV
fusion = pd.concat([fichier1, fichier2], ignore_index=True)

# Sauvegarder le fichier fusionné
fusion.to_csv('fichier_fusionne.csv', index=False)

print("Fusion terminée et enregistrée sous 'fichier_fusionne.csv'.")

