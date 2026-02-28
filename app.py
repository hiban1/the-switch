
import streamlit as st

# Ta base de données des 12 incontournables
produits_carnes = [
# Voici la liste des burgers de Mcdonald's
    
    {"nom": "Big Mac", "enseigne": "McDonald's", "prix": 6.53, "proteines": 26, "type": "Burger"},
    {"nom": "Double Cheese", "enseigne": "McDonald's", "prix": 5.70, "proteines": 24, "type": "Burger"},
    {"nom": "Royal Cheese", "enseigne": "McDonald's", "prix": 7.30, "proteines": 25, "type": "Burger"},
    {"nom": "Royal Bacon", "enseigne": "McDonald's", "prix": 7.23, "proteines": 26, "type": "Burger"},
    {"nom": "McChicken", "enseigne": "McDonald's", "prix": 5.70, "proteines": 20, "type": "Burger"},
    {"nom": "Filet-O-Fish", "enseigne": "McDonald's", "prix": 5.70, "proteines": 15, "type": "Burger"},
    {"nom": "280 Original", "enseigne": "McDonald's", "prix": 8.30, "proteines": 34, "type": "Burger"},
    {"nom": "9 McNuggets", "enseigne": "McDonald's", "prix": 7.50, "proteines": 24, "type": "Nuggets"},
    
# Voici la liste des burgers de Burger King
    
    {"nom": "Whopper", "enseigne": "Burger King", "prix": 6.65, "proteines": 27, "type": "Burger"},
    {"nom": "Double Whoppe Cheese", "enseigne": "Burger King", "prix": 9.06, "proteines": 44, "type": "Burger"},
    {"nom": "Steakhouse", "enseigne": "Burger King", "prix": 7.26, "proteines": 31, "type": "Burger"},
    {"nom": "Big King", "enseigne": "Burger King", "prix": 5.76, "proteines": 19, "type": "Burger"},
    {"nom": "Double Cheese Bacon XXL", "enseigne": "Burger King", "prix": 9.40, "proteines": 45, "type": "Burger"},
    {"nom": "Chicken Louisiane Steakhouse", "enseigne": "Burger King", "prix": 7.55, "proteines": 23, "type": "Burger"},
    {"nom": "Crispy Chicken Cheese", "enseigne": "Burger King", "prix": 5.71, "proteines": 16, "type": "Burger"},
    {"nom": "10 King Nuggets", "enseigne": "Burger King", "prix": 6.46, "proteines": 21, "type": "Nuggets"},

# Voici la liste des burgers de KFC

    {"nom": "Tower cheese and bacon", "enseigne": "KFC", "prix": 8.85, "proteines": 31, "type": "Burger"},
    {"nom": "Colonel Original Fish", "enseigne": "KFC", "prix": 7.15, "proteines": 26, "type": "Burger"},
    {"nom": "Colonel Original", "enseigne": "KFC", "prix": 7.15, "proteines": 24, "type": "Burger"},
    {"nom": "Boxmaster Original", "enseigne": "KFC", "prix": 7.90, "proteines": 33, "type": "Burger"},
    {"nom": "Bucket Tenders (x10)", "enseigne": "KFC", "prix": 17.45, "proteines": 48, "type": "Nuggets"},
    {"nom": "Hot Wings (x8)", "enseigne": "KFC", "prix": 8.76, "proteines": 42, "type": "Nuggets"},
    {"nom": "Colonel Original Bacon", "enseigne": "KFC", "prix": 7.66, "proteines": 40, "type": "Burger"},
    {"nom": "Kentucky BBQ Burger", "enseigne": "KFC", "prix": 9.95, "proteines": 28, "type": "Burger"}

    
]



# On ajoute quelques alternatives pour le test
alternatives_vegans = [
    {"nom": "Veggie Nuggets (x9)", "enseigne": "McDonald's", "prix": 7,50, "proteines": 15, "type": "Nuggets"},
    {"nom": "McVeggie", "enseigne": "McDonald's", "prix": 5.70, "proteines": 14, "type": "Burger"},
    
    {"nom": "Veggie Whopper", "enseigne": "Burger King", "prix": 6.65, "proteines": 22, "type": "Burger"},
    {"nom": "Veggie Steakhouse", "enseigne": "Burger King", "prix": 7.36, "proteines": 25, "type": "Burger"},
    {"nom": "Veggie Chicken Louisiane", "enseigne": "Burger King", "prix": 7.55, "proteines": 21, "type": "Burger"},
    
    {"nom": "Colonel Original Veggie", "enseigne": "KFC", "prix": 7.23, "proteines": 18, "type": "Burger"},
    {"nom": "Boxmaster Veggie", "enseigne": "KFC", "prix": 8.23, "proteines": 22, "type": "Burger"},
    {"nom": "Tower Cheese and Bacon Veggie", "enseigne": "KFC", "prix": 8.85, "proteines": 20, "type": "Burger"},
    {"nom": "Colonel Original Bacon Veggie", "enseigne": "KFC", "prix": 7.66, "proteines": 21, "type": "Burger"}


    
]

st.set_page_config(page_title="The Switch", page_icon="🌱")


# --- 2. L'INTERFACE ---

st.title("🌱 The Switch")
st.write("Trouvez l'alternative vegan la plus adaptée à vos besoins.")

options_noms = [p['nom'] for p in produits_carnes]
choix = st.selectbox(
    "Quel produit manges-tu d'habitude ?",
    options=options_noms,
    index=None,
    placeholder="Tapez le nom (ex: Big Mac...)",
)

if choix:
    # On identifie ce que l'utilisateur a choisi
    cible = next(p for p in produits_carnes if p['nom'] == choix)
    
    # ON PLACE LES BOUTONS ICI
    priorite = st.radio(
        "Ta priorité aujourd'hui :",
        ["💪 Protéines", "💰 Prix", "🏢 Même Enseigne"],
        horizontal=True
    )
    
    # On cherche les alternatives du même type (Burger ou Nuggets)
    alts = [p for p in alternatives_vegans if p['type'] == cible['type']]
    
    if alts:
        # LOGIQUE DE TRI
        if priorite == "💪 Protéines":
            alts.sort(key=lambda x: x['proteines'], reverse=True)
        elif priorite == "💰 Prix":
            alts.sort(key=lambda x: x['prix'])
        elif priorite == "🏢 Même Enseigne":
            alts.sort(key=lambda x: x['enseigne'] != cible['enseigne'])

        # On prend le premier résultat après le tri
        gagnant = alts[0]
        
        st.divider()
        st.subheader(f"✅ Ton Switch : {gagnant['nom']} ({gagnant['enseigne']})")
        
        col1, col2 = st.columns(2)
        with col1:
            diff_prix = round(gagnant['prix'] - cible['prix'], 2)
            st.metric("Prix", f"{gagnant['prix']}€", f"{diff_prix}€", delta_color="inverse")
        with col2:
            diff_prot = gagnant['proteines'] - cible['proteines']
            st.metric("Protéines", f"{gagnant['proteines']}g", f"{diff_prot}g")
            
        if diff_prot < 0:
            st.info(f"💡 Note : Tu perds {abs(diff_prot)}g de protéines, mais c'est mieux pour la planète !")
    else:
        st.warning("Aucune alternative trouvée pour ce type de produit.")

