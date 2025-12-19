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

# 3. Données simplifiées
obj_dict = {
    "Trop de sollicitations": [
        "🎯 Différenciateur : Je me doute bien. Je ne cherche pas à être votre 10ème partenaire, mais celui que vous appelez quand les 9 autres sèchent. Quelle est votre compétence la plus dure à trouver ?",
        "💎 Expertise : Mon approche est spécialisée sur une niche précise. Puis-je vous envoyer un seul profil pertinent pour tester notre réactivité ?"
    ],
    "Rappelez plus tard": [
        "📅 Anticipation : Je note ! Pour que mon appel soit utile dans 6 mois, votre priorité sera plutôt sur du renfort d'équipe ou un nouveau projet ?",
        "🚀 Quick Win : Si je croise la perle rare d'ici là, je vous fais un signe rapide ou on attend vraiment 6 mois ?"
    ],
    "Pas de budget": [
        "💰 Long terme : Je comprends. Mon but n'est pas de vendre aujourd'hui, mais de me faire connaître pour vos futurs arbitrages. On se voit 10 min pour anticiper l'année prochaine ?",
        "💡 Efficacité : Parfois, le manque de budget cache un coût interne trop élevé. Nos modèles agiles permettent de débloquer des situations sans exploser vos budgets fixes."
    ],
    "Pas une priorité": [
        "📍 Curiosité : Je comprends. Du coup, quel est le sujet qui occupe 80% de votre temps actuellement ?",
        "⏳ Veille : On peut rester en contact ? Je vous envoie une étude de cas, et vous reviendrez vers moi quand le sujet remontera dans la pile."
    ],
    "Pas le décideur": [
        "🤝 Allié : Merci de me l'indiquer ! Pour m'éviter de déranger la mauvaise personne, qui gère ce sujet chez vous ?",
        "🔄 Double approche : Est-ce que c'est vous qui validez l
