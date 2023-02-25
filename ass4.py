A = [1, 2, 4, 6,7,8]
B = [2, 3, 6]
i = 0
j = 0
C = []
while i < len(A) and j < len(B):
    if A[i] < B[j]:
        C.append(A[j])
        i = i + 1
    else:
        C.append(B[j])
        j = j + 1
while j < len(B):
    C.append(B[j])
    j = j + 1
while i < len(A):
    C.append(A[i])
    i += 1

print(C)