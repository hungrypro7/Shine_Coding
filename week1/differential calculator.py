# 미분계산기 만들기 - 전공자용
var = input("독립 변수를 입력하세요 : ")
ex = input("다항식을 입력하세요 : ")
ans = ''
point = 0
for idx, j in enumerate(ex):    # 인덱스, 원소
    if j == '+' or j == '-':
        point = idx
        point += 1
        ans += j
    if j == 'x':
        if int(ex[idx+2]) >= 2:
            if idx - point >= 1:    # 앞에 계수가 있는 경우
                ans += str(int(ex[point:idx]) * int(ex[idx+2]))
                ans += 'x^'
                ans += str(int(ex[idx+2])-1)
            else:       # 앞에 계수가 없는 경우
                ans += str(int(ex[idx+2]))
                ans += 'x^'
                ans += str(int(ex[idx+2])-1)
        elif int(ex[idx+2]) == 1:
            if idx - point >= 1:    # 앞에 계수가 있는 경우
                ans += str(int(ex[point:idx]) * int(ex[idx+2]))
            else:       # 앞에 계수가 없는 경우
                ans += '1'

    if idx == len(ex)-1 and '^' not in ex[point:idx]:   # 상수항이 있으면 0을 ans에 넣어줌
        ans += '0'

print('결과는 ' + ans + ' 입니다.')