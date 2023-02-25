import matplotlib.pyplot as plt

X1 = [0,1,3,4,5]
Y1 = [1,2,3,4,5]
X2 = [1,3,5,7]
Y2 = [2,4,6,8]
plt.plot(X1, Y1)
plt.plot(X2, Y2)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('test',fontsize=20,color='blue')
plt.show()