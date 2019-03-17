import os
team_path = 'C:\\temp'
fin = open(os.path.join(team_path, 'input6.txt'), 'r')
arr = []
N = int(fin.readline().strip())
for x in range(N):
    s = int(fin.readline().strip())
    res = 0
    while s > 0:
        if s == 1: 
            print(res)
            break
        elif s % 2 == 0:
            s = s/2
            res += 1
        elif s % 2 == 1:
            s = (3*s) + 1
            res += 1
    arr.append(str(res))
fout = open(os.path.join(team_path, 'output6.txt'), 'w')
fout.write('\n'.join(arr))
fout.close()
