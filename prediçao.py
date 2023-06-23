new_bill_length_mm = 38.2
new_bill_depth_mm = 18.1
new_flipper_length_mm = 185.0
bill_length_mm_mean = 43.92
bill_length_mm_std = 5.46
bill_depth_mm_mean = 17.15
bill_depth_mm_std = 1.97
flipper_length_mm_mean = 200.92
flipper_length_mm_std = 14.06


new_bill_length_mm_std = (new_bill_length_mm - bill_length_mm_mean) / bill_length_mm_std
print(new_bill_length_mm_std)
new_bill_depth_mm_std = (new_bill_depth_mm - bill_depth_mm_mean) / bill_depth_mm_std
print(new_bill_depth_mm_std)
new_flipper_length_mm_std = (new_flipper_length_mm - flipper_length_mm_mean) / flipper_length_mm_std
print(new_flipper_length_mm_std)


peso_encontrado = np.array([38.2, 18.1, 185.0, 0, 1, 0, 0, 0, 1, 1, 0])
print(peso_encontrado)

peso = model.predict(peso_encontrado.reshape(1, -1))
print(peso)