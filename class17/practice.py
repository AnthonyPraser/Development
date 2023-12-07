sum = 0
count = 0
x = int(input('Enter a number: '))
for i in range(10,x,5):
 sum += i
count += 1
print(sum)
print(sum/count)