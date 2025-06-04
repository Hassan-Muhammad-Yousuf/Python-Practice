def mergeSortedArrays(arr1, arr2):

    if not len(arr1):
        return arr2
    if not len(arr2):
        return arr1
    
    final = []
    #array1 = arr1[0]
    #array2 = arr2[0]
    i = 0    
    j = 0

        
    while i < len(arr1) and j < len(arr2):
        #print(arr1[i], arr2[j])
        if arr1[i] < arr2[j]:
            final.append(arr1[i])
            i += 1
        else:
            final.append(arr2[j])
            j += 1
    final.extend(arr1[i:])
    final.extend(arr2[j:])
    return final

        
a = mergeSortedArrays([0, 3, 4, 31], [4, 6, 30])
print(a)