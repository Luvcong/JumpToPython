
# 입출력 - 함수
# 함수란 ?
# 입력 값을 가지고 어떤 일을 수행한 후 그 결과물을 내어놓는 역할
# 반복적으로 사용되는 부분을 기능 단위의 함수로 분리하여 코드를 작성

# 파이썬 함수의 구조
'''
def 함수이름(매개변수) :
    수행할 문장 1
    수행할 문장 2
    ...
'''

# 1. def
# 함수를 만들때 사용하는 예약어

# 2개의 입력 값을 받아서 입력 값의 합계를 return 하는 add 함수 코드 작성
def add(a, b) :
    return a + b

a = 3
b = 5
c = add(a, b)
print(c)

# 2. 매개변수(parameter)와 인수(argument)
# 매개변수(parameter) : 함수에 입력으로 전달된 값을 받는 변수
# 인수(argument)      : 함수를 호출할 때 전달하는 입력 값을 의미
def add(a, b) :     # a, b는 매개 변수수
    return a + b
print(add(3, 4))    # 3, 4는 인수

# 3. 함수의 형태
# 3-1) 일반적인 함수
'''
def 함수이름(매개변수) :
    수행할 문장
    ...
    return 리턴 값
'''
def add(a, b) :
    result = a + b
    return result

# 리턴값을 받을 변수 = 함수이름(인수1, 인수2)
a = add(3, 4)
print(a)

# 3-2) 입력 값이 없는 함수
def say() :
    return "Hi"

# 리턴값을 받을 변수 = 함수이름()
a = say()
print(a)

# 3-3) 리턴 값이 없는 함수
def add(a, b) :
    print("%d, %d의 합은 %d입니다." % (a, b, a + b))

# 함수이름(인수1, 인수2)
add(3, 4)

# 3-4) 입력 값과 리턴 값이 없는 함수
def say() :
    print("Hi")

# 함수이름()
say()

# 4. 매개변수를 지정하여 호출
def sub(a, b) :
    return a - b

result = sub(a = 7, b = 3)  # 4
print(result)

# 매개변수를 지정하여 호출하면 매개변수 순서 상관없이 호출 가능
result = sub(b = 7, a = 3)  # -4
print(result)

# 5. 입력값이 몇개인지 모를때
'''
def 함수이름(*매개변수) :
    수행할 문장
    ...
'''
# 여러 개의 입력 값을 받는 함수 생성
# 1)
def add_many(*args) :
    result = 0
    for i in args :
        result = result + i
    return result

result = add_many(1, 2, 3)
print(result)

result = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)

# 2)
def add_mul(choice, *args) :
    if choice == "add" :
        result = 0
        for i in args :
            result = result + i
    elif choice == "mul" :
        result = 1
        for i in args :
            result = result * i
    return result

result = add_mul('add', 1, 2, 3, 4, 5)
print(result)   # 15
result = add_mul('mul', 1, 2, 3, 4, 5)
print(result)   # 120

# 6. kwargs : 키워드 매개변수
# 키워드 매개변수를 사용할 때는 매개변수 앞에 별 2개(**)를 붙여서 사용
def print_kwargs(**kwargs) :
    print(kwargs)

print(print_kwargs(a = 1))  # {'a': 1}
print(print_kwargs(name='foo', age=3))  # {'name': 'foo', 'age': 3}
# 매개변수 앞에 ** 를 붙이면 매개변수 kwargs는 딕셔너리가 되고,
# 모든 Key=Value 형태의 입력 값이 해당 딕셔너리에 저장된다.

# 7. 함수의 리턴 값
def add_and_mul(a, b) :
    return a + b, a * b
# 함수의 return 값은 언제나 1개만 가능하지만, 위 함수는 오류가 발생하지 않는다
# 위와 같은 함수는 튜플 형태로 1개의 값을 return하기 떄문
result = add_and_mul(3, 4)
print(result)   # (7, 12)

# 하나의 튜플 값을 2개의 값으로 분리하여 받고 싶은 경우
result1, result2 = add_and_mul(3, 4)
print(result1, result2)     # 7 12

# 8. 리턴의 다른 활용법 - 빠져나가기
def say_nick(nick) :
    if nick == "바보" :
        return
    print("나의 별명은 %s 입니다." % nick)

say_nick("바보")    # 함수의 조건식을 빠져나감
say_nick("공주")

# 9. 매개변수에 초기값 설정
def say_myself(name, age, man=True) :
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살 입니다." % age)
    if man :
        print("남자입니다")
    else :
        print("여자입니다")

say_myself("공주", 3, False)
say_myself("호빵", 3)   # man의 입력 값을 넘겨주지 않아도 초기값 Ture로 인식
# 주의! 초기값을 설정하려는 매개변수는 항상 뒤쪽에 위치 해야함

# 10. 함수와 변수의 범위
a = 1   # 함수 밖에서 a 변수 선언
def vartest(a) :
    a = a + 1

vartest(a)
print(a)    # 1 출력
# vartest(a)에서 입력 값을 전달 받는 매개변수 a는
# 함수 안에서만 사용하는 변수일뿐, 함수 밖의 변수 a와는 상관 없다

# 함수 밖의 a 변수의 갑을 변경시키는 방법
# 10-1) return 사용
a = 1
def vartest(a) :
    a = a + 1
    return a

a = vartest(a)
print(a)    # 2
# 한수 밖의 a 변수와는 상관 없지만, return을 통해 값을 전달 받아 2를 출력

# 10-2) global 사용
a = 1
def vartest() :
    global a    # 함수 밖에 선언된 a변수를 직접 사용
    a = a + 1

vartest()
print(a)    # 2
# 함수는 독립적으로 존재하는 것이 좋기 때문에 실제 사용은 권장하지 않음

# 10-3) lambda 사용
# 함수 생성 예약어로 def와 동일한 역할 / 간결한 표현이 가능
# [함수이름 = lambda 매개변수1, 매개변수2, .... : 매개변수를 이용한 표현식]
add = lambda a, b : a + b
result = add(3, 4)
print(result)
# lambda를 이용하여 만든 함수는 return 명령어가 없어도 결과 값을 return