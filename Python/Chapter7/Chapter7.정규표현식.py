# 7-1. 정규 표현식 살펴보기
# 정규표현식 : 복잡한 문자열을 처리할 때 사용하는 기법, 모든 언어 공통

# 정규표현식을 모른다면 ?
data = """
park 800905-1049118
kim 700905-1059119"""

result = []
for line in data.split("\n"): # 문자열.split 함수 (리스트로 만들어줌)
    word_result = []
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "********"
        word_result.append(word)
    result.append(" ".join(word_result)) # 공백을 하나 두고 나눈 단어 합침
print("\n".join(result))

# 정규표현식을 안다면 ? 
# 훨씬 간편하고 직관적인 코드 작성 가능
# 뒤에서 배우고 다시 돌아오기



# 7-2. 정규 표현식 시작하기

# 정규 표현식의 기초, 메타 문자
# 메타문자 : 원래 그 문자가 가진 뜻이 아닌 특별한 용도로 사용하는 문자


# 1. 문자 클래스 []
# [] 사이의 문자들과 매치
# 즉, [abc]라면 a, b, c 중 한 개의 문자와 매치
# 예를 들어, "before"은 정규식과 일치하는 문자인 "b"가 있으므로 매치
# [] 안의 두 문자 사이에 하이픈(-)을 사용하면 두 문자의 범위를 의미 (ex) [a-c] => [abc], [0-5] => [012345], [a-zA-Z] => 알파벳 모두, [0-9] => 숫자
# 주의해야 할 메타문자인 ^ : not을 의미 (ex) [^0-9] => 숫자가 아닌 문자만 매치

# 자주 사용하는 문자 클래스
# \d : 숫자와 매치, [0-9]와 동일한 표현식
# \D : 숫자가 아닌 것과 매치, [^0-9]와 동일
# \s : whitespace 문자(space나 tab처럼 공백), [\t\n]과 동일
# \S : whitespace 문자가 아닌 것과 매치, [^\t\n]과 동일
# \w : 문자+숫자와 매치, [a-zA-Z0-9] => 문자, 숫자, 언더바
# \W : 문자+숫자가 아닌 문자와 매치, [^a-zA-Z0-9_]


# 2. Dot(.)
# 줄바꿈 문자인 \n을 제외한 모든 문자와 매치됨
# a.b라는 정규식은 "a + 모든문자 + b"라는 의미
# a0b는 가운데 0이 모든 문자를 의미하는 .과 일치하므로 정규식과 매치
# abc는 a와 b 사이에 어떤 문자 하나는 있어야 하는 정규식과 일치하지 않으므로 매치 안됨
# a[.]b는 "a + dot문자 + b"라는 의미, 왜냐하면 문자 클래스 [] 안에 dot가 들어갔으므로 dot 문자 자체를 의미

# 3. 반복(*)
# ca*t의 정규식은 a가 "0"번 이상 반복되면 매치
# 즉, * 앞에 있는 문자의 반복을 의미

# 4. 반복(+)
# 위의 반복 메타문자인 *과는 달리 "1"번 이상 반복되면 매치

# 5. 반복({m, n}, ?)
# 반복횟수를 제한할 수 있음
# {3, 5}라고 하면 3회부터 5회까지만 제한 
# {3,}이라고 하면 3회 이상
# {,3}이라고 하면 3회 이하
# {1,}은 +와 동일하고, {0,}은 *과 동일
# ?는 0회 혹은 1회를 의미, 즉 있거나 없거나 매치, 따라서 {0, 1}과 동일
# {3}은 반드시 3회만 반복



# 파이썬에서 정규 표현식을 지원하는 re 모듈
# 컴파일한 패턴 객체 p를 이용하여 그 이후의 작업 수행 가능
import re
p = re.compile('ab*') # p는 패턴 객체를 의미함

# 정규식을 사용한 문자열 검색
# 컴파일된 패턴 객체는 4가지 메서드를 제공
# match, search, finall, finditer
# match와 search는 정규식과 매치될 때 match 객체를, 매치되지 않을 때 None을 돌려줌

# 1. match() : 문자열의 처음부터 정규식과 매치되는지 조사
import re
p = re.compile('[a-z]+') # a부터 z까지 문자열이 1번 이상 반복되는지에 대한 정규표현식
m = p.match('python') # match 객체를 돌려줌
print(m)
m = p.match('3 python') # 첫 문자열이 3이므로 매치되지 않음, 따라서 None을 돌려줌
print(m)

# 2. search() : 문자열 전체를 검색하여 정규식과 매치되는지 조사
import re
p = re.compile('[a-z]+')
m = p.search('python') # match 객체 돌려줌
print(m)
m = p.search('3 python') # 문자열 전체 검색이므로 match 객체 돌려줌
print(m)

# 3. findall() : 정규식과 매치되는 모든 문자열을 리스트 형태로 돌려줌
import re
p = re.compile('[a-z]+')
result = p.findall('Life is too short') # 리스트 형태
print(result)

# 4. finditer() : 정규식과 매치되는 모든 문자열을 반복 가능한 객체로 돌려줌
import re
p = re.compile('[a-z]+')
result = p.finditer('Life is too short')
print(result) # 반복가능한 객체로 돌려줌
for r in result:
    print(r) # 반복가능한 객체가 포함하는 각각의 요소는 match 객체임


# match 객체의 메서드
# 어떤 문자열이 매치되었는지, 매치된 문자열의 인덱스는 ?
# group, start, end, span

# 1. group() : 매치된 문자열을 돌려줌
# 2. start() : 매치된 문자열의 시작 위치를 돌려줌
# 3. end() : 매치된 문자열의 끝 위치를 돌려줌
# 4. span() : 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 돌려줌

# match 메서드를 사용하였을 때
import re
p = re.compile("[a-z]+") 
m = p.match("python")
print(m.group()) # python을 돌려줌
print(m.start()) # 시작 인덱스인 0을 돌려줌, 항상 0임, 문자열의 시작부터 조사했기 때문
print(m.end()) # 끝 인덱스인 6을 돌려줌
print(m.span()) # 시작, 끝 인덱스를 튜플로 돌려줌

# search 메서드를 사용하였을 때
import re
p = re.compile("[a-z]+")
m = p.search("3 python")
print(m.group()) # python을 돌려줌
print(m.start()) # 시작 인덱스인 2를 돌려줌
print(m.end()) # 끝 인덱스인 8을 돌려줌
print(m.span()) # (2, 8)을 돌려줌

# 모듈 단위로 수행하기 (간결하게 컴파일된 파일 객체로 그 이후 작업 수행)
# origin
import re
p = re.compile("[a-z]+")
m = p.match("python")
# 모듈 단위로 수행
import re
m = re.match("[a-z]+", "python") # 보통 한 번 만든 패턴 객체를 여러 번 사용할 때에는 origin 방법을 많이 사용


# 컴파일 옵션
# 1. DOTALL (약어 S) : dot문자가 줄바꿈 문자를 포함하여 모든 문자와 매치
import re
p = re.compile("a.b", re.DOTALL) 
p = re.compile("a.b", re.S) # 약어 사용
m = p.match("a\nb")
print(m)

# 2. IGNORECASE (약어 I) : 대, 소문자에 관계없이 매치
import re
p = re.compile("[a-z]", re.I)
m = p.match("python")
print(m)
m = p.match("Python") # 대문자로 시작하지만, 컴파일 옵션인 I로 인해 매치됨
print(m)
m = p.match("PYTHON") # 대문자로 시작하지만, 컴파일 옵션인 I로 인해 매치됨
print(m)

# 3. MULTILINE (약어 M) : 여러 줄과 매치 / 메타 문자인 ^(문자열 처음), $(문자열 마지막)와 연관된 옵션
import re
p = re.compile("^python\s\w+") # ^는 문자열 처음, \s는 whitespace, \w는 문자, 숫자, _중 한 문자

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data)) # python이 처음으로 나오는 곳은 python one이므로 python one만 매치됨

p = re.compile("^python\s\w+", re.MULTILINE)
data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data)) # 컴파일 옵션인 MULTILINE 덕분에 각 줄마다 적용됨

# 4. VERBOSE (약어 X) : verbose 모드를 사용
# 긴 정규표현식을 하나씩 뜯어서주석 또는 줄 단위로 구분 가능
import re
charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')
# 이를 컴파일 옵션인 VERBOSE를 사용한다면 ?
import re
charref = re.compile(r"""
&[#]                # start of a numeric entity reference
(
    0[0-7]+         # Octal form
    | [0-9]+        # Decimal form
    | x[0-9a-fA-F]+ # hexadecimal form
)
;
""", re.VERBOSE)

# 백슬래시 문제
# 만약, "\section" 문자열을 찾기 위한 정규식을 만든다고 가정
# 이 때 \section에서 \s는 whitespace로 해석되어 의도대로 매치되지 않음
# 의도대로 매치하고 싶다면 \\section으로 변경해야 함
# p = re.compile('\\section')
# 그러나 파이썬에서 백슬래시 두 개 \\는 백슬러시 하나 \로 인식되므로 결국 \section이 전달되는 것
# 따라서 백슬래시를 4개를 사용해야 함
import re
p = re.compile("\\\\section") # 너무 복잡함
p = re.compile(r"\\section") # 문자열 앞에 r을 붙여주면 raw string이 되어 동일한 의미를 갖게 됨



# 7-3. 강력한 정규 표현식의 세계로
# 1. 메타문자 |
# or과 동일한 의미로 사용됨
import re
p = re.compile("Crow|Servo")
m = p.match("CrowHello")
print(m)

# 2. 메타문자 ^
# 문자열의 맨 처음과 일치함
# 앞에서 살펴본 컴파일 옵션인 MULTILINE을 사용할 경우 각 줄의 처음과 일치
import re
print(re.search("^Life", "Life is too short")) # compile과 search를 한 번에 쓸 수도 있음
print(re.search("^Life", "My Life")) # 문자열의 맨 처음이 Life이 아니므로 None을 돌려냄

# 3. 메타문자 $
# 문자열의 맨 끝을 의미, 즉 메타문자 ^과 반대를 의미
import re
p = re.compile("short$") 
m = p.search("Life is too short")
print(m)
print(re.search("short$", "Life is too short, you need python"))

# 4. 메타문자 \A
# 문자열의 처음과 매치됨
# ^ 메타문자와 동일한 의미이지만, MULTILINE을 사용할 경우 전체 문자열의 처음만 매치됨

# 5. 메타문자 \Z
# 문자열의 끝과 매치됨
# $ 메타문자와 동일한 의미이지만, MULTILINE을 사용할 경우 젠체 문자열의 끝과 매치

# 6. 메타문자 \b
# 단어 구분자 (공백, !, ?, , , . , $ 등)
import re
p = re.compile(r"\bclass\b") # 백슬래시를 쓰므로 raw string을 의미하는 r 사용
print(p.search("no class at all"))
print(p.search("the declassified algorithm"))
print(p.search("one subclass is"))

# 7. 메타문자 \B
# \b 메타 문자와 반대인 경우, 즉 whitespace로 구분된 단어가 아닌 경우에만 매치
import re
p = re.compile(r"\Bclass\B")
print(p.search("no class at all"))
print(p.search("the declassified algorithm"))
print(p.search("one subclass is"))


# 그루핑
# 괄호를 이용해서 어떠한 표현식을 묶어줌
# 즉, 그루핑을 해주는 메타문자는 괄호 ()이다.
import re
p = re.compile("(ABC)+") # 만약 "ABC+"라고 했으면 C만 1번 이상 반복인거임 !
m = p.search("ABCABCABC OK?")
print(m)
print(m.group()) # group()은 매치 객체의 메서드로 매치된 문자열을 돌려줌

import re
p = re.compile(r"\w+\s+\d+[-]\d+[-]\d+") # 그루핑 하지 않은 것
m = p.search("park 010-1234-1234")
print(m.group())

# 이름만 뽑아오고 싶다면 ?
import re
p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+") # 그루핑 한 것
m = p.search("park 010-1234-1234")
print(m.group(1)) # 그루핑 한 첫 번째 것을 불러올 수 있음
# 이 때 group(0)은 매치된 문자열 전체, group(1)은 매치된 문자열 중 첫번째 그룹, ...

# 전화번호를 뽑아오고 싶다면 ?
import re
p = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group(2)) # 그루핑 한 두 번째 것을 불러올 수 있음

# 국번만 뽑아오고 싶다면 ?
import re
p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d)")
m = p.search("park 010-1234-1234")
print(m.group(3)) # 바깥에서 안쪽으로 들어올수록 인덱스 증가

# 그루핑된 문자열 재참조하기 (\1 : 1번째 그룹을 재참조, \2 : 2번째 그룹을 재참조)
# 즉, 한 번 그루핑한 문자열을 재참조할 수 있음을 의미
# 즉, 동일한 단어를 연속적으로 사용해야만 매치가 된다는 것
import re
p = re.compile(r"(\b\w+)\s+\1")
print(p.search("Paris in the the spring").group())

# 그루핑된 문자열에 이름 붙이기 ?P<그룹 이름>
# 정규식 안에 그룹이 무척 많아진다고 하면 그루핑된 문자열의 이름으로 찾는 것이 수월
import re
p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group("name")) # group()의 괄호 안에 그룹 이름을 넣어주면 해당 그룹의 문자열을 돌려낼 수 있음
# 재참조 할 때는 (?P=그룹 이름)이라는 확장 구문 사용
import re
p = re.compile(r"(?P<word>\b\w+)\s+(?P=word)")
print(p.search("Paris in the the spring").group())


# 전방탐색
# 긍정형 전방탐색 (?=...) : ...에 해당하는 정규식과 매치되어야 하며 조건이 통과되어도 문자열이 소비되지 않는다.
# 부정형 전방탐색 (?!...) : ...에 해당하는 정규식과 매치되지 않아야 하며 조건이 통과되어도 문자열이 소비되지 않는다.

# 1. 전방탐색 : 긍정형 (?=)
import re
p = re.compile(".+:") # .은 줄바꿈문자를 제외한 아무 문자, +는 1번 이상 반복
m = p.search("http://google.com")
print(m.group())
# 이 때 :을 검색 조건에는 넣되 출력할 때 없애고 싶다면 ?
import re
p = re.compile(".+(?=:)") # 해당 문자를 괄호로 둘러싼 뒤 문자 앞에 ?=을 넣어줌
m = p.search("http://google/com")
print(m.group())

# 2. 전방탐색 : 부정형 (?!), 긍정형과 달리 등호 대신 느낌표를 사용
import re
p = re.compile(".*[.](?!bat$).*$", re.M) # bat로 끝나는 걸 출력하지마 !
l = p.findall("""
autoexec.exe
autoexec.bat
autoexec.jpg
""")
print(l)

import re
p = re.compile(".*[.](?!bat$|exe$).*$") # bat이나 exe로 끝나는 걸 출력하지마 !
l = p.findall("""
autoexec.exe
autoexec.bat
autoexec.jpg
""")
print(l)

# 문자열 바꾸기 sub
# sub 메서드의 첫 번째 매개변수는 "바꿀 문자열", 두 번째 매개변수는 "대상 문자열"
import re
p = re.compile("(blue|white|red)") # blue나 white나 red가 나오면
print(p.sub("colour", "blue socks and red shoes")) # colour로 바꿔라

# 딱 한 번만 바꾸고 싶은 경우
import re
p = re.compile("(blue|white|red)")
print(p.sub("colour", "blue socks and red shoes", count = 1))

# sub 메서드와 유사한 subn 메서드
# subn 역시 sub와 동일한 기능을 하지만 반환 결과를 튜플로 돌려준다는 차이가 있음
# 돌려준 튜플의 첫 번째 요소는 변경된 문자열, 두 번째 요소는 바꾸기가 발생한 횟수
import re
p = re.compile("(blue|white|red)")
print(p.subn("colour", "blue socks and red shoes"))

# sub 메서드를 사용할 때 참조 구문 사용하기
# 이름 +전화번호 => 전화번호 + 이름
# sub의 바꿀 문자열 부분에 "\g<그룹이름>" 사용
import re
p = re.compile(r"(?P<name>\w+)\s+(?P<phone>\d+[-]\d+[-]\d+)")
print(p.sub("\g<phone> \g<name>", "park 010-1234-1234"))
print(p.sub("\g<2> \g<1>", "park 010-1234-1234")) # 그룹 이름 대신 참조 번호를 사용해도 결과는 동일

# sub 메서드의 매개변수로 함수 넣기
# sub 메서드의 첫 번째 매개변수로 함수를 넣을 수 있음 
# 아래의 hexrepl은 match 객체를 입력으로 받아 16진수로 변환하여 돌려주는 함수
def hexrepl(match):
    value = int(match.group())
    return hex(value)

import re
p = re.compile(r"\d+")
print(p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code'))


# Greedy vs Non-Greedy
# Non-Greedy 사용시 반복하고 싶은 문자 뒤에 ?를 붙여줌
import re
s = "<html><head><title>Title</title>"
print(re.match("<.*>", s).group()) # greedy, < 와 > 사이에 있는 모든 문자 가져옴
print(re.match("<.*?>", s).group()) # non-greedy, < 와 > 가 처음 나타나는 부분만 가져옴
