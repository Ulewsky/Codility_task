#function that create list from 0 to n
n = int(input('Write natural number '))
k = []
def chain(n):
    for i in range(0,n+1):
        k.append(i)
    print(k)
chain(n)
