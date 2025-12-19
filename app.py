import streamlit as st

# 1. Configuration de la page
st.set_page_config(page_title="Objection Crusher", layout="wide")

# 2. Style CSS
st.markdown("""
    <style>
    .obj-box { background-color: #fff4f4; padding: 15px; border-radius: 10px; border-left: 5px solid #ff4b4b; margin-bottom: 20px; }
    .res-box { background-color: #f0fff4; padding: 15px; border-radius: 10px; border-left: 5px solid #28a745; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Objection Crusher Pro")

# 3. Base de données ultra-sécurisée (une seule ligne par texte)
obj_dict = {
    "Referencement / Accord Cadre": [
        "Je comprends. La plupart de mes clients ont des accords cadres. Je ne cherche pas a les remplacer, mais a vous presenter une expertise de niche.",
        "Comment faites-vous aujourd'hui quand vos fournisseurs ne trouvent pas le profil critique dont vous avez besoin ?"
    ],
    "Deja un concurrent": [
        "C'est un excellent choix. Generalement, nos clients aiment avoir un deuxieme point de comparaison pour rester agiles.",
        "Mon but est d'etre votre solution numero 2 quand votre partenaire habituel est en tension. On en parle 5 minutes ?"
    ],
    "Barrage / Envoi de mail": [
        "Je le fais avec plaisir. Pour que ce mail soit utile, quels sont les 2 profils techniques les plus durs a recruter pour vous ?",
        "Je vous l'envoie de suite. On se bloque 5 min mardi pour voir ce qui a retenu votre attention ?"
    ],
    "Pas de budget": [
        "Je comprends. Mon but n'est pas de vendre aujourd'hui, mais de me faire connaitre pour vos futurs arbitrages.",
        "Parfois, nos modeles agiles permettent de debloquer des projets sans impacter vos budgets fixes de fonctionnement."
    ],
    "Rappelez dans 6 mois": [
        "C'est note !
