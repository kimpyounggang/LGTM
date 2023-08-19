# 네 번째 점


# 세점 -> 축에 평행한 직사각형 생성

# 예제입력
# 5 5
# 5 7
# 7 5

# 에출 
# 7 7

# 좌표계는 데카르트 인듯


# 최대 4개점, 3점 주어지는 경우의 수
# 4!/(3!(4-3)!)

# 4 3 2 1

# 3 2 1


# 12 24 

# 6

# 경우의수 -> 4

# a  b
# c  d

# a b c
# a b d
# a c d
# b c d

# 동일한 값 2개 -> a d 있음
# 최소, 최대, 동일2개

# def has_duplicates(lst):
#     for item in lst:
#         if lst.count(item[2]) > 1:
#             return True
#     return False

# vertexs = []
# for i in range(3):
#     x,y = map(int, input().split())
#     vertexs.append([x,y,x*y])

# if has_duplicates(vertexs):
#     # 동일한값 있음
#     vertexs.sort(key=lambda x: vertexs[2])
#     if min(vertexs) == vertexs[0]:
#         # 최대값 없음
#         m = max(vertexs[1])
#         print(f'{m} {m}')
#     else:
#         # 최대값 있음
#         m = min(vertexs[1])
#         print(f'{m} {m}')
# else:
#     # 동일한값 없음
#     vertexs.sort(key=lambda x: vertexs[2])
#     print(f'{vertexs[1][1]} {vertexs[1][0]}')
    


x_nums = []
y_nums = []
for _ in range(3):
    x, y = map(int, input().split())
    x_nums.append(x)
    y_nums.append(y)

for i in range(3):
    if x_nums.count(x_nums[i]) == 1:
        x4 = x_nums[i]
    if y_nums.count(y_nums[i]) == 1:
        y4 = y_nums[i]
print(x4, y4)


# 답 보고 넘어감

