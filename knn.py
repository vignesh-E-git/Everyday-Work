# 1. importing dataset from sklearn

import pandas as pd
from sklearn.datasets import fetch_california_housing
dataset = fetch_california_housing()
print(dataset)


# 2. download the dataset locally
# numpy array -> structured dataset -> pandas dataframe -> to_csv -> download

df = pd.DataFrame(dataset.data,columns=dataset.feature_names)
df["target"] = dataset.target
print(df)
df.to_csv("california_housing.csv")


# 3.spliting and shrinking the dataset

import pandas as pd
from sklearn.model_selection import train_test_split as splitter

df = pd.read_csv("california_housing.csv")
#print(df) # 20640 x 10 size

df = df.head(500)
print(df.head(0)) # heading column

X = df.drop(columns=["target"])
Y = df["target"]

X_train,X_test,Y_train,Y_test = splitter(X,Y,test_size=0.2) # 400 for training and 100 for testing
#print(Y_test)

# 4. select->fit->predict model

from sklearn.neighbors import KNeighborsRegressor as knn
model = knn()
model.fit(X_train,Y_train)
# predictions = model.predict(X_test) #predict all
predictions = model.predict(X_test[0:5])
print(predictions)