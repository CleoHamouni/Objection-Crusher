import streamlit as st

st.set_page_config(page_title="Objection Crusher Pro", layout="wide")

st.markdown("""
    <style>
    .obj-box { background-color: #fff4f4; padding: 15px; border-radius: 10px; border-left: 5px solid #ff4b4b; margin-bottom: 20px; }
    .res-box { background-color: #f0fff4; padding: 15px; border-radius: 10px; border-left: 5px solid #28a745; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Objection Crusher Pro")

# Variables de réponses (méthode robuste anti-bug)
R1 = "Je comprends. On ne cherche pas a remplacer vos fournisseurs, mais a proposer une expertise de niche."
R2 = "Comment faites-vous quand vos fournisseurs ne trouvent pas le profil critique ?"
R3 = "C'est un excellent choix. Nos clients aiment avoir un deuxieme point de comparaison pour rester agiles."
R4 = "Mon but est d'etre votre solution numero 2 quand votre partenaire est en tension. On en parle ?"
R5 = "Je le fais avec plaisir. Pour que ce mail soit utile, quels sont vos 2 profils les plus durs a trouver ?"
R6 = "Je comprends. Mon but n'est pas de vendre aujourd'hui, mais d'anticiper vos futurs arbitrages."
R7 = "C'est note ! Pour que mon appel soit utile dans 6 mois, quelle sera votre priorite a ce moment-la ?"
R8 = "Si je trouve une perle rare d'ici la, je vous fais un signe ou on attend vraiment 6 mois ?"
R9 = "Je ne cherche pas a etre votre 10eme
