#Swap values in a vector by k places
w = [90,91,92,93,94]
k = 2
k:len(w)
print(w[-k:len(w)]+ (w[0:len(w)-k]))
