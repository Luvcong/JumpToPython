
# Q1. 홀수, 짝수 판별
# 주어진 자연수가 홀수인지, 짝수인지 판별하는 함수 작성
# 홀수면 True, 짝수면 False
def is_odd(num) :
    if num % 2 == 0 :
        return True
    else :
        return False

print(is_odd(4))
print(is_odd(3))

# Q2. 모든 입력의 평균 값 구하기
# 입력으로 들어오는 수의 개수는 정해져있지 않음
def avg_numbers(*args) :
    result = 0
    for i in args :
        result += i
    return result / len(args)

print(avg_numbers(1, 2))            # 1.5
print(avg_numbers(1, 2, 3, 4, 5))   # 3.0

# Q3. 프로그램 오류 수정(1)
# 2개의 숫자를 입력 받아 더한 후 return
input1 = input("첫번째 숫자를 입력하세요")
input2 = input("두번째 숫자를 입력하세요")
total = int(input1) + int(input2)
print("두 수의 합은 %s입니다." % total)

# Q4. 출력 결과가 다른 것을 고르세요
print("you" "need" "python")
print("you"+"need"+"python")
print("you", "need", "python")
print("".join(["you", "need", "python"]))
# 쉼표(,)가 있는 경우 띄어쓰기가 출력되기 때문에 3번이 다른 결과를 출력

# Q5. 프로그램 오류 수정(2)
# 파일(test.txt)에 "Life is too short" 문자열을 저장한 후 다시 파일을 읽어 출력하는 코드 작성
# 1)
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()
print(open("test.txt", 'r').readlines())

# 2)
with open("test.txt", 'w') as f :
    f.write("Life is too short")
print(open("test.txt", 'r').readlines())

# Q6. 사용자 입력 저장하기
# 사용자의 입력을 test.txt에 저장하는 코드 작성
# 프로그램을 다시 실행하더라도 기존에 작성한 내용은 유지하고, 새로 입력한 내용을 추가
user_input = input("저장할 내용을 입력하세요")
f = open("test.txt", 'a')
f.write(user_input)
f.write("\n")
f.close()

# Q7. 파일의 문자열 바꾸기
# 파일 내용 중 "java" 문자열을 "python"로 바꿔서 저장
f = open("test.txt", 'r')
body = f.read()
f.close()

body = body.replace("java", "python")

f = open("test.txt", 'w')
f.write(body)
f.close()

# Q8. 입력값을 모두 더해 출력
# 입력 값을 모두 더하여 출력하는 스크립트를 작성
import sys
sum = 0
numbers = sys.argv[1:]
for num in numbers :
    sum += num
print(sum)

