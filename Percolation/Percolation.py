import numpy as np
from Union_find import UnionFind

class Percolation:
    def __init__(self,n):
        if n <= 0:
            raise ValueError("Grids under 0 size is not acceptable")
        
        self.n = n
        # n x n grid, all sites blocked (False)
        self.grid = np.zeros((n,n), dtype=bool)
        #union_find with two sites
        self.uf = UnionFind(n*n+2)
        #top site index
        self.top_vir = n * n
        #bottom site index
        self.bot_vir = n * n + 1
        #tracking open sites
        self.open_sites_count = 0
    
    def _index(self, row, col):
        # convertting 2d coordinates into 1D index
        return row * self.n + col
    
    def open(self, row, col):
        if self.isOpen(row, col):
            return
        
        # open the sites
        self.grid[row, col] = True 
        #increment open site count
        self.open_sites_count += 1
        index =  self._index(row, col)

        # connect the top virtual sites if its in the top row
        if row == 0:
            self.uf.union(index, self.top_vir)

        # connect the bottom virtual sites if its in the bottom row
        if row == self.n -1:
            self.uf.union(index, self.bot_vir)

        # connecting open sites adjacency (top,bottom, left, right)
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            newRow, newCol = row + dr, col + dc
            if 0 <= newRow < self.n and 0 <= newCol < self.n and self.isOpen(newRow, newCol):
                self.uf.union(index, self._index(newRow, newCol))

    def isOpen(self, row, col):
        #check if sites in row and col are open
        return self.grid[row, col]
    
    def isFull(self, row, col):
        #check if sites in row and col are connected to top
        return self.uf.connected(self._index(row, col), self.top_vir)
    
    def percolates(self):
        #check percolation (top is connectd to bottom?)
        return self.uf.connected(self.top_vir, self.bot_vir)
    
    def numOfOpenSites(self):
        #returning open sites
        return self.open_sites_count

