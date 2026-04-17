import streamlit as st
import requests

st.set_page_config(page_title="Questionnaire TGR", page_icon="📋", layout="centered")

# STYLE
st.markdown("""
<style>
hr {
    border: 1px solid #ddd;
}
@media (prefers-color-scheme: dark) {
    hr {
        border: 1px solid #333;
    }
}
</style>
""", unsafe_allow_html=True)

# HEADER
st.title("📋 Enquête sur la qualité du service administratif (TGR)")

st.markdown("""
Ce questionnaire s’inscrit dans le cadre d’un PFE visant à évaluer le rôle du système d’information  
dans l’amélioration de la qualité du service administratif.  

Les réponses resteront strictement confidentielles.
""")

# PROGRESS TRACKER
progress = 0

# FORM
with st.form("formulaire"):

    poste = st.text_input("1. Poste au sein de l’agence")
    anciennete = st.radio("2. Ancienneté", ["Moins d’1 an", "1 à 3 ans", "Plus de 3 ans"])

    st.markdown("---")

    utilisation = st.radio("3. Utilisez-vous le système d’information ?", ["Oui", "Non"])
    frequence = st.radio("4. Fréquence d’utilisation", ["Rarement", "Parfois", "Souvent", "Toujours"])
    facilite = st.radio("5. Le système est-il facile à utiliser ?", ["Très difficile", "Difficile", "Facile", "Très facile"])

    st.markdown("---")

    rapidite = st.radio("6. Dans quelle mesure le système d’information améliore-t-il la rapidité de traitement des dossiers ?",
                        ["Faible", "Moyenne", "Élevée"])
    qualite = st.radio("7. Dans quelle mesure le système d’information améliore-t-il la qualité du service administratif ?",
                       ["Faible", "Moyenne", "Élevée"])
    erreurs = st.radio("8. Dans quelle mesure le système d’information contribue-t-il à la réduction des erreurs ?",
                       ["Faible", "Moyenne", "Élevée"])
    suivi = st.radio("9. Dans quelle mesure le système d’information facilite-t-il le suivi et la traçabilité des dossiers ?",
                     ["Faible", "Moyenne", "Élevée"])

    st.markdown("---")

    fiabilite = st.radio("10. Le système garantit-il la fiabilité des informations ?", ["Oui", "Non", "Partiellement"])
    securite = st.radio("11. Le système est-il sécurisé ?", ["Oui", "Non", "Moyennement"])

    st.markdown("---")

    difficulte = st.radio("12. Rencontrez-vous des difficultés ?", ["Oui", "Non"])

    if difficulte == "Oui":
        type_diff = st.multiselect("13. Type de difficultés", ["Techniques", "Organisationnelles", "Humaines"])
    else:
        type_diff = []

    formation = st.radio("14. La formation reçue est-elle suffisante ?", ["Oui", "Non"])

    st.markdown("---")

    evaluation = st.radio("15. Comment évaluez-vous l’efficacité globale du système ?",
                          ["Très efficace", "Efficace", "Peu efficace", "Pas efficace"])
    suggestions = st.text_area("16. Quelles améliorations proposez-vous ?")

    submit = st.form_submit_button("🚀 Envoyer ma réponse")

# PROGRESS CALCULATION
answered = sum([
    poste != "",
    anciennete != "",
    utilisation != "",
    frequence != "",
    facilite != "",
    rapidite != "",
    qualite != "",
    erreurs != "",
    suivi != "",
    fiabilite != "",
    securite != "",
    difficulte != "",
    formation != "",
    evaluation != ""
])

progress = answered / 14

st.progress(progress)

# SAVE
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
