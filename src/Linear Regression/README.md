## 💡 Beginner-Friendly Explanation of Linear Regression:

### 🎯 What is Linear Regression?

1. Linear Regression is a way to **predict a number (y)** based on some **input features (x)**.
    Example:
    * You want to predict someone's salary (y) based on years of experience and education level (x).
2. We assume the relationship between input features and output is linear and define the following equation:
    $$
    \hat{Y} = w_0x_0 + w_1x_1 + \dots + w_nx_n
    $$
    Where:
    * `w` are the **weights** (parameters we need to learn),
    * `x` are the **features** of each data point,
    * $\hat{Y}$ is the **predicted value**.
3. Our main goal is to find the most accurate set of weights, accurate here is defined as the set of weights which gives the least Mean Squared Error (MSE)
    * Calculates the **gradient (partial derivative)** of the loss function (MSE) with respect to one weight.
    * Uses the formula for the derivative of MSE w\.r.t a weight $w_j$:
    $$
    \frac{\partial \text{MSE}}{\partial w_j} = -\frac{2}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i) x_{ij}
    $$
4. We use gradient descent to find the most accurate set of weights which minises the MSE function
