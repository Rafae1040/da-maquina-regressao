from sklearn.model_selection import train_test_split

#Separando a base de dados em treino e teste utilizando uma proporção de 2/3 para treino e 1/3 para testes.


predictors_train, predictors_test, target_train, target_test = train_test_split(
    penguim.drop(['body_mass_g'], axis=1), 
    penguim['body_mass_g'], 
    test_size=1/3, 
    random_state=123
)

predictors_train.head()

predictors_train.shape

predictors_test.head()

predictors_test.shape

target_train.head()

target_train.shape

target_test.head()

target_test.shape