
# 자료형 - 문자형
# 문자열을 만들고 사용하기 위해서는
# 큰 따옴표 / 작음 따옴표 / 큰 따옴표 3개 / 작은 따옴표 3개를 연속으로 사용하여 만들 수 있다.
print('Hello World')
print("Hello World")
print('''Hello World''')
print("""Hello World""")

# 1. 큰 따옴표 안에 작은 따옴표 사용
# food = 'Python's favorite food is perl'   # 오류 발생
food = "Python's favorite food is perl"
print(food)

# 2. 문자열에 큰 따옴표 사용
say = '"Python is very easy". he says.'
print(say)

# 3. 역슬래시를 사용하여 작은/큰 따옴표 문자열 포함
food = 'Python \'s favvorite food is perl'
say = "\"Python is very easy.\". he says"

# 4. 여러 줄 문자열을 변수에 대입시
# 4-1) 역슬래시(\)
# Life is too short
# You need python
multiline = "Life is too short\nYou need python"
# 주의할 점은 \n을 띄어쓰지 않음!

# 4-2) 따옴표 사용(''' / """)
multiline = '''
    Life is too short
    You need python
    '''

multiline = """
    Life is too short
    You need python
    """

# 여러 줄 문장을 작성하는 경우 이스케이프보다 따옴표 사용이 더 가독성이 좋음
# 이스케이프 코드란?
# \n : 줄 바꿈
# \t : 탭 간격
# \\ : 역슬래시(\)를 그대로 표현
# \' : 작은 따옴표를 그대로 표현
# \" : 큰 따옴표를 그대로 포현
# \r : 캐리지 리턴 (줄 바꿈 문자, 커서를 현재 줄의 가장 앞으로 이동
# \f : 폼 피드 (줄 바꿈 문자, 커서를 현재 두르이 다음 줄로 이동)
# \a : 벨소리 (출력할 때 PC스피커에서 '삑' 소리 출력)
# \b : 백스페이스
# \000 : null문자

# ★ 5. 문자열 연산
# 파이썬에서는 문자열을 더하거나 곱할 수 있다! (파이썬만의 특징)
# 5-1) 문자열 더하기
head = "Python"
tail = "is fun"
print(head + tail)

# 5-2) 문자열 곱하기
a = "Python"
print(a * 2)
print("=" * 50)
print("My Program")
print("=" * 50)

# 5-3) 문자열 길이
# len
a = "Life is too short"
print(len(a))

'''
Q. "You need Python"의 문자열을 변수에 대입 후 길이를 구하세요
'''
text = "You need Python"
print(len(text))

# 6. 문자열 인덱싱 / 슬라이싱
# 6-1) 문자열 인덱싱
# 인덱스 숫자는 0부터 시작
a = "Life is too short, You need Python"
print(a[3]) # e

# 위와 같이 특정 값을 뽑아내는 것을 '인덱싱'이라고 함
# a[-0]인 경우?
print(a[-0])    # L : 0과 -0은 동일하기 때문에 [0]과 동일한 값을 출력
print(a[-2])    # o
print(a[-5])    # y
# 마이너스가 붙는 경우 뒤에서부터 인덱싱을 시작하고,
# 뒤에서부터 인덱싱 하는 경우 숫자가 1부터 시작한다.

# 6-2) 문자열 슬라이싱
a = "Life is too short, You need Python"

# 위 문자열에서 Life 만 뽑아내는 방법?
# 1) 인덱싱 활용시
b = a[0] + a[1] + a[2] + a[3]
print(b)    # Life

# 2) 슬라이싱 활용시
# a[시작번호:끝번호] 
print(a[0:4])   # 인덱스 0부터 3까지 문자열을 뽑아내어 출력 (0 <= a < 4)
print(a[19:])   # 19번째 인덱스부터 끝까지 출력
print(a[:17])   # 0부터 16번째 인덱스까지 출력
print(a[:])     # 전체 문자열 출력
print(a[19:-7]) # You need

# 슬라이싱으로 문자열 나누기
a = "20250108Sunny"
year   = a[:4]
day    = a[4:8]
weater = a[8:]
print(year)
print(day)
print(weater)

# Pithon 문자열을 Python 문자열로 바꾸기
a = "Pithon"
# a[1] = "y"
# print(a)
# 오류 발생! 문자열의 요소값은 변경 불가 (슬라이싱 기법을 사용하여 변경)
print(a[0]  + "y" + a[2:])
print(a[:1] + "y" + a[2:])

# 7. 문자열 포매팅
# 7-1) 숫자 포매팅 (%d)
a = "I eat %d apples" % 3
print(a)

# 7-2) 문자열 포매팅 (%s)
a = "I eat %s apples" % "five"
print(a)
# 문자열 대입시에는 따옴표를 사용하는 것 주의

# 7-3) 숫자형 변수 대입
num = 3
print("I eat %d apples" % num)

# 7-4) 2개 이상의 변수 대입
# 2개 이상의 값을 넣으려면 % 괄호 안에 쉼표로 구분하여 각각의 값을 넣어준다.
num = 10
day = "three"
print("I ate %d appels. so I was sick for %s days." % (num, day))

# format 함수 사용하여 2개 이상의 값을 대입할 수 있다
# name=value 같은 형태로 입력 값을 입력하여 표시
print("I ata {number} apples. so I was sick for {day} days.".format(number=10, day=3))

# 7-5) 인덱스와 이름 활용
print("I ata {0} apples. so I was sick for {day} days.".format(10, day=3))

# 8) 정렬
# 왼쪽 정렬
print("{0:<10}".format("hi"))
# 오른쪽 정렬
print("{0:>10}".format("hi"))
# 가운데 정렬
print("{0:^10}".format("hi"))

# 9) 공백 채우기
print("{0:=^10}".format("hi"))
print("{0:!<10}".format("hi"))
print("{0:!^10}".format("hi"))

# 10) 소수점 표현
y = 3.42134234
# 소수점 4자리까지 표시
print("{0:0.4f}".format(y))

# 11) 중괄호 표시
# 중괄호 문자를 포매팅 문자가 아닌, 문자열로 표시하고 싶은 경우 {{}} 2개를 연속으로 사용용
print("{{ and }}".format())

# 12) f 문자열 포매팅
# python 3.6 버전 이후부터 사용할 수 있는 기능
# 문자열 앞에 f 접두사를 붙이면 f문자열 포매팅 기능을 사용할 수 있다
name = "이지은"
age  = 31
print(f'나의 이름은 {name}이고, 나이는 {age}입니다')

# f 문자열 포매팅은 표현식도 지원됨
print(f'나는 내년이면 {age + 1}살이 됩니다')

# f 문자열 포매팅에서 딕셔너리 사용 가능
# 딕셔너리란? key와 value라는 것을 한 쌍으로 가지는 자료형
d = {'name':'이지은', 'age':'31'}
print(f'나의 이름은 {d["name"]}이고, 나이는 {d["age"]}입니다')

# 12-1) f 문자열 포매팅 정렬
print(f'{"hi":<10}')    # 왼쪽 정렬
print(f'{"hi":>10}')    # 오른쪽 정렬
print(f'{"hi":^10}')    # 가운데 정렬

# 12-2) f 문자열 공백 채우기
print(f'{"hi":=^10}')
print(f'{"hi":^10}')

# 12-3) f 문자열 소수점 표현
y = 3.42134234
# 소수점 4자리까지 표시
print(f'{y:0.4f}')
# 소수점 4자리까지 표시 + 총 자리수를 10자리로 표시
print(f'{y:10.4f}')

# 12-4) f 문자열 중괄호 표시
print(f'{{ and }}')

'''
Q. format 함수 or f 문자열 포매팅을 사용하여 !!!python!!! 문자열 출력
'''
print("{0:!^12}".format('python'))
print(f'{"python":!^12}')


# 13) 문자열 내장 함수
# 13-1) count
a = "hobby"
# a 변수에 있는 b의 개수 출력
print(a.count('b'))

# 13-2) find
# b가 처음으로 나온 위치 반환
a = "Python is the best choice"
print(a.find('b'))  # 14
print(a.find('k'))  # -1 : 찾는 문자열이 존재하지 않으면 -1 반환

# 13-3) index
# 찾는 문자열의 위치 반환
# 찾는 문자열이 없다면 오류 발생!! find 함수와의 차이점
a = "Life is too short"
print(a.index('t'))
# print(a.index('k')) # ValueError: substring not found

# 13-4) join
print(",".join('abcd'))
print(",".join(['a', 'b', 'c', 'd']))

# 13-5) upper
# 소문자를 대문자로 변경
a = "hi"
print(a.upper())

# 13-6) lower
# 대문자를 소문자로 변경
a = "HELLO"
print(a.lower())

# 13-7) lstrip
# 왼쪽 공백 삭제
a = " hi  "
print(a.lstrip())

# 13-8) rstrip
# 오른쪽 공백 삭제
a = " hi    "
print(a.rstrip())

# 13-9) strip
# 양쪽 공백 삭제
a = "    hi    "
print(a.strip())

# 13-10) replace
# 문자열 변경 : replace(원본문자열, 변경문자열)
a = "Life is too short"
print(a.replace("Life", "Your leg"))

# 13-11) split
# 문자열 나누기
# 괄호 안에 값을 넣지 않으면 spacebar, tab, enter 등을 기준으로 문자열 분리
# 괄호 안에 값을 넣으면 해당 값을 기준으로 문자열을 분리한다.
# split을 사용하면 분리한 값이 리스트에 담겨서 return
a = "LIfe is too short"
print(a.split())    # 공백을 기준으로 문자열 분리
b = "a:b:c:d"
print(b.split(':')) # : (콜론)을 기준으로 문자열 분리
