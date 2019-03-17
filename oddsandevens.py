import os
team_path = 'C:\\temp'
fin = open(os.path.join(team_path, 'input5.txt'), 'r')
N = int(fin.readline().strip())
res2 = []
for _ in range(N):
    s = sorted(map(int, fin.readline().strip().split()))
    odd = []
    even = []
    res = []
    for num in s:
        if num % 2 == 0 or num == 0:
            even.append(num)
        else:
            odd.append(num)
    res = odd + even
    res2.append(res)
fout = open(os.path.join(team_path, 'output5.txt'), 'w')
fout.write(''.join(str(res2)))
fout.close()
