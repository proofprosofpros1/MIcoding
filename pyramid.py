import os

team_path = 'C:\\temp'
fin = open(os.path.join(team_path, 'input4.txt'), 'r')
# N = int(fin.readline().strip())
# for x in range(N):
#     res = []
#     S = int(fin.readline().strip())
#     for x in range(1, S+1):
#         res.append(x * x)
#         print(res)
# fout = open(os.path.join(team_path, 'output4.txt'), 'w')
# fout.write(''.join(res))
# fout.close()
res = []
a = int(fin.readline().strip())
for i in range(a):
    s = int(fin.readline().strip()) 
    sum = 0
    for i in range(s+1):
        sum += i*i
    res.append(str(sum))

fout = open(os.path.join(team_path, 'output4.txt'), 'w')
fout.write('\n'.join(res))
fout.close()
