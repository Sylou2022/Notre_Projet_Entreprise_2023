import streamlit as st
import pandas as pd
import webbrowser
import datetime
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from matplotlib import pyplot as plt

# st.set_option('browser.gatherUsageStats', False)

def load_data(nrows):
    fichier2 = st.file_uploader('telecharger votre fichier ici', type='csv', key='n2')
    if fichier2 is not None: 
        data = pd.read_csv(fichier2, sep=';')
        data['Date'] = pd.to_datetime(data['Date'])
        return data

def main():
    st.set_page_config(page_title="Projet-Entreprise", page_icon="🧊")

    background_css = """
        <style>
        body {
            background-color: green;
        }

        .stApp {
            background-color: #ffffff;
            background-color: #FFFFFF;
        }

        .sidebar .sidebar-content {
            background-color: #C0C0C0;
        }
        </style>
    """

    st.markdown(background_css, unsafe_allow_html=True)

    fichier = st.file_uploader('telecharger votre fichier ici', type='csv')
    if fichier is not None:
        data = load_data(2336)
        data = pd.read_csv(fichier, sep=';')
        data['Date'] = pd.to_datetime(data['Date'])
        st.sidebar.header("Menu")

        selected_option = st.sidebar.selectbox("", ["Accueil", "Carte des agences", "Pourcentages des Etoiles" ,"Tableau de données", "Nombre d'avis positifs par ville /année", "Qualité de services par Ville","Taux des avis par ville", "Les Scores par ville","Entrainement du modèle NLP"])

        if selected_option == "Accueil":
            st.markdown("<h1 style='color: #000000;'>Tableau de Bord</h1>", unsafe_allow_html=True)
            st.markdown("<h2 style='color: #000000;'>Bienvenue dans Projet Entreprise</h2>", unsafe_allow_html=True)
            
        elif selected_option == "Carte des agences":
            webbrowser.open('carte_pole_emploi.html')
        
        elif selected_option == "Pourcentages des Etoiles":
            st.markdown("<h2 style='color: #000000;'>Somme des Etoiles en %</h2>", unsafe_allow_html=True)
            st.markdown("La répartition en pourcentage des différentes catégories d'étoiles. Les résultats montrent que 1 étoile représente 56,5% dépassant la moyenne. Ce graphique met en évidence la prédominance de la catégorie 1 étoile. ", unsafe_allow_html=True)
            Labels = ["\u2605", '\u2605\u2605', '\u2605\u2605\u2605', '\u2605\u2605\u2605\u2605', '\u2605\u2605\u2605\u2605\u2605']
            sizes = [1305, 104, 131, 154, 616]
            color = ['#ff0000', '#ffa700', '#fff400', '#a3ff00', '#2cba00']

            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, colors=color, labels=Labels, autopct='%1.1f%%', startangle=90)

            centre_circle = plt.Circle((0, 0), 0.70, fc='white')
            fig = plt.gcf()
            fig.gca().add_artist(centre_circle)

            ax1.axis('equal')
            plt.tight_layout()
            st.pyplot(fig1)

        elif selected_option == "Tableau de données":
            st.markdown("<h2 style='color: #000000;'>Données brutes</h2>", unsafe_allow_html=True)
            st.write(data)
        
        elif selected_option == "Nombre d'avis positifs par ville /année":
            st.markdown("<h2 style='color: #000000;'>Nombre d'avis positifs par ville et par année</h2>", unsafe_allow_html=True)
            st.markdown("Ce graphique montre le nombre total d'avis positifs par ville et par année. Il nous permet de voir les villes et les années avec le plus grand nombre d'avis positifs.", unsafe_allow_html=True)

            fig2 = px.bar(data, x="Ville", y="Nombre d'avis positifs", color="Année", barmode="group")
            st.plotly_chart(fig2)

        elif selected_option == "Qualité de services par Ville":
            st.markdown("<h2 style='color: #000000;'>Qualité de services par Ville</h2>", unsafe_allow_html=True)
            st.markdown("Ce graphique montre la qualité des services par ville. Chaque ville est représentée par une note moyenne calculée à partir des avis des utilisateurs.", unsafe_allow_html=True)

            fig3 = px.bar(data, x="Ville", y="Note moyenne", color="Ville")
            st.plotly_chart(fig3)

        elif selected_option == "Taux des avis par ville":
            st.markdown("<h2 style='color: #000000;'>Taux des avis par ville</h2>", unsafe_allow_html=True)
            st.markdown("Ce graphique montre le taux des différents types d'avis (positif, négatif, neutre) par ville. Il nous permet de voir la répartition des avis par ville.", unsafe_allow_html=True)

            fig4 = px.bar(data, x="Ville", y=["Pourcentage d'avis positifs", "Pourcentage d'avis négatifs", "Pourcentage d'avis neutres"], barmode="stack")
            st.plotly_chart(fig4)

        elif selected_option == "Les Scores par ville":
            st.markdown("<h2 style='color: #000000;'>Scores par ville</h2>", unsafe_allow_html=True)
            st.markdown("Ce graphique montre les scores attribués à chaque ville en fonction de différents critères. Les scores sont calculés à partir des avis des utilisateurs.", unsafe_allow_html=True)

            fig5 = make_subplots(rows=1, cols=3, subplot_titles=("Score Qualité", "Score Ponctualité", "Score Amabilité"))

            fig5.add_trace(go.Bar(x=data["Ville"], y=data["Score Qualité"], name="Score Qualité"), row=1, col=1)
            fig5.add_trace(go.Bar(x=data["Ville"], y=data["Score Ponctualité"], name="Score Ponctualité"), row=1, col=2)
            fig5.add_trace(go.Bar(x=data["Ville"], y=data["Score Amabilité"], name="Score Amabilité"), row=1, col=3)

            fig5.update_layout(showlegend=False)
            st.plotly_chart(fig5)

        elif selected_option == "Entrainement du modèle NLP":
            st.markdown("<h2 style='color: #000000;'>Entrainement du modèle NLP</h2>", unsafe_allow_html=True)
            st.markdown("Section réservée à l'entraînement du modèle de traitement du langage naturel (NLP).", unsafe_allow_html=True)
        
        st.sidebar.markdown("<h3 style='color: #000000;'>Informations</h3>", unsafe_allow_html=True)
        st.sidebar.markdown("<p style='color: #000000;'>Application développée par <b>XYZ</b></p>", unsafe_allow_html=True)

if __name__ == '__main__':
    main()