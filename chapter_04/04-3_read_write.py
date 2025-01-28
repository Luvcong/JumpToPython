
# 입출력 - 파일 읽고 쓰기

# 1. 파일 생성 - open
# 파일객체 = open(파일이름, 파일열기모드)
# 프로그램을 실행한 디렉터리에 새로운 파일 생성
f = open("새파일.txt", 'w')
f.close()   # 객체 닫기

# 파일 열기 모드
# r (읽기모드)
# w (쓰기모드)
# a (추가모드) : 파일의 마지막에 새로운 내용을 추가할 때 사용

# 쓰기모드로 여는 경우 해당 파일이 이미 존재할 경우 원래 있던 내용이 모두 사라짐
# 해당 파일이 존재하지 않는 경우 새로운 파일 생성!

# 경로를 지정해서 저장하고 싶은 경우
f = open("D:/study/새파일.txt", 'w')
f.close()
# 쓰기 모드로 열었던 파일 객체를 닫지 않고 다시 사용하려고 하면 오류 발생

# 2. 파일 쓰기
# 쓰기 모드로 파일 열어 내용 작성
f = open("D:/study/JumpToPython/새파일.txt", 'w')
for i in range(1, 11) :
    data = "%d번째 줄입니다\n" % i 
    f.write(data)   # data를 파일 객체 f에 쓰기
f.close()

# 3. 파일 읽기
# 3-1) readline 함수
# 첫번째 줄 읽어서 출력
f = open("D:/study/JumpToPython/새파일.txt", 'r')
line = f.readline()
print(line)
f.close()

# 모든 줄 읽어서 출력
f = open("D:/study/JumpToPython/새파일.txt", 'r')
while True :
    line = f.readline()
    if not line : break     # 더 이상 읽을 줄이 없을 경우 빈 문자열("") return
    print(line)
f.close()
# 한 줄씩 읽어 출력할 때 줄 끝에 \n 문자가 존재 > 빈 줄도 같이 출력

# 3-2) readlines 함수
# 파일의 모든 줄을 읽여서 각각의 줄을 요소로 가지는 리스트를 return
f = open("D:/study/JumpToPython/새파일.txt", 'r')
lines = f.readlines()
print(lines)    # ['1번째 줄입니다\n', '2번째 줄입니다\n', ..., '10번째 줄입니다\n']

# ** strip() : 줄 바꿈 (\n) 문자 제거
for line in lines :
    line = line.strip()
    print(line)
f.close()

# 3-3) read 함수
# 파일의 내용 전체를 문자열로 return 
f = open("D:/study/JumpToPython/새파일.txt", 'r')
data = f.read()
print(data)
f.close()

# 파일 객체 + for문 사용
# 파일 객체는 for문과 함께 사용하면 파일을 줄 단위로 읽을 수 있음
f = open("D:/study/JumpToPython/새파일.txt", 'r')
for line in f :
    print(line)
f.close()

# 4. 파일 수정
# 파일에 새로운 내용 추가
f = open("D:/study/JumpToPython/새파일.txt", 'a')
for i in range(11, 20) :
    data = "%d번째 줄입니다\n" % i
    f.write(data)
f.close()

# 5. with : 파일 객체 열고 닫기
# with문을 사용하면 with block을 벗어나는 순간 열린 파일 객체 f가 자동으로 닫힘
with open("D:/study/JumpToPython/새파일2.txt", 'w') as f :
    f.write("안녕하세용")
