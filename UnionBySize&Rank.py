class Union_Rank_Size:
    def __init__(self, element):
        #initialising the parent
        self.parent = [i for i in range(element)]
        #initialising the size by 1s for union by size
        self.size = [1] * element
        #initialising the size by 1s for union by rank
        self.rank = [0] * element
        # Flag to determine whether to use rank or size
        self.use_rank = True
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

    #uniting the sets which includes i and j by sizes
    def union_by_size(self, i, j):
        #find the representative or root node for i
        irep = self.find(i)
        #find the representative or root node for j
        jrep = self.find(j)

        #if elemenst are in the same set no need to unite
        if irep == jrep:
            return
        #Getting the size of i's and j's tree
        isize, jsize =  self.size[irep], self.size[jrep]
        #if i's tree is less than j's tree
        if isize < jsize:
            #move i under j
            self.parent[irep] = jrep
            #increment j's tree size by i's tree
            self.size[jrep] += self.size[irep] 
        else:
            #move j under i
            self.parent[jrep] = irep
            #increment i's tree size by j's tree
            self.size[jrep] += self.size[irep]
    def union(self, i, j):
        if self.use_rank:
            self.union_by_rank(i,j)
        else:
            self.union_by_size(i,j)

    def main():
        # Get the number of elements from the user
        n = int(input("Enter the number of elements: "))

        # Ask if user wants to use union by rank or size
        use_rank = input("Use union by rank? (yes/no): ").strip().lower() == 'yes'

        # Initialize Union_Rank_Size instance
        unionFind = Union_Rank_Size(n)
        unionFind.use_rank = use_rank

        # Get the number of union operations from the user
        num_operations = int(input("Enter the number of union operations: "))

        # Perform union operations based on user input
        for _ in range(num_operations):
            # Read a pair of elements to unite
            i, j = map(int, input("Enter the pair of elements to union (e.g., '0 1'): ").split())
            # Perform the union operation
            unionFind.union(i, j)

        # Print the representative of each element after all unions
        print("\nResult:")
        for i in range(n):
            print(f"Element {i}: Representative = {unionFind.find(i)}")

    # Ensure this script runs the main function if executed directly
if __name__ == "__main__":
    Union_Rank_Size.main()
