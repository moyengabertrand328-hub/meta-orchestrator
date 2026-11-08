import streamlit as st
from google import genai

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(
    page_title="Meta-Orchestrator | Global Nexus",
    page_icon="👑",
    layout="wide"
)

# --- CONFIGURATION DES CLÉS (CENTRE DE COMMANDEMENT GLOBAL) ---
API_KEY_GOOGLE = "AQ.Ab8RN6JwyqYKu9o8syr8hZsktUITDkKACbHQZmkuSF3mdfxIhA"
client_google = genai.Client(api_key=API_KEY_GOOGLE)

# --- INTERFACE UTILISATEUR : LE TRÔNE DU MÉTA-ORCHESTRATEUR ---
st.title("👑 Meta-Orchestrator | Global AI Nexus")
st.markdown("### *La Matrice Centrale de Commandement Multi-IA*")
st.markdown("---")

# Panneau de contrôle global dans la barre latérale
st.sidebar.header("🌐 Paramètres du Nexus")
moteur_principal = st.sidebar.selectbox(
    "Moteur IA Principal",
    [
        "Google Gemini 3.8 Flash (Vitesse Maximale)",
        "Mode Hybride Global (Multi-Analyses)",
        "Simulateur de Réseau Neuronal Distribué"
    ]
)
niveau_autonomie = st.sidebar.slider("Niveau d'Autonomie des Agents", 1, 10, 10)
st.sidebar.success("⚡ Nexus actif : Connexion globale établie.")

# Zone de mission suprême
mission = st.text_area(
    "Entrez la directive suprême pour le réseau d'IA :",
    placeholder="Ex: Concevoir un empire digital autonome complet : stratégie, code source, et architecture de déploiement..."
)

col1, col2 = st.columns([1, 4])
with col1:
    lancer = st.button("👑 Exécuter le Nexus", type="primary")

if lancer:
    if not mission.strip():
        st.warning("Veuillez entrer une directive valide.")
    else:
        with st.spinner("👑 Le Nexus déploie sa puissance sur le réseau mondial d'IA..."):
            prompt_nexus = (
                "Tu es le Meta-Orchestrator suprême, le noyau central qui orchestre toutes les intelligences. "
                "Traite cette directive avec une précision absolue et une autorité absolue en générant 4 blocs maîtres en Markdown :\n"
                "1. **STRATÉGIE DE DOMINATION & ANALYSE**\n"
                "2. **EXÉCUTION TECHNIQUE & CODE SOURCE**\n"
                "3. **PLANS D'AUTOMATISATION & MONÉTISATION**\n"
                "4. **PROTOCOLES DE DÉPLOIEMENT GLOBAL**\n\n"
                f"Directive Suprême : {mission}"
            )
            
            try:
                # Appel direct ultra-rapide au noyau Gemini
                response = client_google.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=prompt_nexus
                )
                resultat_nexus = response.text
                st.success("✨ Directive exécutée avec succès par le Nexus !")
            except Exception as e:
                st.error(f"Erreur critique du Nexus : {e}")
                st.stop()

        # Affichage des résultats du Nexus
        st.markdown("---")
        st.subheader("📊 Rapport d'Exécution du Global Nexus")
        st.markdown(resultat_nexus)

        # Téléchargement du manifeste mondial
        st.download_button(
            label="📥 Télécharger le Manifeste du Nexus (.md)",
            data=resultat_nexus,
            file_name="manifeste_global_nexus.md",
            mime="text/markdown"
        )