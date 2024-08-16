import numpy as np
import random
from Percolation import Percolation


class PercolationStats:
    def __init__(self, n, trials):
        # Check if the grid and number of trials are valid
        if n <= 0 or trials <= 0:
            raise ValueError("Grids and trials under 0 is nbot acceptable")
        
        self.trials = trials
        self.thresholds = []

        for _ in range(trials):
            # running percolation for specific num of trails 
            perc = Percolation(n)
            while not perc.percolates():
                # continue to open the sites until th=e grid percolates
                row, col = random.randint(0, n-1), random.randint(0, n-1)
                #generate random row and col indice to select the site grid
                if not perc.isOpen(row, col):
                    perc.open(row, col)

            self.thresholds.append(perc.numOfOpenSites() / (n * n))
            #append the threshold to the list of thresholds

    def mean(self):
        #calculating mean of percolation thresholds
        return np.mean(self.thresholds)
    
    def stddev(self):
        #calculating standard deviation of percolation thresholds
        return np.std(self.thresholds, ddof=1)
    
    def confidenceLo(self):
        # calculating lower bound of 95% confidence interval
        mean = self.mean()
        margin = 1.96 * self.stddev() / np.sqrt(self.trials)
        return mean - margin
    
    def confidenceHi(self):
        # calculating upper bound of 95% confidence interval
        mean = self.mean()
        margin = 1.96 * self.stddev() / np.sqrt(self.trials)
        return mean + margin
