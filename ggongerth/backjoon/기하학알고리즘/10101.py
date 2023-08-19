# 세 각의 크기가 모두 60이면, Equilateral
# 세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
# 세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
# 세 각의 합이 180이 아닌 경우에는 Error

def cal(obj):
    c = 0
    for i in obj:
        c +=i
    if c == 180:
        return True
    else:
        return False

tree = []
for i in range(3):
    tree.append(int(input()))

if tree[0] == 60 and tree[1] == 60 and tree[2] == 60:
    print('Equilateral')
    
else:
    if cal(tree):
        for i in tree:
            if tree.count(i) > 1:
                print('Isosceles')
                break
            else:
                print('Scalene')
                break
    else:
        print('Error')
        
        
정답은
a = int(input())
b = int(input())
c = int(input())

if a == b == c == 60:               # 세 각의 크기가 모두 60인 경우
    print("Equilateral")
elif a + b + c == 180:              # 세 각의 합이 180이고
    if a == b or b == c or c == a:  # 두 각이 같은 경우
        print("Isosceles")
    else:                           # 같은 각이 없는 경우
        print("Scalene")
else:                               # 세 각의 합이 180이 아닌 경우
    print("Error")