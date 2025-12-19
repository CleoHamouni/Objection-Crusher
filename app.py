import streamlit as st

st.set_page_config(page_title="Objection Crusher IA", page_icon="🛡️", layout="wide")

# --- STYLE ---
st.markdown("""
    <style>
    .objection-box {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #ff4b4b;
        margin-bottom: 20px;
    }
    .response-box {
        background-color: #e8f4ea;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #28a745;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Objection Crusher - Spécial IA")
st.markdown("Transformez les refus clients en opportunités de rendez-vous.")

# --- BASE DE DONNÉES DES OBJECTIONS ---
objections = {
    "Le Référencement (L'Accord Cadre)": {
        "text": "On a déjà une liste de fournisseurs référencés, on ne peut pas travailler avec vous.",
        "responses": [
            "🎯 **Le contournement :** 'Je comprends tout à fait. La plupart de mes clients actuels ont aussi des accords cadres. Justement, je ne vous appelle pas pour remplacer vos fournisseurs, mais pour vous présenter une expertise de niche qu'ils n'ont peut-être pas en ce moment. On en parle 10 min ?'",
            "💎 **L'angle expertise :** 'C'est justement parce que vous avez des processus stricts que mon profil [Expertise] pourrait vous intéresser en secours sur vos projets critiques. Comment faites-vous quand vos fournisseurs habituels ne trouvent pas le bon profil ?'"
        ]
    },
    "Le Travail avec un Concurrent": {
        "text": "On travaille déjà avec Alten/Altran/Capgemini et ça se passe très bien.",
        "responses": [
            "🤝 **La saine concurrence :** 'C'est une excellente nouvelle, ce sont des acteurs de qualité. Généralement, nos clients aiment avoir un deuxième point de comparaison pour rester agiles sur les tarifs et la réactivité. Quel est le dernier profil qu'ils n'ont pas réussi à vous trouver ?'",
            "⚡ **La réactivité :** 'Très bien ! Mon objectif n'est pas de les remplacer, mais d'être votre solution n°2 quand ils sont en tension de staffing. Puis-je vous envoyer notre dernier dossier de compétences pour que vous l'ayez sous le coude ?'"
        ]
    },
    "Le Timing (Pas le temps)": {
        "text": "Je n'ai pas le temps là, rappelez-moi dans 3 ou 6 mois.",
        "responses": [
            "⏳ **Le décalage intelligent :** 'Je comprends, vous êtes en plein rush. Si je vous appelle aujourd'hui, c'est justement pour anticiper vos besoins de dans 3 mois et vous éviter le stress du recrutement de dernière minute. On se prend 5 min mardi matin ou vous préférez jeudi ?'",
            "🚀 **La curiosité :** 'Entendu. Juste une question avant que je vous laisse : quel sera votre projet prioritaire dans 6 mois ? Cela me permettra de vous envoyer uniquement des infos pertinentes d'ici là.'"
        ]
    },
    "L'Envoi de mail (Le Barrage)": {
        "text": "Envoyez-moi une présentation par mail, je reviendrai vers vous.",
        "responses": [
            "📧 **Le mail qualifié :** 'Je le fais avec plaisir. Pour que je ne vous envoie pas une énième plaquette commerciale inutile, quels sont les 2 types de profils techniques que vous avez le plus de mal à recruter en ce moment ?'",
            "📞 **L'engagement :** 'Je vous l'envoie de ce pas. Généralement, après lecture, mes interlocuteurs ont 2 ou 3 questions précises. On se bloque 5 min mardi à 10h pour faire le point sur ce que vous en avez pensé ?'"
        ]
    }
}

# --- INTERFACE ---
st.subheader("⚠️ Choisissez l'objection que vous venez d'entendre :")
choix = st.selectbox("", list(objections.keys()))

if choix:
    st.markdown(f'<div class="objection-box"><b>L\'objection :</b> "{objections[choix]["text"]}"</div>', unsafe_allow_html=True)
    
    st.subheader("✅ Réponses suggérées :")
    for resp in objections[choix]["responses"]:
        st.markdown(f'<div class="response-box">{resp}</div>', unsafe_allow_html=True)
        st.write("")

st.divider()
st.info("💡 **Conseil d'IA :** Le secret n'est pas dans les mots, mais dans le ton. Restez calme, souriant (ça s'entend au téléphone) et n'argumentez jamais, rebondissez !")
