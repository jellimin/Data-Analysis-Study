# 6-4. 간단한 메모장 만들기
# 메모 추가하고 조회 가능한 메모장

# 1. 입력으로 받은 옵션과 메모를 출력하는 코드 작성
# memo.py
import sys

option = sys.argv[1] # sys.argv는 입력된 값을 읽어 들일 수 있는 파이썬 라이브러리, sys.argv[0]이 프로그램 이름임
memo = sys.argv[2]

print(option)
print(memo)

# 2. 다음 명령을 수행
# > python memo.py -a "Life is too short"

# 3. 입력으로 받은 메모를 파일에 쓰도록 코드 변경
# memo.py
import sys

option = sys.argv[1]
if option == "-a":
    memo = sys.argv[2]
    f = open("memo.txt", "a")
    f.write(memo)
    f.write("\n")
    f.close()

# 4. 다음 명령을 수행
# > python memo.py -a "Life is too short"
# > python memo.py -a "You need python"
# 파일에 정상적으로 메모가 기입되었는지 확인하기 위해 > type memo.txt

# 5. 작성한 메모를 출력하는 부분 만들기
# 메모 출력 옵션을 -v로 사용
# memo.py
import sys

option = sys.argv[1]

if option == "-a":
    memo = sys.argv[2]
    f = open("memo.txt", "a")
    f.write(memo)
    f.write("\n")
    f.close()
elif option == "-v":
    f = open("memo.txt")
    memo = f.read()
    f.close()
    print(memo)

# 6. 다음과 같은 명령 수행
# > python memo.py -v



# 6-5. 탭을 4개의 공백으로 바꾸기
# 필요한 기능 : 파일 읽어들이고, 문자열 변경
# 입력값 : 탭을 포함한 문서 파일
# 출력값 : 탭이 공백으로 수정된 문서 파일
# 예를 들어 python tabto4.py scr dst라고 입력한다면
# tabto4.py가 작성해야 할 프로그램 이름, src는 탭을 포함한 원본 파일이름, dst는 변환 결과 저장할 파일 이름

# 1. tabto4.py 파일 작성
# tabto4.py
import sys

src = sys.argv[1]
dst = sys.argv[2]
print(src)
print(dst)

# 2. 입력값이 정상적으로 출력되는지 확인
# > python tabto4.py a.txt b.txt

# 3. 원본파일 a.txt 작성
Life    is    too    short
You    need    python

# 4. 탭 문자를 공백 4개로 변환할 수 있도록 코드 변경
# tabto4.py
import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_content = f.read()
f.close()

space_content = tab_content.replace("\t", " "*4)
print(space_content)

# 5. 다음 명령을 수행
# > python tabto4.py a.txt b.txt
# tab 문자와 공백 문자를 눈으로 구분하여 식별하기 어려움

# 6. 변경된 내용을 b.txt에 저장할 수 있도록 프로그램 변경
# tabto4.py
import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_content = f.read()
f.close()
space_content = tab_content.replace("\t", " "*4)

f = open(dst, "w")
f.write(space_content)
f.close()

# 7. 다음 명령을 수행
# > python tabto4.py a.txt b.txt


# 6-6. 하위 디렉터리 검색하기
# 특정 디렉터리부터 시작해서 그 하위 모든 파일 중 파이썬 파일만 출력해주는 프로그램 만들기

# 1. sub_dir_search.py 파일을 작성
# sub_dir_search.py
# search 함수를 만들고 시작 디렉터리를 입력받도록 코드 작성
def search(dirname):
    print(dirname)

# 2. 이 디렉터리에 있는 파일을 검색할 수 있도록 소스를 변경
# sub_dir_search.py
# 해당 코드를 실행하면 C:/ 디렉터리에 있는 파일이 출력됨
import os

def search(dirname):
    filenames = os.listdir(dirname) # os.listdir은 해당 디렉터리에 있는 모든 파일의 리스트를 구할 수 있음
    for filename in filenames:
        full_filename = os.path.join(dirname, filename) # os.path.join을 이용해 경로와 파일이름을 이어줌
        print(full_filename)

search("C:/")

# 3. C:/ 디렉터리에 있는 파일들 중 확장자가 .py인 파일만을 출력하도록 함
# sub_dir_search.py
import os 

def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        ext = os.path.splitext(full_filename)[-1] # os.path.splitext는 확장자를 기준으로 파일 이름을 두 부분으로 나눠줌
        if ext == ".py":
            print(full_filename)

search("C:/")

# 4. 우리가 최종으로 원하는 것은 C:/ 디렉터리 밑의 .py만이 아니라 하위 디렉터리도 검색
import os

def search(dirname):
    try: # try ~ except로 감싼 이유는 os.listfir를 수행할 때 권한이 없는 디렉터리에 접근하더라도 오류 패스 위해
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename): # os.path.isdir은 파일이 디렉터리인지 아닌지 구분
                search(full_filename) # 해당 경로를 입력으로 받고, search 함수 사용 (재귀호출)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == ".py":
                    print(full_filename)
    except PermissionError:
        pass

search("C:/")

# 하위 디렉터리 검색을 쉽게 해주는 os.walk
# os.walk는 시작 디렉터리부터 하위 디렉터리를 차례대로 방문하게 해주는 함수
# 디렉터리와 파일을 검색하는 일반적인 경우에 os.walk를 사용하는 것을 추천
import os

for (path, dir, files) in os.walk("C:/"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext = ".py":
            print("%s/%s" %(path, filename))
