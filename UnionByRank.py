class DisjointSet:
    def __init__ (self, size):
        #generating the sequence of given input
        self.parent = [i for i in range(size)]
        #all initialized to 0 to keep the tree balanced
        self.rank = [0] * size
    #Find the Representative of the set
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

    #Unites the set that incl i and the set includes j
    def union_by_rank(self, i ,j):
        #find the representative or root node for i
        irep = self.find(i)
        #find the representative or root node for j
        jrep = self.find(j)

        #if elemenst are in the same set no need to unite
        if irep == jrep:
            return
        
        # getting the rank of i's and j's tree
        irank, jrank = self.rank[irep], self.rank[jrep]

        # if i's rank is less than j's rank
        if irank < jrank:
            #move i  under j
            self.parent[irep] = jrank

        # if j's rank is less than i's rank
        elif irank > jrank:
            #move j  under i
            self.parent[jrep] = irank

        #else their rank are same 
        else:
            #moving them doesn't matter
            self.parent[irep] = jrep
            #increment the tree's result
            self.rank[jrep] += 1

    #example Usage
    def main(self):
        size = int(input("Enter the number of elements in the disjoint set: "))
        ds = DisjointSet(size)

        num_unions = int(input("Enter the number of union operations to perform: "))
        
        for _ in range(num_unions):
            i, j = map(int, input("Enter the pair of elements to union (e.g., '0 1'): ").split())
            ds.union_by_rank(i, j)

        # Find the representative of each element
        print("\nResults:")
        for i in range(size):
            print(f"Element {i} belongs to the set with representative {ds.find(i)}")



ds = DisjointSet(size=5)
ds.main()
