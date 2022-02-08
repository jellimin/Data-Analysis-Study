# 2장. 파이썬 프로그래밍의 기초, 자료형



# 2-1. 숫자형

# 정수형
a = 1
print(a)
print(type(a)) # type이 int(정수)

# 실수형
a = 1.24
print(a)
print(type(a)) # type이 float(실수)

# 지수형, 실수형의 소수점 표현방식
a = 4.24e10
print(a)
print(type(a)) # type이 float(실수)

# 사칙연산
a = 3
b = 4
print(a*b) # + , * , / , //(몫) , %(나머지), **(제곱)

# 나혼자코딩
a = 14
b = 3
print(a//b)
print(a%b)



# 2-2. 문자열 자료형

# 문자열 자료형 만들기 : 큰따옴표, 작은따옴표, 큰3, 작은3
a = "Hello world" 
print(type(a)) # type이 str(문자형)

# 백슬래쉬(\) 사용
# a = 'Python's favorite food is perl' 오류
a = 'Python\'s favorite food is perl' # ' 앞에 \를 사용하면 문자열 시작과 끝이 아닌 문자열 따옴표임을 나타냄
print(a)

# 이스케이프 코드 줄바꿈 \n 사용
a = "Life is too short \n You need python"
print(a)

# 이스케이프 코드 탭 \t 사용
a = "Hi, \t My name is MY"
print(a)

# 큰3, 작은3의 장점은 이스케이프 문자를 안 써도 됨
a = """"hi 
my name is my   hihi"""
print(a)

b = '''hi
My name is min
young'''
print(b)

# 문자열 더하기
a = "Python"
b = "is fun !"
print(a+b)

# 문자열 곱하기
print(a* 100) # python을 100번 출력

print("=" * 50) # 프로그램 제목 표시할 때 자주 사용
print("my program")
print("=" * 50) 

# 문자열 길이 구하기
a = "Life is too short"
print(len(a))

# 나혼자코딩 
print(len("You need python"))

# 문자열 인덱싱 (앞은 0부터, 뒤는 1부터)
# 파이썬은 0부터 숫자를 센다
a = "Life is too short, You need python"
print(a[0]) # L이 나옴
print(a[1]) # i가 나옴
print(a[-1]) # n이 나옴

# 문자열 슬라이싱
a = "Life is too short, You need python"
print(a[0:4]) # [이상:미만:간격]
a = "20010331Rainy"
print(a[:8])
print(a[8:])
print(a[::2])
print(a[::-2])
print(a[:]) # 처음부터 끝까지 뽑아냄

# pithon을 python으로?
a = "pithon"
print(a[:1] + "y" + a[2:6])

# 문자열 포맷팅 (문자열 안의 특정값을 바꿔야하는 경우)
# %d 숫자 / %s 문자열 / %f 실수형 => 포맷 코드라고 함
a = "I ate %d apples." %3 # 숫자 대입
print(a)
a =  "I was sick for %s days." % "three" # 문자열 대입
print(a)
number = 10 # 변수 이용
a = "I ate %d apples." %number
print(a)
number = 8 # 두 개 이상 넣기
day = "eight"
a = "I ate %d apples. I was sick for %s days." %(number, day)
print(a) 
a = "I ate %s apples. I was sick for %s days." %(3, "eight")
print(a) # 사실상 %s로 다 해주어도 됨 사기 !

# %d 뒤에 %를 쓰고 싶으면 %%를 써야함
a = "Error is %d%%" %90
print(a)

# 포맷코드와 숫자 함께 사용하기
# 1. 정렬과 공백
a = "%10s" %"hi" # 10자리로 하고, 오른쪽 정렬
print(a)
a = "%-10s" %"hi" # 10자리로 하고, 왼쪽 정렬
print(a)
a = "%-10s jane" %"hi" # 10자리로 하고, 왼쪽 정렬하고, 문자열 적기
print(a)
# 2. 소수점 표현하기
a = "%f" % 3.42134234 # 실수형 대입
print(a)
a = "%0.4f" % 3.42134234 # 소수점 자리수 표현
print(a)
a = "%10.4f" %3.42134234 # 자리수는 10자리, 소수점 아래는 4자리
print(a)

# 포맷 함수를 사용한 포매팅
a = "I ate {0} cookies" .format(3) # 숫자 대입
print(a)
a = "I ate {0} apples" .format("five") # 문자열 대입
print(a)
number = 3 # 변수 이용
a = "I ate {0} apples" .format(number) 
print(a)
number = 3 # 2개 이상의 값 넣기
day = "three"
a = "I ate {0} apples. so I was sick for {1} days." .format(number, day)
print(a)
a = "I ate {number} apples. so I was sick for {day} days." .format(number = 10, day = 3) # 인덱스 대신 이름으로 넣기
print(a)

# f 문자열 포매팅 (뒤에 format 함수없이 문자열 앞에 f만 붙이면 됨)
name = "int"
a = f"나의 이름은 {name}입니다"
print(a)

# 문자열 관련 함수

# 1. 문자 개수 세기
a = "hobby"
print(a.count("b")) 

# 2. 문자 위치 알려주기 (인덱스)
print(a.find("b")) 
print(a.find("x")) # 없으면 -1이 나옴

# 3. 문자 위치 알려주기 (인덱스)
print(a.index("b")) 
# print(a.index("x")) # 없으면 에러 발생

# 4. 문자열 삽입
a = ",".join("hihi") 
print(a)
a = ",".join(["a","b","c"]) # 리스트일땐 문자열 기준으로 하나의 스트링으로 만들어줌
print(a)

# 5. 소문자를 대문자로
a = "hi"
print(a.upper())

# 6. 대문자를 소문자로
a = "HI"
print(a.lower()) 

# 7. 공백 지우기
a = "   hi   "
print(a.strip()) 

# 8. 문자열 바꾸기
a = "My name is MINYOUNG"
print(a.replace("MINYOUNG", "YEJI")) 

# 9. 문자열 나누기 
a = "Life is too short"
print(a.split()) # (공백) => 리스트로 바뀜
a = "a:b:c:d"
print(a.split(":")) # (특정 기호) => 리스트로 바뀜



# 2-3. 리스트 자료형

# 리스트 생성
a = [] # a = list()로 비어있는 리스트 생성 가능
b = [1, 2, 3]
c = ["Life", "is", "too", "short"]
d = [1, 2, "Life", "dream"]
e = [1, 2, ["Life", "dream"]] # 리스트 안에 리스트

# 리스트 인덱싱
a = [1, 2, 3]
print(a[0])
print(a[0] + a[2])
print(a[-1])
a = [1, 2, 3, ["a", "b", "c"]]
print(a[0])
print(a[-1])
print(a[3])
print(a[3][0]) # 이중리스트에서 인덱싱
a = [1, 2, ["a", "b", ["Life", "is"]]]
print(a[2][2][0]) # 삼중리스트에서 인덱싱

# 리스트 슬라이싱
a = [1, 2, 3, 4, 5]
print(a[0:3]) # 이상:미만:간격임을 주의
a = [1, 2, 3, ["a", "b", "c"], 4, 5]
print(a[2:5]) # 중첩된 리스트에서 슬라이싱하기
print(a[3][:2])

# 나혼자코딩
A = [1, 2, 3, 4, 5]
print(A[1:3])

# 리스트 연산하기
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b) # 리스트 더하기
print(a * 3) # 리스트 반복하기
print(len(a)) # 리스트 길이 구하기

# 리스트 요소 수정하기
a = ["주소연", "정호수", "이예지"]
a[0] = "공이빈"
print(a)
a[0:2] = ["이예준", "권지하"]
print(a)

# 리스트 요소 삭제하기
a = ["이이연", "이성인", "민지연"]
a[0:2] = [] # 빈 리스트로 교체해 삭제
print(a)
a = ["a", "b", "c"]
del a[1] # del 함수 사용해 삭제
print(a)

# 리스트 관련 함수
# 1. 리스트에 요소 추가
a = [1, 2, 3]
a.append(4)
print(a)
a.append([5, 6]) # 리스트에 리스트 추가
print(a)

# 2. 리스트 정렬
a = [1, 3, 6, 5]
a.sort()
print(a) # 숫자의 경우 오름차순으로 정렬
a = ["한글", "영어", "프랑스어"]
a.sort()
print(a) # 한글의 경우 가나다순
a = ["zebra", "bus", "apple"]
a.sort()
print(a) # 영어의 경우 알파벳순

# 3. 리스트 뒤집기
a = [1, 3, 4, 5]
a.reverse()
print(a)

# 4. 위치 반환
a = [1, 2, 3]
print(a.index(3))
print(a.index(2))

# 5. 리스트에 요소 삽입
# apppend() 함수와는 다르게 insert()는 특정 인덱스에 삽입 가능
a = [1, 2, 5]
a.insert(0, 10) # 0번째 인덱스에 10 삽입
print(a)

# 6. 리스트 요소 제거
# 여러개 있을 때 가장 먼저 있는 값만 사라짐
a = [1, 2, 1, 5]
a.remove(1)
print(a)

# 7. 리스트 요소 끄집어 내기
a = [1, 3, 5]
print(a.pop()) # 마지막 요소인 5를 끄집어냄
print(a) # 5를 제외한 [1, 3]만 남음
a = [1, 3, 5]
print(a.pop(0)) # 0번째 인덱스 값만 끄집어냄
print(a) # 0번째 인덱스 값인 1만 제외하고 [3, 5]만 남음

# 8. 리스트에 포함된 요소 x의 개수 세기
a = [1, 5, 3, 1, 1]
print(a.count(1))

# 9. 리스트 확장 
# extend(x)의 x에는 "리스트"만 올 수 있음
a = [1, 2, 3]
a.extend([4, 5])
print(a)



# 2-4. 튜플
# 리스트는 대괄호, 튜플은 소괄호
# (중요) 리스트는 변경가능, 튜플은 변경불가능( => 고정)
# 튜플은 괄호 생략 무방
# 튜플은 1개의 요소만을 가질 때 뒤에 콤마 필요
t1 = ()
t1 = (1,)
t1 = (1, 2, 3)
t1 = 1, 2, 3
t1 = (1, 2, ("a", "b"))

# 튜플 요소값 삭제 및 변경 시 요류
t1 = (1, 2, 'a', 'b')
# del t1[0] # 삭제 불가능
# t1[0] = 'c' # 변경 불가능

# 튜플 인덱싱
t1 = (1, 2, 'a', 'b')
print(t1[0])

# 튜플 슬라이싱
t1 = (1, 2, 'a', 'b')
print(t1[0:2])

# 튜플 더하기
t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
print(t1 + t2) # 두 튜플을 더해 새로운 튜플을 만든거지 기존의 튜플이 변하는 것은 아니다

# 튜플 곱하기
t1 = (1, 2, 'a', 'b')
print(t1 * 3)

# 나혼자코딩
t1 = (1, 2, 3)
print(t1 + (4,)) # 하나의 요소를 가진 튜플을 만들 때 끝에 콤마 추가


# 2-5. 딕셔너리 (연관배열, 해시)
# 리스트는 일일이 위치를 다 찾아야하지만,
# 딕셔너리는 key를 검색해 그 value을 찾을 수 있음 (key를 통해 value를 얻음)
# 키 : 값의 패턴으로 표현됨
# {key1 : value1, key2 : value2, ...}
# key에는 변하지 않는 값 (ex) 튜플 등
# value에는 변하지 않는 값, 변하는 값 (ex) 튜플, 리스트, 딕셔너리 등

dic = {'name':'pey', 'phone':'0119993233', 'birth':'1118'}
print(dic)

# 딕셔너리 쌍 추가, 삭제하기

# 1. 딕셔너리 쌍 추가하기
a = {1:'a'}
a['name'] = '익명'
print(a)

# 2. 딕셔너리 쌍 삭제하기
a = {'이름':'준수', '번호':'012-123-1532'}
del a['번호'] # key를 입력해서 삭제해줌
print(a)

# 딕셔너리에서 key를 사용해 value 얻기 (리스트에는 인덱스를 넣었는데, 딕셔너리에서는 key를 넣는 것이 핵심이다)
grade = {'jully':90, 'mike':50, 'sam':100}
print(grade['jully'])

# 딕셔너리 만들 때 주의할 사항
a = {1:'a', 1:'b'} # key가 같으면 안됨 (물론 value는 같아도 됨)
print(a) # 중복된 key를 입력할 시 마지막에 입력한 것만 남음

# 딕셔너리 관련 함수

# 1. keys 리스트 만들기
a = {'name':'jelly', 'phone':'012-345-789', 'birth':'1231'}
print(a.keys()) # dict_keys 객체를 돌려줌

# dict_keys 객체 사용법
# dict_keys 객체는 리스트와 차이가 거의 없지만,
# 리스트 고유의 append, insert, sort, remove, pop등 사용 불가
for k in a.keys():
    print(k)

# dict_keys 객체 = > 리스트
print(list(a.keys()))

# 2. value 리스트 만들기
print(a.values()) # dict_vlaues 객체를 돌려줌

# dict_values 사용법
for v in a.values():
    print(v)

# 3. key, value 쌍 얻기
print(a.items()) # key와 value의 쌍을 튜플로 묶은 값을 dict_items 객체를 돌려줌

# dict_items 사용법
for k, v in a.items():
    print("키는 :" + k)
    print("값은 :" + v)

# 4. key, value 쌍 모두 지우기
a.clear()
print(a)

# 5. key로 value 얻기
# 위에서 대괄호로 얻는 방법
a = {'name':'jelly', 'phone':'012-345-789', 'birth':'1231'}
# print(a['grade']) # 대괄호 사용 시 error
# print(a.get('grade')) # get 사용 시 none
# 이를 활용하여 아래와 같이 사용할 수 있음
print(a.get('grade', '없음')) # grade가 없으면 없음을 출력

# 6. 해당 key가 딕셔너리 안에 있는지 조사하기
# get() 함수말고 in 함수 사용 가능
print('grade' in a) # 결과값이 False
print('name' in a) # 결과값이 True

# 나혼자코딩
dict = {'name':'홍길동', 'birth':'1128', 'age':'30'}
print(dict)



# 2-6. 집합 자료형
# 집합은 중복된 요소를 가질 수 없음
# 집합은 순서가 없음 (인덱스로 접근 불가)
# 리스트를 만들어서 set()을 쓰거나,
# 처음부터 {}을 써서 만들거나
# 문자열을 만들어서 set()을 쓰면 됨

# 집합 자료형 만들기
s1 = set([1, 2, 3])
print(s1)
s1 = {1, 2, 3}
print(s1)
s1 = set("hello")
print(s1)
print(type(s1))

# 집합 자료형은 언제 자주 사용할까?
list1 = [1, 2, 3, 2, 3] # 중복된 값을 하나씩만 남기고 싶음
newlist = list(set(list1)) # 하나씩만 남기고, 다시 리스트로
print(newlist)

# 집합 자료형을 인덱싱으로 접근하기 위해서는?
# 집합 자료형은 순서가 없으므로 인덱싱 불가
# 따라서 순서가 있는 리스트나 튜플로 접근
set1 = set([1, 2, 3])
list1 = list(set1)
print(list1[1]) # 리스트 인덱싱
set2 = set([1, 2, 3])
list2 = tuple(set2)
print(list2[2]) # 튜플 인덱싱

# 교집합
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 & s2)
print(s1.intersection(s2))

# 합집합
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 | s2)
print(s1.union(s2))

# 차집합
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 - s2)
print(s1.difference(s2))

# 집합 자료형 관련 함수

# 1. 값 1개 추가하기 
s1 = set([1, 2, 3])
s1.add(4)
print(s1)

# 2. 값 여러 개 추가하기
s1 = set([1, 2, 3])
s1.update([4, 5, 6])
print(s1)

# 3. 특정 값 제거하기
s1 = set([1, 2, 3, 4])
s1.remove(4)
print(s1)



# 2-7. 불 자료형
# 참, 거짓을 불이라고 부름

a = True # True에서 T는 대문자를 써야 함
print(a)
print(type(a))

a = False
print(a)
print(type(a))

# 자료형의 참과 거짓
# 참 : "python" / [1, 2, 3] / (1, 2) / {'이름':'하림'} / 1
# 거짓 : "" / [] / () / {} / 0 / None(아무것도 없는 값)
# 즉, 무언가 있으면 True, 비어있으면 False로 판단

a = "안녕"
if a:
    print(a) # a를 True라고 인식하니까 a가 출력됨

a = ""
if a:
    print(a) # a를 False라고 인식하니까 a가 출력 안됨

a = [1, 2, 3, 4]
while a:
    a.pop() # 마지막 요소를 꺼내버림
    print(a)

# 불 연산 (자료형이 참, 거짓인지 판단)
print(bool("Python"))
print(bool(""))



# 2-8. 자료형의 값을 저장하는 공간, 변수
a = 1
b = "python"
c = [1, 2, 3]

# 리스트를 복사할 때의 방법
a = [1, 2, 3]
b = a # a를 b에 넣으면 a와 b는 완전히 동일함
print(id(a)) # a 변수가 가리키는 메모리의 주소
print(id(b)) # b 변수가 가리키는 메모리의 주소
print(a is b) # a와 b의 주소가 같으면 True로 출력
a[1] = 4
print(b) # 현재 a가 b로 복사된 것이 아님

# 1. [:] 사용
a = [1, 2, 3]
b = a[:] # 슬라이싱을 해서 복사를 할 수 있음, 아까는 메모리의 주소를 할당한 것임
a[1] = 4
print(b)
print(id(a))
print(id(b)) # 두 변수의 메모리의 주소가 아예 다름

# 2. copy 모듈 사용
from copy import copy
a = [1, 2, 3]
b = copy(a)
print(id(a))
print(id(b)) # 두 변수의 메모리의 주소가 아예 다름

# 변수를 만드는 여러 가지 방법
a, b = ("python", "life") # 튜플로 a, b에 값 대입
(a, b) = ("python", "life")
(a, b) = "python", "life"
print(a)
print(b)

[a, b] = ['python', 'life'] # 리스트로 a, b에 값 대입
print(a)
print(b)

a = b = 'hello' # 여러 변수에 같은 값 대입
print(a)
print(b)

a = 3
b = 5
a, b = b, a # 두 변수의 값을 바꿈
print(a)
print(b)

# 나혼자코딩
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b) # False가 출력됨, 서로 다른 메모리이므로 주소가 다름



# p. 112 연습문제

# 1번
a = [80, 75, 55]
print((a[0] + a[1] + a[2]) / 3)

# 2번
a = 13
print(a % 2) # 나머지 계산 이용

# 3번 
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)

# 4번
pin = "881120-1068234"
print(pin[7])

# 5번
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)

# 6번
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

# 7번
a = ['Life', 'is', 'too', 'short']
result = " ".join(a) # " " 기준으로 리스트 a를 스트링으로 만들어줌
print(result)

# 8번
a = (1, 2, 3)
a = a + (4,) # 튜플이 하나의 요소만 가지면 콤마를 붙여주기
print(a)

# 9번
# 3번이 틀림
# key에는 변하지 않는 값만 넣을 수 있는데 리스트를 넣었기 때문이다.

# 10번
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)
print(result)

# 11번
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aset = set(a)
b = list(aset)
print(b)

# 12번
# a, b 둘다 리스트 [1, 2, 3]을 할당했기 때문이다.
a = b = [1, 2, 3]
a[1] = 4
print(b)