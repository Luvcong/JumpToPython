
# 입출력 - 사용자 입출력

# 1. input
# a = input()
# > hello 문장 입력
# print(a)    # hello

# 프롬프트를 이용하여 사용자 입력받기
# input("안내문구")
# number = input("숫자를 입력하세요")
# print(number)

# 주의! input에 입력되는 모든 것은 "문자열"로 취급되기 떄문에
# 숫자로 입력하더라도 문자열로 저장된다
# print(type(number))     # <class 'str'>

# 2. print
# 2-1) 큰따옴표로 둘러쌓인 문자열은 + 연산과 동일!
print("life" "is" "too short")  # lifeistoo short
print("life"+"is"+"too short")  # lifeistoo short

# 2-2) 문자열 띄어쓰기는 쉼표(,)를 사용
print("life", "is", "too short")    # life is too short

# 2-3) 한 줄에 결과 값 출력
for i in range(10) :
    print(i, end=' ')
# end 매개변수의 초기값은 줄바꿈(\n) 문자
