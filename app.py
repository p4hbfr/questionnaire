import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Questionnaire TGR", page_icon="📋", layout="centered")

# ✅ FIXED CSS (titles visible)
st.markdown("""
<style>

/* GLOBAL */
body {
    background-color: #0e1117;
    color: white;
}

/* CONTAINER */
.block-container {
    max-width: 700px;
}

/* TITLE */
h1 {
    text-align: center;
    color: white;
}

/* DESCRIPTION */
.desc {
    text-align: center;
    color: #c9d1d9;
    margin-bottom: 30px;
}

/* CARD */
.card {
    background-color: #161b22;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 20px;
    border: 1px solid #30363d;
}

/* ✅ IMPORTANT FIX: show question titles */
label, .stMarkdown, p {
    color: #ffffff !important;
    font-size: 16px !important;
}

/* RADIO */
.stRadio > div {
    background-color: #0e1117;
    padding: 10px;
    border-radius: 10px;
}

/* INPUTS */
input, textarea {
    background-color: #0e1117 !important;
    color: white !important;
}

/* BUTTON */
.stButton>button {
    width: 100%;
    background: linear-gradient(135deg, #4CAF50, #2ecc71);
    color: white;
    font-size: 18px;
    border-radius: 12px;
    padding: 12px;
    border: none;
}

</style>
""", unsafe_allow_html=True)

# HEADER
st.markdown("<h1>📋 Enquête sur la qualité du service administratif (TGR)</h1>", unsafe_allow_html=True)

st.markdown("""
<div class="desc">
Ce questionnaire s’inscrit dans le cadre d’un PFE visant à évaluer le rôle du système d’information 
dans l’amélioration de la qualité du service administratif.<br><br>
Les réponses resteront strictement confidentielles.
</div>
""", unsafe_allow_html=True)

# FORM
with st.form("formulaire"):

    st.markdown('<div class="card">', unsafe_allow_html=True)
    poste = st.text_input("1. Poste au sein de l’agence *")
    anciennete = st.radio("2. Ancienneté *", ["Moins d’1 an", "1 à 3 ans", "Plus de 3 ans"])
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    utilisation = st.radio("3. Utilisez-vous le système d’information ? *", ["Oui", "Non"])
    frequence = st.radio("4. Fréquence d’utilisation *", ["Rarement", "Parfois", "Souvent", "Toujours"])
    facilite = st.radio("5. Le système est-il facile à utiliser ? *", ["Très difficile", "Difficile", "Facile", "Très facile"])
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    rapidite = st.radio("6. Amélioration de la rapidité *", ["Faible", "Moyenne", "Élevée"])
    qualite = st.radio("7. Amélioration de la qualité *", ["Faible", "Moyenne", "Élevée"])
    erreurs = st.radio("8. Réduction des erreurs *", ["Faible", "Moyenne", "Élevée"])
    suivi = st.radio("9. Suivi des dossiers *", ["Faible", "Moyenne", "Élevée"])
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    fiabilite = st.radio("10. Fiabilité des informations *", ["Oui", "Non", "Partiellement"])
    securite = st.radio("11. Sécurité du système *", ["Oui", "Non", "Moyennement"])
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    difficulte = st.radio("12. Rencontrez-vous des difficultés ? *", ["Oui", "Non"])
    type_diff = st.multiselect("13. Type de difficultés", ["Techniques", "Organisationnelles", "Humaines"])
    formation = st.radio("14. Formation suffisante ? *", ["Oui", "Non"])
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    evaluation = st.radio("15. Efficacité globale *", ["Très efficace", "Efficace", "Peu efficace", "Pas efficace"])
    suggestions = st.text_area("16. Suggestions")
    st.markdown('</div>', unsafe_allow_html=True)

    submit = st.form_submit_button("🚀 Envoyer ma réponse")

# SAVE
if submit:
    if poste.strip() == "":
        st.error("Veuillez remplir votre poste.")
    else:
        data = {
            "Poste": poste,
            "Ancienneté": anciennete,
            "Utilisation": utilisation,
            "Fréquence": frequence,
            "Facilité": facilite,
            "Rapidité": rapidite,
            "Qualité": qualite,
            "Erreurs": erreurs,
            "Suivi": suivi,
            "Fiabilité": fiabilite,
            "Sécurité": securite,
            "Difficulté": difficulte,
            "Type difficultés": ", ".join(type_diff),
            "Formation": formation,
            "Évaluation": evaluation,
            "Suggestions": suggestions
        }

        file_exists = os.path.isfile("reponses.csv")
        pd.DataFrame([data]).to_csv("reponses.csv", mode="a", header=not file_exists, index=False)

        st.success("✅ Merci ! Votre réponse a été enregistrée.")
