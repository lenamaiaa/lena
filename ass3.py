index =9
A = [0,1]
i = 2
while i < index:
    A.append(A[i-1]+A[i-2])
    i = i+1
print(A)
