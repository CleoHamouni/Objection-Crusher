import streamlit as st

st.set_page_config(page_title="Objection Crusher", layout="wide")

st.markdown("""
    <style>
    .obj-box { background-color: #fff4f4; padding: 15px; border-radius: 10px; border-left: 5px solid #ff4b4b; margin-bottom: 20px; }
    .res-box { background-color: #f0fff4; padding: 15px; border-radius: 10px; border-left: 5px solid #28a745; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Objection Crusher Pro")

# Variables de réponses pour éviter les lignes trop longues
R1 = "Je comprends. On ne cherche pas a remplacer vos fournisseurs, mais a proposer une expertise de niche."
R2 = "Comment faites-vous quand vos fournisseurs ne trouvent pas le profil critique ?"
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

# Dictionnaire simplifié
obj_dict = {
    "Referencement": [R1, R2],
    "Deja un concurrent": [R3, R4],
    "Barrage / Mail": [R5],
    "Pas de budget": [R6],
    "Rappelez dans 6 mois": [R7, R8],
    "Trop de sollicitations": [R9],
    "Pas une priorite": [R10],
    "Pas le decideur": [R11, R12]
}

choix = st.selectbox("⚠️ Selectionnez l'objection :", ["Choisir..."] + list(obj_dict.keys()))

if choix != "Choisir...":
    st.markdown(f'<div class="obj-box"><b>Objection :</b> {choix}</div>', unsafe_allow_html=True)
    for r in obj_dict[choix]:
        st.markdown(f'<div class="res-box">{r}</div>', unsafe_allow_html=True)

st.divider()
st.info("💡 Conseil : Transformez toujours l'objection en question ouverte.")
