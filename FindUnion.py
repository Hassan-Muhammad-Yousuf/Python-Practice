#Find the Representative of the set

def find(i):
    #if i is the parent of itself
    if (parent[i] == i):
        
        #Return i  becuase it is the parent of itself
        return i
    else:
        #else if i is not the parent so we call find function to find it
        return find(parent[i])

#Unites the set that incl i and the set includes j
def union(parent, rank, i ,j):
    #find the representative or root node for i
    irep = find(parent, i)
    #find the representative or root node for j
    jrep = find(parent, j)

    #Choose any parent either its i or j for the representative or root node
    parent[irep] = jrep
