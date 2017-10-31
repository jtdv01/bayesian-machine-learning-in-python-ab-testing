import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import beta, norm

# Number of iterations
T = 501

true_ctr = 0.5

# Beta priors, which is a uniform
a,b = 1,1

# Where to plot
plot_indices = (10, 20, 30, 50, 100, 200, 500)

# Initialise an empty with T number of iterations
data = np.empty(T)

for i in range(T):

    # Draw a sample from the bandit
    x = 1 if np.random.random() < true_ctr else 0 

    data[i] = x

    # Update the beta distribution
    a += x
    b += 1 - x

    if x in plot_indices:
        # Etimated ctr is data up to i
        p = data[:i].mean()
        n = i + 1

        std = np.sqrt(p * (1-p) /n)

        # Plot the gaussian
        x = np.linspace(0, 1, 200)

        g = norm.pdf(x, loc=p, scale= std)
        plot.plot(x, g, label = "Gaussian Approximation")

        posterior = beta.pdf(x, a=a, b=b)
        plt.plot(x, posterior, label= 'Beta Posterior')
        plt.legend()
        plt.title(f"N: {n}")
        plt.show()