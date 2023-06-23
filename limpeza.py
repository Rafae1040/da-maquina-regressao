# Descartando as colunas originais e mantendo apenas a variável resposta e as variáveis preditivas com o sufixo _std", _nom" e "_ord".

penguim = penguim.drop(columns=["species","island", "bill_length_mm", "bill_depth_mm", "flipper_length_mm", "sex"], axis=1)

penguim.head()
