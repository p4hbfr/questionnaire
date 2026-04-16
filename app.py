import streamlit as st
import requests

st.set_page_config(page_title="Questionnaire TGR", page_icon="📋", layout="centered")

# ✅ MODERN STYLE (works in dark & light)
st.markdown("""
<style>

/* Cards */
.card {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 20px;
    border: 1px solid #ddd;
}

/* Dark mode auto */
@media (prefers-color-scheme: dark) {
    .card {
        background-color: #161b22;
        border: 1px solid #30363d;
    }
}

/* Titles */
h1 {
    text-align: center;
}

/* Description */
.desc {
    text-align: center;
    margin-bottom: 30px;
}

/* Button */
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
    rapidite = st.radio("6. Dans quelle mesure le système d’information améliore-t-il la rapidité de traitement des dossiers ? *",
                        ["Faible", "Moyenne", "Élevée"])
    qualite = st.radio("7. Dans quelle mesure le système d’information améliore-t-il la qualité du service administratif ? *",
                       ["Faible", "Moyenne", "Élevée"])
    erreurs = st.radio("8. Dans quelle mesure le système d’information contribue-t-il à la réduction des erreurs ? *",
                       ["Faible", "Moyenne", "Élevée"])
    suivi = st.radio("9. Dans quelle mesure le système d’information facilite-t-il le suivi et la traçabilité des dossiers ? *",
                     ["Faible", "Moyenne", "Élevée"])
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    fiabilite = st.radio("10. Le système garantit-il la fiabilité des informations ? *", ["Oui", "Non", "Partiellement"])
    securite = st.radio("11. Le système est-il sécurisé ? *", ["Oui", "Non", "Moyennement"])
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    difficulte = st.radio("12. Rencontrez-vous des difficultés ? *", ["Oui", "Non"])

    # ✅ CONDITION (IMPORTANT)
    if difficulte == "Oui":
        type_diff = st.multiselect("13. Type de difficultés", ["Techniques", "Organisationnelles", "Humaines"])
    else:
        type_diff = []

    formation = st.radio("14. La formation reçue est-elle suffisante ? *", ["Oui", "Non"])
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    evaluation = st.radio("15. Comment évaluez-vous l’efficacité globale du système ? *",
                          ["Très efficace", "Efficace", "Peu efficace", "Pas efficace"])
    suggestions = st.text_area("16. Quelles améliorations proposez-vous ?")
    st.markdown('</div>', unsafe_allow_html=True)

    submit = st.form_submit_button("🚀 Envoyer ma réponse")

# SAVE TO GOOGLE SHEETS
if submit:
    if poste.strip() == "":
        st.error("Veuillez remplir votre poste.")
    else:
        url = "https://sheetdb.io/api/v1/hi0twxy26y2da"

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

        response = requests.post(url, json=data)

        if response.status_code == 201:
            st.success("✅ Merci ! Votre réponse a été enregistrée avec succès.")
        else:
            st.error("❌ Erreur lors de l’envoi.")
