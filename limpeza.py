penguim = penguim.drop(columns=["species","island", "bill_length_mm", "bill_depth_mm", "flipper_length_mm", "sex"], axis=1)

penguim.head()