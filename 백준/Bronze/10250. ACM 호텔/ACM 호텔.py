s = int(input())

for i in range(s):
    h, w, n = map(int,input().split())
    xx = n//h+1
    yy = n%h
    if n % h == 0:
        xx = n//h
        yy = h
    print(f'{yy*100 + xx}')
