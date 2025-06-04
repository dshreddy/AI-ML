# Problem Statement : https://neetcode.io/problems/linear-regression-forward
# Video Explanation : https://youtu.be/dOeYmpS-ySw?si=nO35x3ZOjvsXaoPG

# Helpful functions:
# https://numpy.org/doc/stable/reference/generated/numpy.matmul.html
# https://numpy.org/doc/stable/reference/generated/numpy.mean.html
# https://numpy.org/doc/stable/reference/generated/numpy.square.html

import numpy as np
from numpy.typing import NDArray

'''
################ Terminology
m = number of data points 
n = number of features / attributes
'''

class LinearRegression:
    """
    A simple implementation of Linear Regression using Gradient Descent.
    """
    
    def __init__(
        self,
        X: NDArray[np.float64],  # Feature matrix (m rows = data points, n columns = features)
        Y: NDArray[np.float64],  # Target values (m values, one for each data point)
        num_iterations: int,
        initial_weights: NDArray[np.float64]  # Initial guess for weights (n values)
    ) -> None:

        self.X = X
        self.Y = Y
        self.N = len(Y)  # Number of data points
        self.num_iterations = num_iterations
        self.weights = initial_weights
        self.learning_rate = 0.01

    def train(self) -> NDArray[np.float64]:
        """
        Train the model using gradient descent to minimize mean squared error.
        """
        for _ in range(self.num_iterations):
            prediction = self.__get_model_prediction()

            for j in range(len(self.weights)):
                gradient = self.__get_derivative(prediction, j)
                self.weights[j] -= self.learning_rate * gradient

        return np.round(self.weights, 5)
    
    def predict(self, x):
        return np.dot(x, self.weights)
    
    def __get_model_prediction(self) -> NDArray[np.float64]:
        """
        Predict Y values using current weights.
        """
        return np.squeeze(np.matmul(self.X, self.weights))
            
    def __get_derivative(self, prediction: NDArray[np.float64], j: int) -> float:
        """
        Compute the derivative of loss with respect to weight[j].
        """
        error = self.Y - prediction  # Difference between actual and predicted
        jth_feature = self.X[:, j]   # Column j of X (feature j for all data points)
        return (-2 / self.N) * np.dot(error, jth_feature)

# Example usage
model = LinearRegression(
    X=np.array([
        [1, 2, 3],
        [1, 1, 1]
        ], 
        dtype=np.float64
        ),
    Y=np.array(
        [6, 3], 
        dtype=np.float64
        ),
    num_iterations=10,
    initial_weights=np.array(
        [0.2, 0.1, 0.6], 
        dtype=np.float64
        )
)

model.train()
print(model.weights)

x0 = np.array([1, 2, 3], dtype=np.float64)
print(model.predict(x0))

x1 = np.array([1, 1, 1], dtype=np.float64)
print(model.predict(x1))


