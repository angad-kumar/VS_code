from matplotlib import pyplot as plt

x = [24, 30, 25, 30, 29, 14, 12, 29, 21, 28, 24, 28, 12, 17, 18, 14, 13, 24, 18, 18, 28, 22, 24, 27, 14, 23, 26, 23, 15, 27, 24, 16, 19, 20, 25, 30, 27, 14, 21, 25, 26, 28, 17, 15, 19, 20, 14, 15, 27, 20, 22, 30, 30, 15, 20, 13, 22, 25, 25, 30, 29, 15, 20, 25, 12, 20, 15, 25, 15, 14, 27, 19, 28, 22, 24, 21, 30, 25, 18, 12, 18, 19, 19, 18, 13, 21, 28, 25, 16, 13, 23, 23, 27, 18, 26, 21, 22, 15, 27, 25]
  
# Y-axis values
y = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99]

test = []
sum = []
set_value = 15
# i = 10
# print(x[i])



for i in range(0,100):
    error = set_value - x[i]
    test.append(error)

for i in range(0,100):
    data = x[i] + test[i]
    sum.append(data)


plt.plot(y,sum)
plt.plot(y,test)
plt.show()

