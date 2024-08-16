class UnionFind:
    def __init__(self, n):
        # Initialize the union-find structure with n elements
        self.parent = list(range(n))  # Each element is its own parent initially
        self.rank = [0] * n  # Initialize ranks to 0 for all elements

    def find(self, i):
        # Find the root of element 'i' with path compression
        if self.parent[i] == i:
            # If 'i' is the parent of itself, return 'i'
            return i
        else:
            # Recursively find the root and apply path compression
            root = self.find(self.parent[i])
            self.parent[i] = root  # Make 'i' directly point to the root
            return root

    def union(self, i, j):
        # Union the sets containing elements 'i' and 'j'
        rooti = self.find(i)
        rootj = self.find(j)

        if rooti != rootj:
            # Attach smaller tree under larger tree, based on rank
            if self.rank[rooti] > self.rank[rootj]:
                self.parent[rootj] = rooti
            elif self.rank[rooti] < self.rank[rootj]:
                self.parent[rooti] = rootj
            else:
                self.parent[rootj] = rooti
                self.rank[rooti] += 1  # Increase rank if both trees have the same rank

    def connected(self, i, j):
        # Check if elements 'i' and 'j' are in the same set
        return self.find(i) == self.find(j)
