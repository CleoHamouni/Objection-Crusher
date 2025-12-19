import streamlit as st

# 1. Configuration
st.set_page_config(page_title="Objection Crusher Pro", layout="wide", page_icon="🛡️")

# 2. Style
st.markdown("""
    <style>
    .obj-box { background-color: #fff4f4; padding: 15px; border-radius: 10px; border-left: 5px solid #ff4b4b; margin-bottom: 20px; }
    .res-box { background-color: #f0fff4; padding: 15px; border-radius: 10px; border-left: 5px solid #28a745; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Objection Crusher - Version Intégrale")

# 3. Base de données complète
obj_dict = {
    "Référencement / Accord Cadre": [
        "🎯 Je comprends. La plupart de mes clients ont des accords cadres. Je ne vous appelle pas pour les remplacer, mais pour vous présenter une expertise de niche.",
        "💎 Comment faites-vous aujourd'hui quand vos fournisseurs référencés ne trouvent pas le profil critique dont vous avez besoin ?"
    ],
    "Déjà un concurrent (Alten, Cap, etc.)": [
        "🤝 C'est un excellent choix. Généralement, nos clients aiment avoir un deuxième point de comparaison pour rester agiles.",
        "⚡ Mon but est d'être votre solution n°2 quand votre partenaire habituel est en tension de staffing. On en parle 5 minutes ?"
    ],
    "Barrage Secrétaire / Envoi de mail": [
        "📧 Je le fais avec plaisir. Pour que je ne vous envoie pas une plaquette inutile, quels sont les 2 profils techniques les plus durs à recruter ?",
        "📞 Je vous l'envoie de suite. On se bloque 5 min mardi pour voir ce qui a retenu votre attention dans notre approche ?"
    ],
    "Pas de budget / Pas d'externe": [
        "💰 Je comprends. Mon but n'est pas de vendre aujourd'hui, mais de me faire connaître pour vos futurs arbitrages.",
        "💡 Parfois, nos modèles agiles permettent de débloquer des projets critiques sans impacter vos budgets fixes."
    ],
    "Rappelez dans 6 mois": [
        "📅 C'est noté ! Pour que mon appel soit utile dans 6 mois, votre priorité sera plutôt sur du renfort d'équipe ou sur un nouveau projet ?",
        "🚀 Si je trouve une perle rare qui correspond pile à votre stack d'ici là, je vous fais un
