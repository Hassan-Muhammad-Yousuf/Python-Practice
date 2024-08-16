import matplotlib as plt
import numpy as np
import Percolation as Percolation

def visual_perc(n, pause_time=0.1):
    perc = Percolation(n)
    fig, ax = plt.subplots()

    def draw_grid():
        ax.clear()
        ax.imshow(perc.grid, cmap = 'Blues', vmin = 0, vmax = 0)
        ax.set_xtricks([])
        ax.set_ytricks([])
        ax.set_title('Percolation Simulation')
        plt.pause(pause_time)

        while not perc.percolates():
            draw_grid()
            row, col = np.random.randint(0, n, size=2)
            if not perc.isOpen(row,col):
                perc.open(row, col)

        draw_grid()
        plt.show()

if __name__=="__main__":
    visual_perc(20, pause_time=0.05)
