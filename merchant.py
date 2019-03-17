import os
team_path = 'C:\\temp'
#fin = open('input.txt', 'r')
# count = ''
fin = open(os.path.join(team_path, 'input2.txt'), 'r')
res = []
N = int(fin.readline().strip())
for i in range(N):
   a, p, t = map(float, fin.readline().strip().split())
   tot = a * p - a * p * t
   res.append(str(tot))
   # res = a * p
   # res = (res*(1-t))
   # count += str(res)
   # count += '\n'
fout = open(os.path.join(team_path, 'output2.txt'), 'w')
# fout.write(count)
fout.write('\n'.join(res))
fout.close()
