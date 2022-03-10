# Step 1: Import and read csv file
import pickle
import pandas as pd
dataset = pd.read_csv("weight_height_data.csv")
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Step 2: Check for missing values
dataset.isnull().sum()

# Step 3: Split dataset into train and test
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Step 4: Fit Linear Regression Model
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)

# Step 5: Predict values for test data
lin_pred = lin_reg.predict(X_test)

# Step 6: Compare predictions with real results
from sklearn import metrics
print('R square = ', metrics.r2_score(y_test, lin_pred))
print('Mean squared Error = ', metrics.mean_squared_error(y_test, lin_pred))

with open('height_model_pickle', 'wb') as files:
    pickle.dump(lin_reg, files)
    files.close()
