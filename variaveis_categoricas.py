penguim[['species', 'island', 'sex']].head()

penguim['species_Adelie_nom'] = penguim['species'].apply(lambda species: 1 if species == 'Adelie' else 0)
penguim['species_Gentoo_nom'] = penguim['species'].apply(lambda species: 1 if species == 'Gentoo' else 0)
penguim['species_Chinstrap_nom'] = penguim['species'].apply(lambda species: 1 if species == 'Chinstrap' else 0)

penguim['island_Dream_nom'] = penguim['island'].apply(lambda island: 1 if island == 'Dream' else 0)
penguim['island_Torgersen_nom'] = penguim['island'].apply(lambda island: 1 if island == 'Torgersen' else 0)
penguim['island_Biscoe_nom'] = penguim['island'].apply(lambda island: 1 if island == 'Biscoe' else 0)

penguim['sex_m_nom'] = penguim['sex'].apply(lambda sex: 1 if sex == 'Male' else 0)
penguim['sex_f_nom'] = penguim['sex'].apply(lambda sex: 1 if sex == 'Female' else 0)


penguim.head()