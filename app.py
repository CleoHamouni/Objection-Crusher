import streamlit as st

# 1. Config
st.set_page_config(page_title="Objection Crusher", layout="wide")

# 2. Style
st.markdown("""
    <style>
    .obj-box { background-color: #fff4f4; padding: 15px; border-radius: 10px; border-left: 5px solid #ff4b4b; margin-bottom: 20px; }
    .res-box { background-color: #f0fff4; padding: 15px; border-radius: 10px; border-left: 5px solid #28a745; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Objection Crusher Pro")

# 3. Données avec format multi-lignes pour éviter les SyntaxError
obj_dict = {
    "Trop de sollicitations": [
        """Differentiateur : Je me doute bien. Je ne cherche pas a etre votre 10eme partenaire, mais celui que vous appelez quand les autres sechent. Quelle est votre competence la plus dure a trouver ?""",
        """Expertise : Mon approche est specialisee sur une niche precise. Puis-je vous envoyer un seul profil pertinent pour tester notre reactivite ?"""
    ],
    "Rappelez plus tard": [
        """Anticipation : Je note ! Pour que mon appel soit utile dans 6 mois, votre priorite sera plutot sur du renfort d'equipe ou un nouveau projet ?""",
        """Quick Win : Si je croise la perle rare d'ici la, je vous fais un signe rapide ou on attend vraiment 6 mois ?"""
    ],
    "Pas de budget": [
        """Long terme : Je comprends. Mon but n'est pas de vendre aujourd'hui, mais de me faire connaitre pour vos futurs arbitrages. On se voit 10 min pour anticiper l'annee prochaine ?""",
        """Efficacite : Parfois, le manque de budget cache un cout interne trop eleve. Nos modeles agiles permettent de debloquer des situations sans exploser vos budgets fixes."""
    ],
    "Pas une priorite": [
        """Curiosite : Je comprends. Du coup, quel est le sujet qui occupe 80% de votre temps actuellement ?""",
        """Veille : On peut rester en contact ? Je vous envoie une etude de cas, et vous reviendrez vers moi quand le sujet remontera dans la pile."""
    ],
    "Pas le decideur": [
        """Allie : Merci de me l'indiquer ! Pour m'eviter de deranger la mauvaise personne, qui gere ce sujet chez vous ?""",
        """Double approche : Est-ce que c'est vous qui validez l'aspect technique avant la decision ? Ca vaudrait le coup d'echanger 5 min ensemble d'abord."""
    ]
}

# 4. Interface
choix = st.selectbox("Selectionnez l'objection :", ["Choisir..."] + list(obj_dict.keys()))

if choix != "Choisir...":
    st.markdown(f'<div class="obj-box"><b>L\'objection :</b> "{choix}"</div>', unsafe_allow_html=True)
    st.subheader("Comment rebondir :")
    for r in obj_dict[choix]:
        st.markdown(f'<div class="res-box">{r}</div>', unsafe_allow_html=True
