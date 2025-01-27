
# 자료형 - boolean
# True, False를 나타내는 자료형
# 예약어이기 때문에 첫글자를 항상 대문자로 입력해야 함!

a = True
b = False
# type(x) : x의 타입을 확인하는 python의 내장 함수
print(type(a))  # <class 'bool'>
print(type(b))  # <class 'bool'>

print(1 == 1)   # True
print(2 > 1)    # False
print(2 < 1)    # False

# 문자열, 리스트, 튜플, 딕셔너리 등의 값이 비어 있으면("", [], (), {}) False / 비어있지 않으면 True 반환
# 숫자인 경우 0일때 False / 1일때 True
# None의 경우에도 False 반환

a = [1, 2, 3, 4]
while a :
    print(a.pop())

# 조건식 사용하여 boolean 값 확인
# False 반환
if [] :
    print("True")
else :
    print("False")

# True 반환
if [1, 2, 3] :
    print("True")
else :
    print("False")

print(bool(''))         # False
print(bool([1, 2, 3]))  # True
print(bool([]))         # False
print(bool(0))          # False
print(bool(3))          # True