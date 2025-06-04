# Problem Statement : https://neetcode.io/problems/gradient-descent
# Video Explanation : https://youtu.be/MECp_yVQ7ao?si=rDOc1qLLFCmEm4LQ

class GradientDescent:
    '''
    A class that uses the gradient descent algorithm to find the minimum of f(x) = x^2.
    '''

    def get_minimizer(self, iterations: int, learning_rate: float, x: float) -> float:
        '''
        Finds the value of x that minimizes the function f(x) = x^2.

        Parameters:
        - iterations (int): The number of steps (iterations) we take while adjusting x.
        - learning_rate (float): Controls how big each step is.
        - init (float): Starting value of x.

        Returns:
        - minimizer (float): The value of x where f(x) = x^2 is minimized (ideally close to 0).
        '''

        for _ in range(iterations):
            derivative_of_f_at_x = 2 * x  # Calculate the slope at the current x
            x = x - (learning_rate * derivative_of_f_at_x)  # Step in the opposite direction of the slope

        return round(x, 5) # Round off the final value to 5 decimal places


# Example usage:
obj = GradientDescent()
result = obj.get_minimizer(iterations=100, learning_rate=0.1, x=10)
print(f"Minimized value of x: {result}")
