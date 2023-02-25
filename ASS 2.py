r = input()
r = int(r)
y = input()
y = int(y)
sum=0
if r < y:
    for i in range(r,y+1 ):
        sum = sum + i
    print(sum)