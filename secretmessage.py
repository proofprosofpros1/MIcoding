import os 

team_path = 'C:\\temp'
fin = open(os.path.join(team_path, 'input3.txt'), 'r')

N = int(fin.readline().strip())
answer = []
for x in range(N):
    s1 = fin.readline().strip()
    s2 = fin.readline().strip()
    s3 = ''
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            s3 += str(s2[i])
        elif s1 == s2:
            s3 = "No change"
    answer.append(s3 + '\n')

fout = open(os.path.join(team_path, 'output3.txt'), 'w')
fout.write(''.join(answer))
fout.close()
