N = int(input())

x = list(map(int, input().split()))
y = list(map(int, input().split()))

x.sort()
y.sort(reverse = True)
sum = 0        
for i, j in zip(x,y):
    sum += i*j
print(sum)
