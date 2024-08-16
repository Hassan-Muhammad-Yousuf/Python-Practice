class UnionFind:
    def __init__(self,n):
        #initialize the union find structure with n element
        self.parent = list(range(n))  # each element is their own parent 
        self.rank = [1 * n] #tracking tee depth by rank

    def find(self,i):
    #if i is the parent of itself
        if (self.parent[i] == i):
            
            #Return i  becuase it is the parent of itself
            return i
        else:
            #else if i is not the parent so we call find function to find it
            result = self.find(self.parent[i])
            #Storing the i's node which is root in the results
            self.parent[i] = result
            
            return result 
    
    def union(self, i, j):
        rooti = self.find(i)
        rootj = self.find(j)

        if rooti != rootj:
            #attach similar tree under larger tree sorted by rank
            if self.rank[rooti] > self.rank[rootj]:
                self.parent[rootj] = rooti
            if self.rank[rooti] < self.rank[rootj]:
                self.parent[rooti] = rootj
            else:
                self.parent[rootj] = rooti

                self.rank[rooti] += 1 #increase rank if both have the same rank
    
    def connected(self, i, j):
        #checking the elements are in smae set
        return self.find[i] == self.find[j]
    
        

