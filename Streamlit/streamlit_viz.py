import streamlit as st
import pandas as pd
import webbrowser
import datetime
import plotly.express as px
from plotly.subplots import make_subplots
from menu.score_ville import score_ville
from menu.avis_positif_annee import avis_positif_annee
from menu.avis_prc_ville import avis_prc_ville
from menu.qual_serv_ville import qual_serv_ville
from menu.etoile_periode import etoile_periode
from menu.tab_data import tab_data
from menu.pourcentage_etoiles import prc_etoile
from menu.accueil import accueil

# def main():

#     # Déplacer st.set_page_config() comme première commande Streamlit
#     st.set_page_config(page_title="Projet-Entreprise", page_icon="🧊")
    
    
    
    
    
#     # Définir le style CSS pour l'arrière-plan
#     background_css = (
#         """
#         <style>
#         body {
#             background-color: green; /* Couleur d'arrière-plan */
#         }

#         .stApp {

#             background-color: #ffffff /* Couleur de la barre de menu */

#             background-color: #FFFFFF /* Couleur de la barre de menu */
#         }
        
#         .sidebar .sidebar-content {
#             background-color: #C0C0C0; /* Couleur de fond du menu à gauche de l'écran */
#         }

#         </style>
#         """
#     )

#     # Afficher le style CSS personnalisé
#     st.markdown(background_css, unsafe_allow_html=True)
    
#     fichier = st.file_uploader('telecharger votre fichier ici', type='csv')
    
    
#     data = load_data(2336)  
#     # data = pd.read_csv('../Data/csv/Île-de-France_POLE EMPLOI.csv', sep=';')
#     data = pd.read_csv(fichier, sep=';')


#     # data = load_data(2336)  
#     # data = pd.read_csv('../Data/csv/Île-de-France_POLE EMPLOI.csv', nrows=2336, sep=';')
#     data = pd.read_csv(fichier, sep=';')
#     data['Date'] = pd.to_datetime(data['Date'])
#     st.sidebar.header("Menu")
    
#     # data = pd.read_csv('Data/Île-de-France_POLE EMPLOI.csv', sep=';')

#     selected_option = st.sidebar.selectbox("", ["Accueil", "Carte des agences", "Pourcentages des Etoiles" ,"Tableau de données", "Nombre d'avis positifs par ville /année", "Qualité de services par Ville","Taux des avis par ville", "Les Scores par ville","Entrainement du modèle NLP"])

#     if selected_option == "Accueil":
#         accueil()
        
#     elif selected_option == "Carte des agences":
        
#         # URL de la page de la carte des agences
#         webbrowser.open('carte_pole_emploi.html')
    
#     elif selected_option == "Pourcentages des Etoiles":
#         prc_etoile()
    
#     elif selected_option == "Tableau de données":
#         tab_data()
        
#     elif selected_option == "Nombre d'avis positifs par ville /année":
#         avis_positif_annee()
        
#     elif selected_option == "Qualité de services par Ville":
#         qual_serv_ville()
        
#     elif selected_option == "Taux des avis par ville":
#         avis_prc_ville()
        
#     elif selected_option == "Les Scores par ville":
#         score_ville()
     
#     elif selected_option == "Nombre d'étoiles par période":
#         etoile_periode()

#     elif selected_option == "Total avis en % par ville":
#        avis_prc_ville()
       
#     # elif selected_option == "Taux etoile par ville":
#     #     test()
        
        
        
       
#     elif selected_option == "Entrainement du modèle NLP":
#         # st.title("CLASSIFICATION D'AVIS")
#         webbrowser.open('https://sylou2022-nlp-projet-entreprise-nlpmain-p1v3s2.streamlit.app/')
        
        
        
        
            



def load_data(nrows):
    
    # data = pd.read_csv('../Data/csv/Île-de-France_POLE_EMPLOI_copie.csv', nrows=nrows, sep=';')
    
    fichier2 = st.file_uploader('telecharger votre fichier ici', type='csv',key='n2')
    if fichier2 is not None: 
        
        data = pd.read_csv(fichier2, sep=';')
        
        
        
        # data = upload_file()
        data['Date'] = pd.to_datetime(data['Date'])
        return data

# def upload_file():
    
#     fichier1 = st.file_uploader('telecharger votre fichier ici', type='csv', key='n1')
#     return fichier1


def main():

    # Déplacer st.set_page_config() comme première commande Streamlit
    st.set_page_config(page_title="Projet-Entreprise", page_icon="🧊")

    # Définir le style CSS pour l'arrière-plan
    background_css = """
        <style>
        body {
            background-color: green; /* Couleur d'arrière-plan */
        }

        .stApp {
            background-color: #ffffff; /* Couleur de la barre de menu */
            background-color: #FFFFFF; /* Couleur de la barre de menu */
        }

        .sidebar .sidebar-content {
            background-color: #C0C0C0; /* Couleur de fond du menu à gauche de l'écran */
        }
        </style>
    """
    

    # Afficher le style CSS personnalisé
    st.markdown(background_css, unsafe_allow_html=True)

    fichier = st.file_uploader('telecharger votre fichier ici', type='csv')
    if fichier is not None:
        
        data = load_data(2336)  
        # data = pd.read_csv('../Data/csv/Île-de-France_POLE EMPLOI.csv', sep=';')
        data = pd.read_csv(fichier, sep=';')
        data['Date'] = pd.to_datetime(data['Date'])
        st.sidebar.header("Menu")

        # Reste du code...
        # data = pd.read_csv('Data/Île-de-France_POLE EMPLOI.csv', sep=';')

        selected_option = st.sidebar.selectbox("", ["Accueil", "Carte des agences", "Pourcentages des Etoiles" ,"Tableau de données", "Nombre d'avis positifs par ville /année", "Qualité de services par Ville","Taux des avis par ville", "Les Scores par ville","Entrainement du modèle NLP"])

        if selected_option == "Accueil":
            accueil()
            
        elif selected_option == "Carte des agences":
            
            # URL de la page de la carte des agences
            webbrowser.open('carte_pole_emploi.html')
        
        elif selected_option == "Pourcentages des Etoiles":
            prc_etoile()
        
        elif selected_option == "Tableau de données":
            tab_data()
            
        elif selected_option == "Nombre d'avis positifs par ville /année":
            avis_positif_annee()
            
        elif selected_option == "Qualité de services par Ville":
            qual_serv_ville()
            
        elif selected_option == "Taux des avis par ville":
            avis_prc_ville()
            
        elif selected_option == "Les Scores par ville":
            score_ville()
        
        elif selected_option == "Nombre d'étoiles par période":
            etoile_periode()

        elif selected_option == "Total avis en % par ville":
            avis_prc_ville()          
            
            
        
        elif selected_option == "Entrainement du modèle NLP":
            # st.title("CLASSIFICATION D'AVIS")
            webbrowser.open('https://sylou2022-nlp-projet-entreprise-nlpmain-p1v3s2.streamlit.app/')


if __name__ == '__main__':
    main()
