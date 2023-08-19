# 터렛

# x1, y1 -> mx,my = r1

# x2, y2 -> mx,my = r2


# r = 반지름

# 두 원의 접점 문제.
# 접점 0개 (접하지 않음)
# 접점 1개 (r1+r2 =d , rt1 or rt2 = d)
# 접점 2개 (rt1**2 d**2 = rt2**2) (r1, r2 중 작은놈이 rt1)
# 무한대(원이 같음 -> x,y,r 모두 같음)

import math
numb = int(input())
for i in range(numb):
    x1,y1,r1,x2,y2,r2 = map(int, input().split())
    #d
    distance = math.sqrt((x1-x2)**2+(y1-y2)**2)
    
    if distance == 0 and r1 == r2 :  # 두 원이 동심원이고 반지름이 같을 때
        print(-1)
    elif abs(r1-r2) == distance or r1 + r2 == distance:  # 내접, 외접일 때
        print(1)
    elif abs(r1-r2) < distance < (r1+r2) :  # 두 원이 서로다른 두 점에서 만날 때
        print(2)
    else:
        print(0)  # 그 외에