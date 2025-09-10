import pandas as pd
import streamlit as st
import plotly.express as px

# Charger les données
df = pd.read_csv("data/ventes.csv")

st.title("📊 Dashboard des ventes")

# Filtres
regions = st.multiselect("Sélectionnez la/les région(s):", df['région'].unique(), default=df['région'].unique())
produits = st.multiselect("Sélectionnez le/les produit(s):", df['produit'].unique(), default=df['produit'].unique())

filtered_df = df[(df['région'].isin(regions)) & (df['produit'].isin(produits))]

# Chiffre d'affaires par jour
filtered_df['CA'] = filtered_df['quantité'] * filtered_df['prix_unitaire']
daily_sales = filtered_df.groupby('date', as_index=False)['CA'].sum()

fig = px.line(daily_sales, x='date', y='CA', title='Chiffre d’affaires par jour')
st.plotly_chart(fig)

# Top produits
top_products = filtered_df.groupby('produit', as_index=False)['CA'].sum().sort_values('CA', ascending=False)
fig2 = px.bar(top_products, x='produit', y='CA', title='Top Produits')
st.plotly_chart(fig2)

# Tableau brut
st.subheader("Données filtrées")
st.dataframe(filtered_df)
