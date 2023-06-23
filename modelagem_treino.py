from sklearn.linear_model import LinearRegression

model = LinearRegression()

model = model.fit(predictors_train, target_train)

model.__dict__

a = model.coef_
print(a)

b = model.intercept_
print(b)

# Avaliação:

from sklearn.metrics import mean_squared_error

target_predicted = model.predict(predictors_test)

rmse = np.sqrt(mean_squared_error(target_test, target_predicted))
print(rmse)
