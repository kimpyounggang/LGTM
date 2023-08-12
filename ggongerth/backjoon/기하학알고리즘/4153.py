# 작각 삼각형

cases=[]
while True:
    a,b,c = map(int, input().split())
    if a ==0 and b ==0 and c == 0:
        break
    else:
        cases.append([a,b,c])
for case1 in cases:
    case1.sort()
    if case1[0]**2+case1[1]**2-case1[2]**2 == 0:
        print('right')
    else:
        print('wrong')
    