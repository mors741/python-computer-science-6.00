def selSort(L):
    print L
    for i in range(len(L)-1):
        minIndex = i
        minValue = L[i]
        j = i + 1
        while j < len(L):
            if L[j] < minValue:
                minIndex = j
                minValue = L[j]
            j += 1
        temp = L[i]
        L[i] = minValue
        L[minIndex] = temp
        print L
