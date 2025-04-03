# Titre de l'application
st.title("Analyse ESG de Kering, Schneider Electric et Danone")

# Données fictives pour illustration
data = {
    "Entreprise": ["Kering", "Schneider Electric", "Danone"],
    "Secteur": ["Luxe", "Énergie", "Agroalimentaire"],
    "Score ESG": [85, 90, 88],
    "Performance Financière": [5.4, 6.2, 4.8]
}

df = pd.DataFrame(data)

# Affichage des données
st.write("### Détails des entreprises")
st.dataframe(df)

# Visualisation des scores ESG
st.write("### Répartition des Scores ESG")
fig, ax = plt.subplots()
ax.bar(df["Entreprise"], df["Score ESG"], color=['green', 'blue', 'orange'])
ax.set_ylabel("Score ESG")
st.pyplot(fig)

# Visualisation des performances financières
st.write("### Performances Financières")
fig, ax = plt.subplots()
ax.plot(df["Entreprise"], df["Performance Financière"], marker='o', linestyle='-')
ax.set_ylabel("Performance (%)")
st.pyplot(fig)
