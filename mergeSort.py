import random
def merge(S1,S2,S):
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i]<S2[j]):
            S[i+j] = S1[i]
            i +=1
        else:
            S[i+j] = S2[j]
            j += 1
    return S


def merge_Sort(S):
    n = len(S)
    if n< 2:
        return
    
    mid = n // 2
    S1 = S[0:mid]
    S2 = S[mid:n]

    merge_Sort(S1)
    merge_Sort(S2)
    
    S = merge(S1,S2,S) 
    return S

toSort = [random.randint(1,10) for i in range(10)]
print(toSort)
print(merge_Sort(toSort))