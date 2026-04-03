class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        
        # Validating inputs
        if iterations == 0 or learning_rate == 0:
            return init
        
        x_new = init # placeholder for new value

        for i in range(iterations):
            fofx = 2 * x_new
            x_new = x_new - (learning_rate * fofx)

        return round(x_new, 5)