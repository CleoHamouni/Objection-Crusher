import streamlit as st

# 1. Configuration de la page
st.set_page_config(page_title="Objection Crusher IA", page_icon="🛡️", layout="wide")

# 2. Style visuel
st.markdown("""
    <style>
    .objection-box {
        background-color: #fff4f4;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #ff4b4b;
        margin-bottom: 20px;
    }
    .response-box {
        background-color: #f0fff4;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #28a745;
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Objection Crusher Pro")
st.markdown("L'outil pour ne plus jamais rester sans voix en prospection.")

# 3. Base de données des objections
# Note : Chaque texte est sur une seule ligne pour éviter les erreurs Python
objections = {
    "Trop de sollicitations": {
        "text": "On reçoit déjà trop d'appels de cabinets ou d'ESN comme vous.",
        "responses": [
            "🎯 **Le différenciateur :** Je me doute bien, c'est le signe que vous êtes attractifs. Justement, je ne cherche pas à être votre 10ème partenaire, mais celui que vous appelez quand les 9 autres n'ont pas trouvé la solution. Quelle est votre compétence la plus pénurique ?",
            "💎 **L'humilité :** Je serai très bref pour respecter votre temps. Mon approche est spécialisée sur [Votre Niche]. Puis-je vous envoyer un seul profil pertinent pour tester notre réactivité ?"
        ]
