import matplotlib.pyplot as plt
import numpy as np
from percolation import Percolation

def visual_perc(n, pause_time=0.1):
    perc = Percolation(n)  # Create a Percolation instance with grid size n
    fig, ax = plt.subplots()  # Create a figure and axis for plotting

    def draw_grid():
        # Clear the current axis and display the grid
        ax.clear()
        ax.imshow(perc.grid, cmap='Blues', vmin=0, vmax=1)  # Display grid with correct value range
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title('Percolation Simulation')
        plt.pause(pause_time)  # Pause to update the plot

    # Initial drawing
    draw_grid()

    # Open sites until the system percolates
    while not perc.percolates():
        row, col = np.random.randint(0, n, size=2)  # Choose random row and column
        if not perc.isOpen(row, col):
            perc.open(row, col)  # Open the chosen site
        draw_grid()  # Draw the grid after each site is opened

    # Final drawing to show the percolated state
    draw_grid()

    # Keep the plot open until manually closed
    plt.show(block=True)

if __name__ == "__main__":
    visual_perc(20, pause_time=0.05)

