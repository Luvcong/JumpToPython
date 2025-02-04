
# 변수
# C언어나 JAVA의 경우 변수를 만들 때 자료형의 타입을 지정해야함
# But, Python의 경우 변수에 저장된 값을 스스로 판단하여 자료형의 타입을 지정한다.

a = [1, 2, 3]
# [1, 2, 3]의 값을 가지는 리스트 객체가 자동으로 메모리에 생성
# 변수 a는 [1, 2, 3] 리스트가 저장된 메모리의 주소를 가르키게 됨

print(id(a))    # 2286579256448 (변수a의 메모리 주소가 출력됨)

# 예시 - 리스트를 복사할 때
b = a
print(id(a))    # 2286579256448
print(id(b))    # 2286579256448
# a와 b가 동일한 메모리 주소를 갖고 있는 것을 알 수 있음

# 동일 객체가 맞는지 확인
print(a is b )  # True

# a의 1번째 index에 값 변경
a[1] = 4
print(a)    # [1, 4, 3]
print(b)    # [1, 4, 3]
# a를 변경했는데도 b가 동일하게 변경된 것을 확인할 수 있다.
# (동일한 리스트를 가르키고 있기 때문에 변경됨)

# 다른 주소로 객체를 생성하고 싶다면?
# 1. [:] 이용
a = [1, 2, 3]
b = a[:]    # 리스트 전체
print(b)    # [1, 2, 3]
a[1] = 4
print(a)    # [1, 4, 3]

# 2. copy 모듈 이용
from copy import copy
a = [1, 2, 3]
b = copy(a)     # b = a[:] 동일
print(b)

print(b is a)   # False
print(id(b))    # 2358636465792
print(id(a))    # 2358636664576
# 서로 다른 객체를 가르키고 있는 것을 확인할 수 있음

# *** copy() 
# 리스트 자료형의 자체 함수인 copy() 함수를 사용해도
# copy 모듈을 사용하는 것과 동일한 결과를 얻을 수 있다.
a = [1, 2, 3]
b = a.copy()
print(b is a)   # False

# 변수를 만드는 여러가지 방법
# 1) 튜플 변수 사용
a, b = ('python', 'life')
(a, b) = 'python', 'file'
# 위 2개는 동일한 결과를 반환함 - 튜플은 괄호 삭제 가능하기 때문

# 2) 리스트 변수 사용
[a, b] = ['python', 'life']

# 3) 여러 개의 변수에 같은 값 대입
a = b = 'python'

# python에서는 위 방법을 사용하여 두 변수의 값을 쉽게 변경할 수 있다!
a = 3
b = 5 
a, b = b, a
print(a)    # 5
print(b)    # 3
