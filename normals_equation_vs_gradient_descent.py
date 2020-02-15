# -*- coding: utf-8 -*-
"""Normals Equation vs Gradient Descent.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1buHN-fOZ6axMl42si4ucdO6bja-OLsp4
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

data = pd.read_excel("LR_ML.xlsx",sheet_name=0)
#. read the first column
X = data.iloc[:, 0].values
#. read the second column
Y = data.iloc[:, 1].values

#. look at the shapes
Y.shape

X.shape

"""Normal Equation doesn't need feature normalization"""

#  add bias vector
bias = np.ones((len(X),1))
X = np.reshape(X,(len(X),1))
X = np.append(bias,X,axis=1)

"""Normal Equation

![Normal Equation](https://media.geeksforgeeks.org/wp-content/uploads/Untitled-drawing-1-10.png)
"""

#. make a transpose as its used multiple times
transpose = np.transpose(X)
# psuedo inverse the matrix on matrix multiplication
# transpose * X_train is a o(n^3) calculation
# psuedo inverse pinv
part1 = np.linalg.pinv(np.matmul(transpose,X))

part2 = transpose.dot(Y)

#.  define the weights vector
weights = np.matmul(part1,part2)

# bias and the weight
weights

#.  get the predicted by multiplying the matrix(X) and the vector (weights)
predicted_y = X.dot(weights)

plt.scatter(X_temp,y_temp)
plt.plot(X_temp,predicted_y)

r2_score(predicted_y,Y)

np.mean(np.square(np.subtract(predicted_y,Y)))

"""With Feature Normalization the Gradient Descent Algorithm can find the local minima faster"""

X = data.iloc[:, 0].values
Y = data.iloc[:, 1].values

range_ = X.max() - X.min()
X = X - np.average(X)
X = X/range_

X.min()

X.max()

"""Looks Good!"""

#. reshaping the data
X = X.reshape(-1,1)
Y = Y.reshape(-1,1)

model = LinearRegression().fit(X,Y)

model.score(X,Y)

y_predicted = model.predict(X)
y_predicted[0:10]

"""Pretty close"""

plt.scatter(X,Y)
plt.plot(X,y_predicted)

r2_score(y_predicted,Y)