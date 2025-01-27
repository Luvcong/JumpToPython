
# 자료형 - 딕셔너리
# 딕셔너리 = 연관배열(associative array) = 해시(hash)
# 단어 그대로 '사전'이라는 뜻
# 딕셔너리는 리스트나 튜플처럼 순차적으로 요소값을 구하지 않고,
# Key를 통해 Value를 얻는다! -> 딕셔너리의 가장 큰 특징

# 딕셔너리 생성 방법
# {Key1 : Value1, Key2 : Value2, Key3 : Value3 ...}
# └ Key와 Value의 쌍 여러개가 {}로 둘러쌓여 있고, 쉼표로 구분되어 있다.
dic = {'name' : 'peach', 'phone' : '010-1234-1234', 'birth' : '0209'}
a = {1 : "hi"}          # key에 정수값, value에 문자열을 넣은 딕셔너리
a  = {'a' : [1, 2, 3]}  # value에 리스트도 넣을 수 있다.

# 1. 딕셔너리 쌍 추가, 삭제
# 1-1) 딕셔너리 쌍 추가
a = {1 : 'a'}
a[2] = 'b'  # {2 : 'b'} 라는 key:value 추가
print(a)    # {1: 'a', 2: 'b'}

a['name'] = 'peach' # {'name' : 'peach} 라는  key:value 추가가
print(a)            # {1: 'a', 2: 'b', 'name': 'peach'}

a[3] = [1, 2, 3]
print(a)            # {1: 'a', 2: 'b', 'name': 'peach', 3: [1, 2, 3]}

# 1-2) 딕셔너리 쌍 삭제
del a[1]            # a라는 key값을 찾아서 key:value 삭제
print(a)            # {2: 'b', 'name': 'peach', 3: [1, 2, 3]}

# 2. 딕셔너리 사용 예제
# 2-1) key를 사용하여 value 값 확인
grade = {'peach' : 10, 'hoho': 99}
print(grade['peach'])
print(grade['hoho'])

# 리스트나 튜플은 값을 얻기 위해 인덱싱  or 슬라이싱을 사용
# 딕셔너리는 Key를 사용하여 Value 값을 구한다.
# └ 딕셔너리변수이름[Key]
a = {1:'a', 2:'b'}
print(a[1], a[2])   # a의 1, 2번째 요소를 나타내는 것이 아니라 Key에 해당하는 값!

dic = {'name' : 'peach', 'phone' : '010-1234-1234', 'birth' : '0209'}
print(dic['name'])  # peach
print(dic['phone']) # 010-1234-1234
print(dic['birth']) # 0209

# 딕셔너리 생성시 주의할 점!
# 1) Key는 고유한 값이므로 중복되는 Key 값 설정시 1개를 제외한 나머지 요소는 무시된다.
a = {1:'a', 1:'b'}
print(a)    # {1: 'b'} 만 출력 > {1: 'a'} 의 요소가 무시됨

# 2) Key에 리스트 사용 불가 / 튜플은 사용 가능
# 리스트는 값이 변할 수 있기 때문에 Key 값으로 사용 불가
# 튜플은 값이 변할 수 없기 때문에 Key 값으로 사용 가능

# 리스트를 Key에 사용시
# a = {[1, 2] : 'hi'}
# print(a)    # TypeError: unhashable type: 'list' 발생

# 튜플을 Key에 사용시
a = {(1, 2) : 'hi'}
print(a)     # {(1, 2): 'hi'}

# 3. 딕셔너리 관련 함수
# 3-1) keys : key 리스트 생성
a = {'name' : 'peach', 'phone' : '010-1234-1234', 'birth' : '0209'}
print(a.keys()) # dict_keys(['name', 'phone', 'birth']) > a의 Key만을 모아서 dict_keys 객체를 return

# ** python 2.7 까지는 a.keys()를 호출하면 dict_keys가 아닌, 리스트로 반환되었음
# 리스트를 return 하기 위해서는 메모리 낭비가 발생
# > 3.0 이후 버전부터는 메모리 낭비를 줄이기 위해 dict_keys 객체를 리턴하도록 변경됨
# 3.0 이후 버전에서 return 값으로 리스트가 필요한 경우?
# > list(a.keys()) 를 사용하면 된다
print(list(a.keys()))   # ['name', 'phone', 'birth']

# dict_keys 객체 사용 방법
for k in a.keys() :
    print(k)
# 리스트 고유의 append, insert, pop, remove, sort 함수는 사용 불가

# 3-2) values : value 리스트 생성
print(a.values())   # dict_values(['peach', '010-1234-1234', '0209'])

# 3-3) items : key:value 얻기
print(a.items())    # dict_items([('name', 'peach'), ('phone', '010-1234-1234'), ('birth', '0209')])

# 3-4) clear : key:value 삭제
a.clear()
print(a)    # {} 빈 객체 반환

# 3-5) get : key로 value 얻기
# get(x) : x라는 Key에 대응하는 Value를 return
a = {'name' : 'peach', 'phone' : '010-1234-1234', 'birth' : '0209'}
print(a.get('name'))
print(a['name'])        # get과 동일한 결과를 출력

print(a.get('noKey'))   # None 출력
# print(a['noKey'])       # KeyError: 'noKey' 에러 발생

# 딕셔너리 안에 찾으려는 Key가 없는 경우 미리 정해놓은 default 값을 대신 가져오게 할 수도 있다
# get(x, 'default value')
print(a.get('nokey', 'abc'))    # abc

# 3-6) in : 해당 key가 딕셔너리 안에 있는지 찾기
a = {'name' : 'peach', 'phone' : '010-1234-1234', 'birth' : '0209'}
print('name' in a)      # True
print('email' in a)     # False

'''
Q. 다음 표를 딕셔너리로 만드세요 (p.101)
'''
result = {'name' : '홍길동', 'birth' : 1128, 'age' : 30}
print('result : ' , result)
