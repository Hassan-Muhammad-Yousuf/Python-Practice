class UnionFind:
    # Self fuction init
    def __init__(self, element):
        #initialising the parent
        self.parent = [i for i in range(element)]
        #initialising the size 
        self.size = [1] * element

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

    def main():
        # Get the number of elements from the user
        n = int(input("Enter the number of elements: "))
        
        # Initialize UnionFind instance
        unionFind = UnionFind(n)

        # Get the number of union operations from the user
        num_operations = int(input("Enter the number of union operations: "))
        
        for _ in range(num_operations):
            i, j = map(int, input("Enter the pair of elements to union (e.g., '0 1'): ").split())
            unionFind.union_by_size(i, j)
        
        # Print the representative of each element after unions
        print("\nResult:")
        for i in range(n):
            print(f"Element {i}: Representative = {unionFind.find(i)}")

UnionFind.main()