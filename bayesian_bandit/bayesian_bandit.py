import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import beta

"""
Beta distribution is the conjugate priors probability distribution

for the Bernoulli, binomial, negative binomial, and Geometric distribution
"""

NUM_TRIALS = 2000
BANDIT_PROBS = [0.2, 0.5, 0.75]

class Bandit:
    def __init__(self, p):
        self.p = p
        self.a = 1
        self.b = 1

    def pull(self):
        """
        Pull the arm of the bandit
        
        Generate a random number

        If its less than the prob, WIN!
        Else, you lost to the bandit!
        """
        return np.random.random() < self.p
    
    def sample(self):
        return np.random.beta(self.a, self.b)
    
    def update(self, x):
        """
        Conjugate priors.
        X is either 0 or 1
        """
        self.a += x
        self.b += 1 - x
    
def plot(bandits, trial):
    # Between 0 and 1, 200 points to make it smooth
    x = np.linspace(0,1, 200)

    for b in bandits:
        y = beta.pdf(x, b.a, b.b)
        plt.plot(x, y, label = "Real p: %0.4f" % b.p)
    plt.title("Bandit distributions after %s trials" % trial)
    plt.legend()
    plt.show()

def experiment():
    bandits = [Bandit(p) for p in BANDIT_PROBS]

    sample_points = [5, 10, 20, 50, 100, 200, 1000, 1500, 1999]

    for i in range(NUM_TRIALS):
        # Bandit we pull
        bestb = None

        maxsample = -1

        # debugging
        allsamples = []

        for b in bandits:
            sample = b.sample()
            allsamples.append("%.4f" % sample)

            if sample > maxsample:
                maxsample = sample
                bestb = b
            
        if i in sample_points:
            print("Current samples: %s" % allsamples)
            plot(bandits, i)

        # Pull the best bandit's arm
        x = bestb.pull()
        # Update the best bandit with the data
        bestb.update(x)

if __name__ == "__main__":

    """
    The point of the experiment
    is to find the best bandit to pull from

    Exploit the best known bandit
    while leaving some room for exploration
    But not too much exploration because we want to exploit the best one
    """
    experiment()
