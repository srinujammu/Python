# Part1

x =(1,2,3,4,5)

for i in x:
    print('{}'.format(i))

# Part2 Data frame

y =[1,2,3,4,5]
y[4] = 45
for i in y:
    print('{}'.format(i))

# Part3

z =range(5)
#y[4] = 45
for i in z:
    print(' z is {}'.format(i))
# Part4 List of items

k =list(range(5))
k[4] = 45
for i in k:
    print(' k is {}'.format(i))

# dictionary items

L ={'One':1, 'Two':2,'Three':3, 'four':4}
k[4] = 45
for k, v in L.items():
    print('k: {} , v : {}'.format(k,v))