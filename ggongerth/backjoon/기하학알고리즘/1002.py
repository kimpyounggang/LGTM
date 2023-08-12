# 터렛

x1, y1 -> mx,my = r1

x2, y2 -> mx,my = r2


r = 반지름

두 원의 접점 문제.
접점 0개 (접하지 않음)
접점 1개 (r1+r2 =d , rt1 or rt2 = d)
접점 2개 (rt1**2 d**2 = rt2**2) (r1, r2 중 작은놈이 rt1)
무한대(원이 같음 -> x,y,r 모두 같음)


numb = int(input())
for i in range(numb):
    x1,y1,r1,x2,y2,r2 = map(int, input().split())
    #d
    (x1-x2)**2+(y1-y2)**2