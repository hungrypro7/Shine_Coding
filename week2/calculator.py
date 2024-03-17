# 계산기 만들기
ex = input("식을 입력하세요 ")
ans = 0
for i, j in enumerate(ex):
    if j == "+":
        ans = int(ex[:i]) + int(ex[i+1:])
    elif j == "-":
        ans = int(ex[:i]) - int(ex[i+1:])
    elif j == "*":
        ans = int(ex[:i]) * int(ex[i+1:])
    elif j == "/":
        ans = int(ex[:i]) / int(ex[i+1:])

print(f"정답은 {ans} 입니다.")
