from percolation_stats import PercolationStats
from visual import visual_perc

def main():
    n = 20 # grid size
    trials = 100 # number of experiments

    #Run percolation stats
    stats = PercolationStats(n, trials)
    print(f"Mean Percolation threshol: {stats.mean():.4f}")
    print(f"Standard Deviation: {stats.stddev():.4f}")
    print(f"95% Confidence Intrval: [{stats.confidenceLo():.4f}, {stats.confidenceHi():.4f}]")

    #Visualize percolation process
    visual_perc(n, pause_time=0.05)

if __name__ == "__main__":
    main()

