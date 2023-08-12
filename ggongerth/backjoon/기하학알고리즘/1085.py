# 직사각형 탈출

# 0 0 wh


# 6 2

# x 로 6-0 칸 혹은 w-6 칸

# y 로 2-0 칸 혹은 h-2 칸


x,y,w,h = map(int, input().split())
cases = [x,w-x,y,h-y]

cases.sort()
print(cases[0])