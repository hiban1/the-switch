
import streamlit as st

# Ta base de données des 12 incontournables
produits_carnes = [
    {"nom": "Big Mac", "enseigne": "McDonald's", "prix": 5.70, "proteines": 26, "type": "Burger"},
    {"nom": "Double Cheese", "enseigne": "McDonald's", "prix": 4.10, "proteines": 24, "type": "Burger"},
    {"nom": "McChicken", "enseigne": "McDonald's", "prix": 5.40, "proteines": 20, "type": "Burger"},
    {"nom": "Triple Cheese", "enseigne": "McDonald's", "prix": 6.20, "proteines": 31, "type": "Burger"},
    {"nom": "280 Original", "enseigne": "McDonald's", "prix": 7.40, "proteines": 34, "type": "Burger"},
    {"nom": "9 McNuggets", "enseigne": "McDonald's", "prix": 6.90, "proteines": 24, "type": "Nuggets"}
]

# On ajoute quelques alternatives pour le test
alternatives_vegans = [
    {"nom": "Veggie McPlant", "enseigne": "McDonald's", "prix": 5.70, "proteines": 19, "type": "Burger"},
    {"nom": "Veggie Whopper", "enseigne": "Burger King", "prix": 6.10, "proteines": 22, "type": "Burger"},
    {"nom": "Veggie Nuggets (x9)", "enseigne": "McDonald's", "prix": 6.90, "proteines": 15, "type": "Nuggets"}
]

st.set_page_config(page_title="The Switch", page_icon="🌱")

st.title("🌱 The Switch")
st.write("Trouvez l'alternative vegan la plus rentable.")

# --- LA MAGIE EST ICI : LE MENU DÉROULANT AVEC RECHERCHE ---
options_noms = [p['nom'] for p in produits_carnes]
choix = st.selectbox(
    "Quel produit manges-tu d'habitude ?",
    options=options_noms,
    index=None,
    placeholder="Tapez le nom (ex: Big Mac...)",
)

if choix:
    # 1. Trouver le produit carné choisi
    cible = next(p for p in produits_carnes if p['nom'] == choix)
    
    # 2. Trouver la meilleure alternative (même type)
    alts = [p for p in alternatives_vegans if p['type'] == cible['type']]
    
    if alts:
        # Trier par protéines/prix
        alts.sort(key=lambda x: x['proteines'] / x['prix'], reverse=True)
        gagnant = alts[0]
        
        st.divider()
        st.subheader(f"✅ Ton Switch : {gagnant['nom']}")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Prix", f"{gagnant['prix']}€", f"{round(gagnant['prix'] - cible['prix'], 2)}€")
        with col2:
            diff_prot = gagnant['proteines'] - cible['proteines']
            st.metric("Protéines", f"{gagnant['proteines']}g", f"{diff_prot}g")
            
        if diff_prot < 0:
            st.info(f"💡 Note : Tu perds {abs(diff_prot)}g de protéines, mais tu sauves la planète !")
    else:
        st.warning("Aucune alternative trouvée pour ce type de produit.")

