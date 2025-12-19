import streamlit as st

st.set_page_config(page_title="Objection Crusher IA", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .objection-box { background-color: #fff4f4; padding: 20px; border-radius: 10px; border-left: 5px solid #ff4b4b; margin-bottom: 20px; }
    .response-box { background-color: #f0fff4; padding: 20px; border-radius: 10px; border-left: 5px solid #28a745; margin-bottom: 15px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Objection Crusher Pro")

# --- BASE DE DONNÉES ---
objections = {
    "Trop de sollicitations": {
        "text": "On reçoit déjà trop d'appels de cabinets ou d'ESN comme vous.",
        "responses": [
            "🎯 **Le différenciateur :** Je me doute bien. Si je vous appelle malgré tout, c'est que j'ai une approche spécifique sur une expertise de niche. On en parle 2 minutes ?",
            "💎 **L'humilité :** C'est pour ça que je serai bref. Je ne cherche pas à être votre 10ème partenaire, mais celui que vous appelez quand les autres ne trouvent pas."
        ]
    },
    "Rappelez plus tard": {
        "text": "Rappelez-moi dans 3 ou 6 mois, là ce n'est pas le moment.",
        "responses": [
            "📅 **L'anticipation :** Je note ! Pour que mon appel soit utile dans 6 mois, votre priorité sera plutôt sur du renfort d'équipe ou un nouveau projet ?",
            "🚀 **Le 'Quick Win' :** Entendu. Si je tombe sur la perle rare d'ici là, je vous passe un petit coup de fil ou vous préférez attendre 6 mois ?"
        ]
    },
    "Pas de budget": {
        "text": "On n'a pas de budget pour de l'assistance technique en ce moment.",
        "responses": [
            "💰 **Le long terme :** Je comprends. Mon but n'est pas de vendre une prestation immédiate, mais de me faire connaître pour vos futurs arbitrages.",
            "💡 **L'investissement :** Parfois, le manque de budget vient d'un coût trop élevé en interne. On a des solutions agiles qui débloquent ces situations."
        ]
    },
    "Pas une priorité": {
        "text": "Ce n'est pas une priorité pour nous en ce moment.",
        "responses": [
            "📍 **La curiosité :** C'est très clair. Du coup, quel est le gros sujet qui occupe 80% de votre temps actuellement ?",
            "⏳ **La veille :** On peut simplement rester en veille ? Je vous envoie une étude de cas, et vous me direz quand le sujet reviendra sur la pile."
        ]
    },
    "Pas le décideur": {
        "text": "Je ne suis pas la bonne personne / ce n'est pas moi qui décide.",
        "responses": [
            "🤝 **L'allié :** Merci de me l'indiquer ! Pour m'éviter de déranger la mauvaise personne, qui gère ce sujet chez vous ?",
            "🔄 **La double approche :** D'accord. Est-ce que c'est vous qui exprimez le besoin technique avant la décision ? Ça vaudrait le coup d'échanger d'abord."
        ]
    }
}

# --- INTERFACE ---
choix = st.selectbox("Sélectionnez l'objection :", ["Choisir..."] + list(objections.keys()))

if choix != "Choisir...":
    st.markdown(f'<div class="objection-box"><b>L\'objection :</b> "{objections[choix]["text"]}"</div>', unsafe_allow_html=True)
    for resp in objections[choix]["responses"]:
        st
