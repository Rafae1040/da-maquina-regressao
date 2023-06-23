media = penguim['bill_length_mm'].mean()
print(media)

desvio_padrao = penguim['bill_length_mm'].std()
print(desvio_padrao)

penguim['bill_length_mm_std'] = penguim['bill_length_mm'].apply(lambda bill_length_mm: (bill_length_mm - media) /  desvio_padrao)


media = penguim['bill_depth_mm'].mean()
print(media)

desvio_padrao = penguim['bill_depth_mm'].std()
print(desvio_padrao)

penguim['bill_depth_mm_std'] = penguim['bill_depth_mm'].apply(lambda bill_depth_mm: (bill_depth_mm - media) /  desvio_padrao)


media = penguim['flipper_length_mm'].mean()
print(media)

desvio_padrao = penguim['flipper_length_mm'].std()
print(desvio_padrao)

penguim['flipper_length_mm_std'] = penguim['flipper_length_mm'].apply(lambda flipper_length_mm: (flipper_length_mm - media) /  desvio_padrao)

penguim.head()