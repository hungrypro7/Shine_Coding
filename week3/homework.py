import random
score = random.sample(range(0, 100), 20)
score.sort()
print(score)
print("점수가 가장 좋은 사람 : ", score[-1])
print("점수가 중간인 사람 : ", score[len(score)//2])
print("점수가 가장 낮은 사람 : ", score[0])

print()
print("=====전공자용=====")
fib = [1, 1]
for i in range(1, 13):
    fib.append(fib[i]+fib[i-1])
print("13번째 사람의 점수는", fib[12], "입니다.")
