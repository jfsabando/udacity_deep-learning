# TODO: Add import statements
import pandas as pd
from sklearn.linear_model import LinearRegression
# import matplotlib.pyplot as plt

# Assign the dataframe to this variable.
# TODO: Load the data
bmi_life_data = pd.read_csv('bmi_and_life_expectancy.csv', header = 0)

# Make and fit the linear regression model
#TODO: Fit the model and Assign it to bmi_life_model
bmi_life_model = LinearRegression()
bmi_life_model.fit(bmi_life_data[['BMI']], bmi_life_data[['Life expectancy']]) #fit(x, y)

# Mak a prediction using the model
# TODO: Predict life expectancy for a BMI value of 21.07931
# plt.scatter(x_values, y_values)
# plt.plot(x_values, bmi_life_model.predict(x_values))
# plt.show()
laos_life_exp = bmi_life_model.predict(21.07931)
