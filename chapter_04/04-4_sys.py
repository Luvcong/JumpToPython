import sys

# 입출력 - sys
args = sys.argv[1:]
for i in args :
    print(i)
# 위 코드가 작성되어 있는 sys1.py 파일을 만들고
# sys1.py aaa bbb ccc 명령문 실행하면 아래와 같이 출력됨
# aaa
# bbb
# ccc

args = sys.argv[1:]
for i in args :
    print(i.upper(), end=' ')
# sys2.py life is too short, you need python
# LIFE IS TOO SHORT, YOU NEED PYTHON