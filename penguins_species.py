with sns.axes_style('whitegrid'):

  grafico = sns.pairplot(data=penguim, hue="species", palette="pastel")
  
  plt.savefig('penguins_species.png')

# A especie Adelle apresenta ser a mais numerosa e entre as especies ser a maior no atribuito profundidade do bico(bill_depth_mm). 
# A especie Chinstrap se aproxima no atributo comprimento do bico( bill_length_mm), com a especie Gentoo. 
# Ja a especie Gentoo em dois atributos tem uma consistencia maior entre as especies os atributos seria o comprimeto das nadadeiras(flipper_length_mm) e massa corporal(body_mass_g).
