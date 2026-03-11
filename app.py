
import streamlit as st

# Ta base de données des 12 incontournables
produits_carnes = [
# Voici la liste des burgers de Mcdonald's
    
    {"nom": "Big Mac", "enseigne": "McDonald's", "prix": 6.53, "proteines": 27, "type": "Burger"},
    {"nom": "Double Cheese", "enseigne": "McDonald's", "prix": 5.70, "proteines": 27, "type": "Burger"},
    {"nom": "Royal Cheese", "enseigne": "McDonald's", "prix": 7.30, "proteines": 31, "type": "Burger"},
    {"nom": "Royal Bacon", "enseigne": "McDonald's", "prix": 7.23, "proteines": 30, "type": "Burger"},
    {"nom": "McChicken", "enseigne": "McDonald's", "prix": 5.70, "proteines": 19, "type": "Burger"},
    {"nom": "Filet-O-Fish", "enseigne": "McDonald's", "prix": 5.70, "proteines": 15, "type": "Burger"},
    {"nom": "280 Original", "enseigne": "McDonald's", "prix": 8.30, "proteines": 44, "type": "Burger"},
    {"nom": "9 McNuggets", "enseigne": "McDonald's", "prix": 7.50, "proteines": 23, "type": "Nuggets"},
    
# Voici la liste des burgers de Burger King
    
    {"nom": "Whopper", "enseigne": "Burger King", "prix": 6.65, "proteines": 28, "type": "Burger"},
    {"nom": "Double Whoppe Cheese", "enseigne": "Burger King", "prix": 9.06, "proteines": 52, "type": "Burger"},
    {"nom": "Steakhouse", "enseigne": "Burger King", "prix": 7.26, "proteines": 37, "type": "Burger"},
    {"nom": "Big King", "enseigne": "Burger King", "prix": 5.76, "proteines": 27, "type": "Burger"},
    {"nom": "Double Cheese Bacon XXL", "enseigne": "Burger King", "prix": 9.40, "proteines": 60, "type": "Burger"},
    {"nom": "Chicken Louisiane Steakhouse", "enseigne": "Burger King", "prix": 7.55, "proteines": 38, "type": "Burger"},
    {"nom": "Crispy Chicken Cheese", "enseigne": "Burger King", "prix": 5.71, "proteines": 19, "type": "Burger"},
    {"nom": "10 King Nuggets", "enseigne": "Burger King", "prix": 6.46, "proteines": 24, "type": "Nuggets"},

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
    {"nom": "Veggie Nuggets (x9)", "enseigne": "McDonald's", "prix": 7.50, "proteines": 23, "type": "Nuggets"},
    {"nom": "McVeggie", "enseigne": "McDonald's", "prix": 5.70, "proteines": 17, "type": "Burger"},
    
    {"nom": "Veggie Whopper", "enseigne": "Burger King", "prix": 6.65, "proteines": 27, "type": "Burger"},
    {"nom": "Veggie Steakhouse", "enseigne": "Burger King", "prix": 7.36, "proteines": 33, "type": "Burger"},
    {"nom": "Veggie Chicken Louisiane", "enseigne": "Burger King", "prix": 7.55, "proteines": 24, "type": "Burger"},
    
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


# --- SECTION VALIDATION MVP (PAGE PRINCIPALE) ---
st.write("---") 
st.header("🧪 Mode Expert : Ne sacrifiez plus votre santé")
st.write("Vous vous sentez fatigué(e) ? On développe l'outil qui calcule vos apports en **Fer**, **B12** et **Oméga-3** pour chaque burger.")

# Le bouton change de promesse : on devient acteur du projet
st.link_button("🚀 Devenir Bêta-Testeur (Accès Privé)", 
               "https://docs.google.com/forms/d/e/1FAIpQLSdfcfRgc_N1lthe5yvm91dDLScVvAk1WFX0vHRvCwiQkCvljw/viewform?usp=sf_link", 
               use_container_width=True)

# La promo devient une récompense pour l'aide apportée
st.info("🎁 **Récompense :** Les bêta-testeurs bénéficient de -50% à vie sur la version finale.")
st.caption("Rejoignez les 50+ passionnés qui nous aident à optimiser la nutrition végétale. 🌿")


