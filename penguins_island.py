with sns.axes_style('whitegrid'):

  grafico = sns.pairplot(data=penguim, hue="island", palette="pastel")
  
  plt.savefig('penguins_island.png')

#A ilha Biscoe é aquela em que os pinguins apresentam a maior massa corporal(body_mass_g) e o maior comprimeto das nadadeiras( flipper_length_mm) essa ilha pode ter uma predominancia de habitar a especie Gentoo. Já a ilha Dream no atributo comprimento do bico(bill_depth_mm) se iguala e predominancia de habitar a especie Adelle. A ilha Torgensen apesar de ter indices a baixo das outras duas ilhas, no atributos podemos afirmar que essa ilha tem uma diversificação de especies por cada atributo.