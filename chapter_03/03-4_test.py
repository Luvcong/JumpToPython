
# Q1. 3의 배수의 합 구하기
# while문을 사용하여 1부터 1000까지의 자연수 중 3의 배수 합을 구하세요
a = 1
sum = 0
while a <= 1000 :
    if a % 3 == 0 :
        sum += a
    a += 1
print(sum)

# Q2. 별 표시하기
# while문을 사용하여 5층 모양의 피라미드 별 모양을 표시하세요
i = 0 
while True :
    i += 1
    if i > 5 : break
    print("*" * i)

# Q3. 1부터 100까지 출력하기
# for문을 사용하여 1부터 100까지의 숫자를 출력하세요
for i in range(1, 101) :
    print(i)

# Q4. 평균 점수 구하기
# A학급에 총 10명의 학생이 있고, A학급의 평균 점수를 구하세요
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A :
    total += score
avg = total / len(A)
print(avg)

# Q5. 리스트 컴프리헨션 사용
# 리스트 요소 중에서 홀수만 골라 2를 곱하여 출력하세요
numbers = [1, 2, 3, 4, 5]
result = [num * 2 for num in numbers if num % 2 != 0]
print(result)