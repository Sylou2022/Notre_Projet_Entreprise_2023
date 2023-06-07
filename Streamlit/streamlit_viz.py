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
import plotly.graph_objects as go
from matplotlib import pyplot as plt

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
        
        
        
        
            
st.set_option('browser.gatherUsageStats', False)



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
   
            
            st.markdown("<h1 style='color: #000000;'>Tableau de Bord</h1>", unsafe_allow_html=True)
            st.markdown("<h2 style='color: #000000;'>Bienvenue dans Projet Entreprise</h2>", unsafe_allow_html=True)
            
        elif selected_option == "Carte des agences":
            
            # URL de la page de la carte des agences
            webbrowser.open('carte_pole_emploi.html')
        
        elif selected_option == "Pourcentages des Etoiles":
            st.markdown("<h2 style='color: #000000;'>Somme des Etoiles en %</h2>", unsafe_allow_html=True)
            st.markdown("La répartition en pourcentage des différentes catégories d'étoiles. Les résultats montrent que 1 étoile représente 56,5% dépassant la moyenne. Ce graphique met en évidence la prédominance de la catégorie 1 étoile. ", unsafe_allow_html=True)
            Labels = ["\u2605", '\u2605\u2605', '\u2605\u2605\u2605', '\u2605\u2605\u2605\u2605', '\u2605\u2605\u2605\u2605\u2605']
            sizes = [1305, 104, 131, 154, 616]
            color = ['#ff0000', '#ffa700', '#fff400', '#a3ff00', '#2cba00']

            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, colors=color, labels=Labels, autopct='%1.1f%%', startangle=90)

            # Cercle de dessin
            centre_circle = plt.Circle((0, 0), 0.70, fc='white')
            fig = plt.gcf()
            fig.gca().add_artist(centre_circle)

            # Le rapport hauteur / largeur égal garantit que la tarte est dessinée sous forme de cercle
            ax1.axis('equal')
            plt.tight_layout()
            st.pyplot(fig)  

        elif selected_option == "Tableau de données":
            st.markdown("<h2 style='color: #000000;'>Tableau de données</h2>", unsafe_allow_html=True)
            st.markdown("Le tableau de données obtenu après le scraping contient plus de 2300 lignes", unsafe_allow_html=True)
            data = pd.read_csv('../Data/csv/Île-de-France_POLE_EMPLOI_copie.csv', nrows=2337, sep=';')
            data['Date'] = pd.to_datetime(data['Date'])
            st.write(data)
            
        elif selected_option == "Nombre d'avis positifs par ville /année":
            
             # Charger les données depuis le fichier CSV
            df = pd.read_csv('../Data/csv/avi.csv', sep=';')

            # Extraire l'année à partir de la colonne "Date de publication"
            df['Year'] = pd.to_datetime(df['Date de publication'], format='%d/%m/%Y').dt.strftime('%Y')

            # Récupérer toutes les années du CSV
            annees = df['Year'].unique()

            st.markdown("<h6 >Visualisation de l'évolution des avis positifs au fil des années et comparaison des différentes villes. L’analyse sur la satisfaction des utilisateurs dans chaque ville.Les variations temporelles et géographiques des avis positifs.</h6>", unsafe_allow_html=True)
            # Sélection de la ville via le dropdown
            selected_ville = st.selectbox('Sélectionnez une ville', df['Ville'].unique())

            # Filtrer les données pour la ville sélectionnée
            positifs_par_ville = df[df['Ville'] == selected_ville]
            positifs_par_ville = positifs_par_ville[positifs_par_ville['Type'] == 'Positif'].groupby(['Year']).size().reset_index(name='Count')

            # Créer le graphique en courbe
            fig = px.line(positifs_par_ville, x='Year', y='Count')
            

            # Mise en forme du layout du graphique
            fig.update_layout(title=f'Représentation du nombre d\'avis positifs par année pour la ville : {selected_ville}',


            yaxis_title='Nombre d\'avis positifs')
            fig.update_xaxes(title_text='Année',dtick=1)
            
            fig.update_yaxes(title_text='Nombre d\'avis positifs',dtick=1)

            # Afficher le graphique en courbe
            st.plotly_chart(fig)
            
        elif selected_option == "Qualité de services par Ville":
            # Charger les données depuis le fichier CSV
            df = pd.read_csv('../Data/csv/taux_ville.csv', sep=';')

            st.markdown("<h6 >Représentation de la qualité des services par villes en fonction des avis. Perception des utilisateurs et l’identification des villes ayant les meilleurs et les moins bons résultats en termes de satisfaction des services. Analyse comparative et mise en évidence des variations entre les différentes localités.</h6>", unsafe_allow_html=True)

            # Sélection de la colonne "Ville" via le dropdown
            selected_ville = st.selectbox('Sélectionnez une ville', df['Ville'].unique())

            # Filtrer les données pour la ville sélectionnée
            ville_data = df[df['Ville'] == selected_ville]

            # Récupérer les nombres d'avis positifs, négatifs et neutres
            avis_positifs = ville_data["Nombre d’avis Positif"].iloc[0]
            avis_negatifs = ville_data["Nombre d’avis négatif"].iloc[0]
            avis_neutres = ville_data["Nombre d’avis Neutre"].iloc[0]

            # Créer les données pour le graphique en barres
            categories = ['Avis positifs', 'Avis négatifs', 'Avis neutres']
            values = [avis_positifs, avis_negatifs, avis_neutres]
            colors = ['green', 'red', 'yellow']

            # Créer le graphique en barres
            fig = go.Figure(data=[go.Bar(x=categories, y=values, marker=dict(color=colors))])

            # Mise en forme du layout du graphique en barres
            fig.update_layout(title='Qualité de service pour la ville : ' + selected_ville,
                xaxis_title='Types d\'avis',
                yaxis_title='Nombre d\'avis')

            # Afficher le graphique en barres
            st.plotly_chart(fig)
            
        elif selected_option == "Taux des avis par ville":
        
                    # Charger les données des scores des villes d'Île-de-France
            datafr = pd.read_csv('../Data/csv/taux_ville.csv', sep=';')

            # Créer une liste des options de sélection pour le dropdown
            villes = datafr['Ville'].unique()
            
            st.markdown("<h6>La répartition des avis par ville et l’observation des préférences et opinions des utilisateurs. La visualisation claire des proportions relatives des avis positifs, négatifs et neutres, facilitant ainsi la détection de tendances et de disparités entre les villes en termes de satisfaction des services.</h6>", unsafe_allow_html=True)

            # Sélection de la ville via le dropdown
            selected_ville = st.selectbox('Sélectionnez une ville', villes)

            # Filtrer les données pour la ville sélectionnée
            ville_data = datafr[datafr['Ville'] == selected_ville]

            # Récupérer le nombre d'avis négatifs, positifs et neutres
            avis_negatifs = ville_data["Nombre d’avis négatif"].iloc[0]
            avis_positifs = ville_data["Nombre d’avis Positif"].iloc[0]
            avis_neutres = ville_data["Nombre d’avis Neutre"].iloc[0]

            # Calculer le pourcentage des avis négatifs, positifs et neutres
            total_avis = avis_negatifs + avis_positifs + avis_neutres
            pourcentage_negatifs = (avis_negatifs / total_avis) * 100
            pourcentage_positifs = (avis_positifs / total_avis) * 100
            pourcentage_neutres = (avis_neutres / total_avis) * 100

            # Créer une figure en utilisant le graphique semi-circulaire de Plotly pour les avis
            fig_avis = go.Figure()

            # Ajouter une trace semi-circulaire pour les avis négatifs
            fig_avis.add_trace(go.Indicator(
                mode="gauge+number",
                value=pourcentage_negatifs,
                domain={'x': [0, 0.3], 'y': [0, 1]},
                title={'text': '% Avis négatifs'},
                gauge={'axis': {'range': [0, 100]},
                    'bar': {'color': 'red'},
                    'steps': [{'range': [0, 50], 'color': 'red'}],
                    'threshold': {'line': {'color': 'black', 'width': 4}, 'thickness': 0.75, 'value': pourcentage_negatifs}}))

            # Ajouter une trace semi-circulaire pour les avis positifs
            fig_avis.add_trace(go.Indicator(
                mode="gauge+number",
                value=pourcentage_positifs,
                domain={'x': [0.35, 0.65], 'y': [0, 1]},
                title={'text': '% Avis positifs'},
                gauge={'axis': {'range': [0, 100]},
                    'bar': {'color': 'green'},
                    'steps': [{'range': [0, 50], 'color': 'green'}],
                    'threshold': {'line': {'color': 'black', 'width': 4}, 'thickness': 0.75, 'value': pourcentage_positifs}}))


            # Ajouter une trace semi-circulaire pour les avis neutres
            fig_avis.add_trace(go.Indicator(
                mode="gauge+number",
                value=pourcentage_neutres,
                domain={'x': [0.7, 1], 'y': [0, 1]},
                title={'text': ' % Avis neutres'},
                gauge={'axis': {'range': [0, 100]},
                    'bar': {'color': 'blue'},
                    'steps': [{'range': [0, 50], 'color': 'blue'}],
                    'threshold': {'line': {'color': 'black', 'width': 4}, 'thickness': 0.75, 'value': pourcentage_neutres}}))

            # Créer une figure en utilisant le graphique semi-circulaire de Plotly pour la performance totale
            fig_performance = go.Figure()

            # Calculer la performance totale en pourcentage
            performance_totale = (avis_positifs / total_avis) * 100

            # Ajouter une trace semi-circulaire pour la performance totale
            fig_performance.add_trace(go.Indicator(
                mode="gauge+number",
                value=performance_totale,
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': 'Etude Comparative - Performance totale'},
                gauge={'axis': {'range': [0, 100]},
                    'bar': {'color': 'purple'},
                    'steps': [{'range': [0, 100], 'color': 'purple'}],
                    'threshold': {'line': {'color': 'black', 'width': 4}, 'thickness': 0.75, 'value': performance_totale}}))

            # Mise en forme du layout des graphiques
            fig_avis.update_layout(height=400, width=600, margin=dict(l=20, r=20, t=30, b=20))
            # fig_performance.update_layout(height=400, width=400, margin=dict(l=20, r=20, t=30, b=20))

            # Afficher les graphiques
            st.plotly_chart(fig_avis, use_container_width=True)
            # st.plotly_chart(fig_performance, use_container_width=True)
            
        elif selected_option == "Les Scores par ville":
            datafr = pd.read_csv('../Data/csv/taux_ville.csv', sep=';')
            # Créer une liste des options de sélection pour le dropdown
            villes = datafr['Ville'].unique()


            st.markdown("<h6>Représentation visuelle des quantités d'avis positifs, négatifs et neutres dans chaque ville à travers des données brutes. Etablir une étude approfondie pour identifier les tendances et les disparités entres les villes en termes de satisfaction de services.</h6>", unsafe_allow_html=True)

            # Sélection de la ville via le dropdown
            selected_ville = st.selectbox('Sélectionnez une ville', villes)

            # Filtrer les données pour la ville sélectionnée
            ville_data = datafr[datafr['Ville'] == selected_ville]

            # Récupérer le nombre d'avis négatifs, positifs et neutres
            avis_positifs = ville_data["Nombre d’avis Positif"].iloc[0]
            avis_negatifs = ville_data["Nombre d’avis négatif"].iloc[0]        
            avis_neutres = ville_data["Nombre d’avis Neutre"].iloc[0]


            score_positifs = avis_positifs
            score_negatifs = avis_negatifs       
            score_neutres = avis_neutres

            # Créer une figure en utilisant le graphique semi-circulaire de Plotly pour les avis
            fig_avis = go.Figure()


            # Ajouter une trace semi-circulaire pour les avis positifs
            fig_avis.add_trace(go.Indicator(
            mode="gauge+number",
            value=score_positifs,
            domain={'x': [0.35, 0.65], 'y': [0, 1]},
            title={'text': 'Avis positifs'},
            gauge={'axis': {'range': [0, 100]},
            'bar': {'color': 'green'},
            'steps': [{'range': [0, 50], 'color': 'green'}],
            'threshold': {'line': {'color': 'black', 'width': 4}, 'thickness': 0.75, 'value': score_positifs}}))


            # Ajouter une trace semi-circulaire pour les avis négatifs
            fig_avis.add_trace(go.Indicator(
            mode="gauge+number",
            value=score_negatifs,
            domain={'x': [0, 0.3], 'y': [0, 1]},
            title={'text': 'Avis négatifs'},
            gauge={'axis': {'range': [0, 100]},
            'bar': {'color': 'red'},
            'steps': [{'range': [0, 50], 'color': 'red'}],
            'threshold': {'line': {'color': 'black', 'width': 4}, 'thickness': 0.75, 'value': score_negatifs}}))


            # Ajouter une trace semi-circulaire pour les avis neutres
            fig_avis.add_trace(go.Indicator(
            mode="gauge+number",
            value=score_neutres,
            domain={'x': [0.7, 1], 'y': [0, 1]},
            title={'text': ' Avis neutres'},
            gauge={'axis': {'range': [0, 100]},
            'bar': {'color': 'blue'},
            'steps': [{'range': [0, 50], 'color': 'yellow'}],
            'threshold': {'line': {'color': 'black', 'width': 4}, 'thickness': 0.75, 'value': score_neutres}}))


            # Mise en forme du layout des graphiques
            fig_avis.update_layout(height=400, width=600, margin=dict(l=20, r=20, t=30, b=20))


            # Afficher les graphiques
            st.plotly_chart(fig_avis, use_container_width=True)
        
        elif selected_option == "Nombre d'étoiles par période":
            dfm = pd.read_csv('../Data/csv/Île-de-France_POLE_EMPLOI_copie.csv', sep=';')
            st.subheader('Nombre Etoiles par période')

            # Convertir les valeurs float en str dans la colonne "Date"
            dfm['Date'] = dfm['Date'].apply(lambda x: str(x) if isinstance(x, float) else x)

            # Exclure les valeurs 'nan' de la colonne "Date"
            dfm = dfm.dropna(subset=['Date'])

            # Appliquer la fonction strptime() en gérant les exceptions pour les valeurs non valides
            dfm['ParsedDate'] = dfm['Date'].apply(lambda x: pd.NaT if x == 'nan' else datetime.datetime.strptime(x, "%d/%m/%Y") if isinstance(x, str) else pd.NaT)

            # Supprimer les lignes avec des valeurs non valides
            dfm = dfm.dropna(subset=['ParsedDate'])

            # Regrouper par année et calculer la somme des étoiles
            etoiles_sum = dfm.groupby(dfm['ParsedDate'].dt.year)['Etoile'].sum()

            periodes = etoiles_sum.index
            etoiles = etoiles_sum.values

            fig = plt.figure()
            plt.plot(periodes, etoiles, label='Nombre Etoiles')
            plt.xlabel('Années')
            plt.ylabel('Somme des étoiles')
            plt.legend()
            plt.xticks(periodes, labels=[str(year) for year in periodes])  # Afficher les années au format "2023"
            st.pyplot(fig)

        elif selected_option == "Total avis en % par ville":
            avis_prc_ville()          
            
            
        
        elif selected_option == "Entrainement du modèle NLP":
            # st.title("CLASSIFICATION D'AVIS")
            webbrowser.open('https://sylou2022-nlp-projet-entreprise-nlpmain-p1v3s2.streamlit.app/')


if __name__ == '__main__':
    main()
