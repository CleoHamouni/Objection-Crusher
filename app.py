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

# 3. Données
obj_dict = {
    "Trop de sollicitations": [
        "🎯 Je me doute bien. Je ne cherche pas à être votre 10ème partenaire, mais celui que vous appelez quand les autres sèchent. Quelle est votre compétence la plus dure à trouver ?",
        "💎 Mon approche est spécialisée sur une niche précise. Puis-je vous envoyer un seul profil pertinent pour tester notre réactivité ?"
    ],
    "Rappelez plus tard": [
        "📅 Je note ! Pour que mon appel soit utile dans 6 mois, votre priorité sera plutôt sur du renfort d'équipe ou un nouveau projet ?",
        "🚀 Si je croise la perle rare d'ici là, je vous fais un signe rapide ou on attend vraiment 6 mois ?"
    ],
    "Pas de budget": [
        "💰 Je comprends. Mon but n'est pas de vendre aujourd'hui, mais de me faire connaître pour vos futurs arbitrages. On se voit 10 min pour anticiper l'année prochaine ?",
        "💡 Parfois, le manque de budget cache un coût interne trop élevé. Nos modèles agiles permettent de débloquer des situations sans exploser vos budgets."
    ],
    "Pas une priorité": [
        "📍 Je comprends. Du coup, quel est le sujet qui occupe 80% de votre temps actuellement ?",
        "⏳ On peut rester en contact ? Je vous envoie une étude de cas, et vous reviendrez vers moi quand le sujet remontera dans la pile."
    ],
    "Pas le décideur": [
        "🤝 Merci de me l'indiquer ! Pour m'éviter de déranger la mauvaise personne, qui gère ce sujet chez vous ?",
        "🔄 Est-ce que c'est vous qui validez l'aspect technique avant la décision ? Ça vaudrait le coup d'échanger 5 min ensemble d'abord."
    ]
}

# 4. Interface
choix = st.selectbox("Sélectionnez l'objection :", ["Choisir..."] + list(obj_dict.keys()))

if choix != "Choisir...":
    st.markdown(f'<div class="obj-box"><b>L\'objection :</b> "{choix}"</div>', unsafe_allow_html=True)
    st.subheader("Comment rebondir :")
    for r in obj_dict[choix]:
        # La ligne ci-dessous est maintenant bien refermée avec )
        st.markdown(f'<div class="res-box">{r}</div>', unsafe_allow_html=True)

st.divider()
st.info("💡 Conseil : Ne justifiez jamais, rebondissez par une question.")
