with sns.axes_style('whitegrid'):

  grafico = sns.pairplot(data=penguim, hue="sex", palette="pastel")
  
  plt.savefig('penguins_sexo.png')


# Os machos tendem a ser maiores e mais pesados do que as fêmeas. 
# Isso significa que os machos geralmente têm medidas corporais maiores do que as fêmeas. 
# Como o comprimento do bico (bill_length_mm) ou o comprimento das nadadeiras (flipper_length_mm). 
# No entanto, também é comum que haja uma variação natural nessas medidas entre os pinguins.
