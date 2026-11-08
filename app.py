import google.generativeai as genai
import streamlit as st

# Configuration de la page Streamlit
st.set_page_config(
    page_title="Meta-Orchestrateur | Nexus mondial de l'IA", layout="centered"
)

st.title("👑 Meta-Orchestrateur - Nexus")
st.write("La Matrice Centrale de Commande pour le réseau d'IA")

# Récupération de la clé API depuis les secrets Streamlit
try:
  api_key = st.secrets["GEMINI_API_KEY"]
  genai.configure(api_key=api_key)
  cle_configuree = True
except Exception as e:
  cle_configuree = False
  st.error(
      "Erreur : La clé API 'GEMINI_API_KEY' n'est pas configurée dans les Secrets"
      " de Streamlit."
  )

# Champ de saisie pour la directive
directive = st.text_area(
    "Entrez la directive suprême pour le réseau d'IA :",
    placeholder=(
        "Ex: Structurer une offre commerciale complète pour lancer une"
        " activité..."
    ),
)

if st.button("🚀 Exécuter le Nexus") and cle_configuree:
  if directive.strip():
    try:
      with st.spinner("Le Nexus traite votre directive..."):
        # Utilisation d'un modèle récent et valide (gemini-1.5-flash)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(directive)

        st.subheader("Résultat du Nexus :")
        st.write(response.text)
    except Exception as err:
      st.error(f"Une erreur est survenue lors de l'appel à l'IA : {err}")
  else:
    st.warning("Veuillez entrer une directive valide.")
