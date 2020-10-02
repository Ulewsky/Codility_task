def solution(A):
    p = [0]
    n = [0]
    for i in range(0,len(A)):
        if A[i] % 2 == 0:
            p.append(A[i])
        else:
            n.append(A[i])
    return max(p)+max(n) 
