
# 제어문 - 반복문(for)
'''
[ for문의 기본 구조 ]
for 변수 in 리스트(or 튜플, 문자열) :
    수행할 문장 1
    수행할 문장 2
    수행할 문장 3
    ...
'''

# 1. for문 기본 활용
test_list = ['one', 'two', 'three']
for i in test_list :
    print(i)

# 2. 다양한 for문 사용
a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a :
    print(first + last)
# a 리스트의 요소값이 튜플이기 때문에 각각의 요소가 자동으로 (first, last) 변수에 대입된다

# 3. for문 응용
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks :
    number += 1
    if mark >= 60 :
        print("%d번 학생은 합격입니다" % number)
    else :
        print("%d번 학생은 불합격입니다" % number)

# 4. for문과 continue문
# 60점 이상인 사람에게 축하 메시지를, 나머지 사람에게는 메시지를 전송하지 않는 코드 작성
# 내가 작성한 답답
score = [90, 25, 67, 45, 80]
number = 0
for i in score :
    number += 1
    if i >= 60 :
        print("%d번 합격입니다! 축하합니당")
    else :
        continue
# 책 정답
score = [90, 25, 67, 45, 80]
number = 0
for i in score :
    number += 1
    if i < 60 :
        continue
    print("%d번 합격입니다! 축하합니다")

# 5. range 함수
# range(시작숫자, 끝숫자) : 끝 숫자는 포함되지 않음!

# 0부터 10 미만의 숫자를 포함하는 range 객체 생성
a = range(10)
print(a)    # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# range 함수 예시
add = 0
for i in range(1, 11) :
    add = add + i
    print(add)  # 55

# range를 이용해서 점수가 60졈 이상이면 축하 메세지를, 그렇지 않으면 continue 코드 작성
marks = [90, 25, 67, 45, 80]
for num in range(len(marks)) :
    if marks[num] < 60 :
        continue
    print("%d번 합격입니다 축하합니다" % (num + 1))

'''
Q. for문과 range 함수를 사용하여 1부터 100까지 더하는 코드 작성
'''
sum = 0
for num in range(1, 101) :
    sum += num
print(sum)

'''
Q. for문과 range 함수를 사용하여 구구단 코드 작성
'''
for i in range(1, 10) :
    for j in range(1, 10) :
        print(i * j, end=" ")
    print('')

for i in range(1, 10) :
    for j in range(1, 10) :
        print("%d X %d = %d" % (i, j, (i * j)))
    print('')

# 6. 리스트 컴프리헨션 사용하기
# 리스트 안에 for문을 포함하는 list comprehension

# 기본 for문 예시시
a = [1, 2, 3, 4]
result = []
for num in a :
    result.append(num * 3)
print(result)

# 리스트 컴프리헨션 사용
# [표현식] [for] [항목] [in] [반복객체] [if 조건문]
a = [1, 2, 3, 4]
result = [num * 3 for num in a]
print(result)

# 리스트 컴프리헨션 안에 if 조건문 사용
# 짝수에만 3을 곱하여 출력
a = [1, 2, 3, 4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)

# 여러 개의 for문을 사용하는 것도 가능
'''
표현식  for 항목1 in 반복객체1 if 조건문1
        for 항목2 in 반복객체2 if 조건문2
        for 항목3 in 반복객체3 if 조건문3
        ...
'''

# 구구단의 모든 결과를 리스트 컴프리헨션을 사용하여 리스트에 담기
result = [x * y for x in range(2, 10)
                for y in range(1, 10)]
print(result)
