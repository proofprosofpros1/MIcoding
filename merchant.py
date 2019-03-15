N = int(input())
for i in range(N):
    #a, p, t = map(int, input().split())
    tmp = input().split()
    a = int(tmp[0])
    p = int(tmp[1])
    t = float(tmp[2])
    res = a * p
    res = (res*(1-t))
    print(res)
