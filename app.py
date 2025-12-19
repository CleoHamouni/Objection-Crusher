import streamlit as st

# 1. Configuration de la page
st.set_page_config(page_title="Objection Crusher Pro", layout="wide", page_icon="🛡️")

# 2. Style visuel (CSS)
st.markdown("""
    <style>
    .obj-box { background-color: #fff4f4; padding: 15px; border-radius: 10px; border-left: 5px solid #ff4b4b; margin-bottom: 20px; }
    .res-box { background-color: #f0fff4; padding: 15px; border-radius: 10px; border-left: 5px solid #28a745; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Objection Crusher Pro")

# 3. Variables de réponses (Méthode robuste anti-SyntaxError)
R1 = "Je comprends. On ne cherche pas a remplacer vos fournisseurs, mais a proposer une expertise de niche."
R2 = "Comment faites-vous quand vos fournisseurs ne trouvent pas le profil critique dont vous avez besoin ?"
R3 = "C'est un excellent choix. Nos clients aiment avoir un deuxieme point de comparaison pour rester agiles."
R4 = "Mon but est d'etre votre solution numero 2 quand votre partenaire est en tension. On en parle ?"
R5 = "Je le fais avec plaisir. Pour que ce mail soit utile, quels sont vos 2 profils les plus durs a trouver ?"
R6 = "Je comprends. Mon but n'est pas de vendre aujourd'hui, mais d'anticiper vos futurs arbitrages."
R7 = "C'est note ! Pour que mon appel soit utile dans 6 mois, quelle sera votre priorite a ce moment-la ?"
R8 = "Si je trouve une perle rare d'ici la, je vous fais un signe ou on attend vraiment 6 mois ?"
R9 = "Je ne cherche pas a etre votre 10eme partenaire, mais celui que vous appelez quand les 9 autres sechent."
R10 = "Quel est le sujet majeur qui occupe 80% de votre temps actuellement ?"
R11 = "Qui gere generalement ces sujets chez vous pour que je ne derange pas la mauvaise personne ?"
R12 = "Est-ce que c'est vous qui validez l'aspect technique avant que la decision monte au-dessus ?"
R13 = "Je serai tres bref, 60 secondes montre en main. Avez-vous un projet critique qui stagne faute de ressources ?"
R14 = "Je comprends votre rush. Est-ce que je vous rappelle mardi a 14h ou est-ce que jeudi matin vous convient mieux ?"
R15 = "C'est parfait ! Mon objectif n'est pas de changer ce qui marche, mais de vous montrer notre valeur ajoutee."

# 4. Dictionnaire des objections
obj_dict = {
    "Pas le temps / En plein rush": [R13, R14],
    "Referencement / Accord cadre": [R1, R2],
    "Deja un concurrent (Alten, Cap, etc.)": [R3, R4],
    "Barrage Secretaire / Envoi de mail": [R5],
    "Pas de budget / Pas d'externe": [R6],
    "Rappelez dans 6 mois": [R7, R8],
    "Trop de sollicitations": [R9],
    "Pas une priorite": [R10],
    "Pas le decideur": [R11, R12],
    "Tout va bien / Satisfait": [R15]
}

# 5. Interface Utilisateur
choix = st.selectbox("⚠️ Selectionnez l'objection entendue au telephone :", ["Choisir une objection..."] + list(obj_dict.keys()))

if choix != "Choisir une objection...":
    st.markdown(f'<div class="obj-box"><b>L\'objection client :</b> {choix}</div>', unsafe_allow_html=True)
    st.subheader("✅ Comment rebondir immédiatement :")
    for r in obj_dict[choix]:
        st.markdown(f'<div class="res-box">{r}</div>', unsafe_allow_html=True)

st.divider()
st.info("💡 Conseil d'IA : Le secret est de ne jamais argumenter, mais de poser une question pour reprendre le controle.")
