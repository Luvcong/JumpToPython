
# 제어문 - 조건문(if)
# 조건문 : 참과 거짓을 판단하는 문장을 의미
money = True
if money :
    print("택시를 타고 가세용")
else :
    print("걸어가세용")
# money가 true이기 때문에 "택시를 타고 가세용"이라는 문구가 출력된다.

'''
[if문 기본 문법]

if 조건문 :
    수행할 문장_1
    수행할 문장_2
else :
    수행할 문장_A
    수행할 문장_B

** 주의할 점
1) 수행할 문장들이 모두 들여쓰기가 되어 있어야 함
2) 수행할 문장들의 들여쓰기 깊이가 모두 같아야 함
3) 조건문 뒤에 콜론(:)을 꼭 붙어야 함
'''

# 1. 비교 연산자
# < , > , == , != , >= , <=
x = 3
y = 2
print(x > y)    # True
print(x < y)    # False
print(x != y)   # True

# Q. 만약에 3,000원 이상의 돈을 가지고 있으면 택시를 타고, 그렇지 않으면 걸어가세요
money = 7200
if money >= 3000 :
    print("택시타세용")
else :
    print("걸어가세용")

# 2. and / or / not
# Q. 돈이 3,000원 이상 있거나 카드가 있다면 택시를 타고 가고, 그렇지 않으면 걸어가세요
money = 2000
card  = False
if money >= 3000 or card :
    print("택시타세용")
else :
    print("걸어가세용")

# 3. in / not in
# 값이 있는지 없는지 확인하는 조건문

# x in 리스트 : x not in 리스트
# x in 튜플   : x not in 튜플
# x in 문자열 : x not in 문자열

print(1 in [1, 2, 3])           # True
print(1 not in [1, 2, 3])       # False

print('a' in ('a', 'b', 'c'))   # True
print('j' not in 'python')      # True

# Q. 만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어가세요
poket = ['key', 'cellphone', 'money']
if 'money' in poket :
    print("택시양")
else :
    print("걸어가용")

'''
Q. '주머니에 카드가 없으면 걸어가고, 있으면 버스를 타고 가세요' 라는 조건식 작성
'''
poket = ['card', 'money', 'key']
if 'card' not in poket :
    print("걸어가세용")
else :
    print("버스타세용")

# 4. pass
# 조건문의 참, 거짓에 따라 실행할 행동을 아무런 일도 하지 않도록 설정해주는 역할
poket = ['card', 'money', 'key']
if 'money' in poket :
    pass
else :
    print("카드 꺼내기")

# pass를 사용한 위 조건식은 한 줄로 작성할 수도 있다
if 'money' in poket : pass
else : print("카드 꺼내기")

# 5. elif
# if-else를 이용하는 경우
poket = ['paper', 'cellphone']
card = True
if 'money' in poket :
    print("택시틀 타고 가세요")
else :
    if card :
        print("택시를 타고 가세요")
    else :
        print("걸어가세용")
# elif를 이용하는 경우
poket = ['paper', 'cellphone']
card = True
if 'money' in poket :
    print("택시를 타고 가세용")
elif card :
    print("택시를 타고 가세용")
else :
    print("걸어가세용")

# 6. 조건부 표현식
# 변수 = [조건문 참인 값] [if] [조건문] [else] [조건문 거짓인 값]
# 예시
score = 80
if score >= 60 :
    message = "success"
else :
    message = "failure"

# 조건부 표현식을 사용하는 경우
message = "success" if score >= 60 else "failure"
