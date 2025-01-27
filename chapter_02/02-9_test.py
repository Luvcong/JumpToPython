
# Q1. 평균 점수 구하기
korean  = 80
english = 75
math    = 55
avg = (korean + english + math) / 3

# Q2. 홀수, 짝수 판별하기
# 자연수 13이 홀수인지 짝수인지 판별하는 코드 작성
odd  = 13 % 2 == 0
even = 13 % 2 == 1
print(odd)      # False로 출력되므로 홀수
print(even)     # True로 출력되므로 홀수

# Q3. 주민등록번호 나누기
# 881120-1068234
# YYYYMMDD / 숫자 부분으로 출력
pin      = "881120-1068234"
yyyymmdd = pin.split('-')[0]
num      = pin.split('-')[1]
print(yyyymmdd)
print(num)

yyyymmdd = pin[:6]
num      = pin[7:]
print(yyyymmdd)
print(num)

# Q4. 주민등록번호 인덱싱
# 성별을 나타내는 숮자 출력
pin = "881120-1068234"
print(pin[7])

# Q5. 문자열 바꾸기
# a:b:c:d -> a#b#c#d
a = "a:b:c:d"
b = a.replace(':', '#')
print(b)

# Q6. 리스트 역순 정렬
# [1, 3, 5, 4, 2] -> [5, 4, 3, 2, 1]
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

# Q7. 리스트를 문자열로 만들기
# ['Life', 'is', 'too', 'short'] > Life is too short 문자열로 출력
a = ['Life', 'is', 'too', 'short']
result =  " ".join(a)
print(result)

# Q8. 튜플 더하기
a = (1, 2, 3)
a = a + (4, )
print(a)

# Q9. 딕셔너리 키
# 오류 나는 코드 + 이유 작성
a = dict()
print(a)    # {}

# a[[1]] = 'python' 오류 발생
# 딕셔너리는 인덱스 접근이 아니라  key로 접근하기 때문

# Q10. 딕셔너리 값 추출하기
# a에서 'B'에 해당하는 값 추출
a = {'A':90, 'B':80, 'C':70}
# result = a.get('B')
result = a.pop('B')
print(a)
print(result)

# Q11. 리스트에서 중복 제거
a    = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b    = list(aSet)
print(b)

# Q12. 파이썬 변수
a = b = [1, 2, 3]
a[1] = 4
print(b)    # [1, 4, 3] 출력 -> a와 b는 모두 동일한 메모리 주소를 갖고 있기 때문에 변경됨
