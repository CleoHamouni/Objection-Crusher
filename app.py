import streamlit as st

st.set_page_config(page_title="Objection Crusher IA", page_icon="🛡️", layout="wide")

# --- STYLE ---
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
    .main { background-color: #f5f7f9; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Objection Crusher Pro")
st.markdown("Gardez le contrôle de vos appels de prospection face aux refus classiques.")

# --- BASE DE DONNÉES DES OBJECTIONS ---
objections = {
    "Trop de sollicitations": {
        "text": "On reçoit déjà trop d'appels de cabinets ou d'ESN comme vous.",
        "responses": [
            "🎯 **Le différenciateur :** 'Je me doute bien, une entreprise comme la vôtre est forcément très courtisée. Si je me permets de vous appeler malgré tout, c'est que j'ai une approche spécifique sur [Expertise de niche] qui nous permet d'avoir des profils que les généralistes ne touchent pas. On en parle 2 minutes ?'",
            "💎 **L'humilité :** 'C'est justement pour ça que je serai bref. Je ne cherche pas à être votre 10ème partenaire, mais celui que vous appelez quand les 9 autres n'ont pas trouvé la solution. Quelle est votre compétence la plus difficile à sourcer en ce moment ?'"
        ]
    },
    "Rappelez plus tard (Timing)": {
        "text": "Rappelez-moi dans 3 ou 6 mois, là ce n'est pas le moment.",
        "responses": [
            "📅 **L'anticipation :** 'Je note la date ! Mais pour que mon appel dans 6 mois soit vraiment utile, est-ce que votre priorité sera plutôt sur le renfort d'équipe ou sur un nouveau projet technologique ?'",
            "🚀 **Le 'Quick Win' :** 'Entendu. Juste avant de raccrocher, si je tombe sur la perle rare en [Techno] d'ici là, je vous passe un petit coup de fil ou vous préférez rester strictement sur dans 6 mois ?'"
        ]
    },
    "Pas de budget": {
        "text": "On n'a pas de budget pour de l'assistance technique ou du recrutement en ce
