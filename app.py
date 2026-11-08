import os
import streamlit as st
from google import genai

# Configuration de la page Streamlit
st.set_page_config(
    page_title="Méta-Orchestrateur | Nexus mondial de l'IA",
    page_icon="👑",
    layout="wide"
)

st.markdown("""
# 👑 Meta-Orchestrator | Global AI Nexus
### *La Matrice Centrale de Commande Multi-IA*
""")

# Configuration de la clé API (via les secrets Streamlit ou une saisie utilisateur si besoin)
api_key = os.getenv("GEMINI_API_KEY")
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]

st.write("Entrez la directive suprême pour le réseau d'IA :")

directive = st.text_area(
    "Directive :",
    value="Élaborer un plan d'action immédiat pour vendre des services de création de sites web vitrines aux entreprises locales. Générer la structure HTML/Tailwind CSS d'une page de vente percutante, rédiger une séquence de 3 messages d'approche WhatsApp pour prospecter des clients, et fixer une grille tarifaire compétitive adaptée au marché."
)

if st.button("👑 Exécuter le Nexus"):
    if not api_key:
        st.error("Erreur : Aucune clé API Gemini n'a été détectée. Veuillez configurer votre clé dans les secrets Streamlit.")
    else:
        with st.spinner("👑 Le Nexus déploie sa puissance sur le réseau mondial d'IA..."):
            try:
                # Initialisation du client genai avec la nouvelle bibliothèque officielle
                client = genai.Client(api_key=api_key)
                
                # Appel au modèle Gemini (utilisation de gemini-2.5-flash ou équivalent standard)
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=directive
                )
                
                st.success("Directive exécutée avec succès par le Nexus !")
                st.markdown("### 📊 Rapport d'Exécution du Global Nexus")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"Erreur critique du Nexus : {e}")
