# 4-1. 함수
# 입력 또는 출력이 없을 수 있음

def sum(a, b): # 매개변수(입력값)
    result = a + b
    return result # 출력값

print(sum(1, 2)) # 함수를 정의하고 호출까지 해야 함

# 매개변수는 함수에 입력으로 전달된 값을 받는 변수
# 인수는 함수를 호출할 때 전달하는 입력값

# 입력값이 없는 경우
def say():
    return 'Hi'

print(say())

# 출력값이 없는 경우
def sum(a, b):
    print("%d, %d의 합은 %d입니다." %(a, b, a+b))

sum(1, 2)
print(sum(1, 2)) # 출력값이 없어서 None이 출력됨

mylist = [1, 2, 3]
print(mylist.append(4)) # append 함수도 출력값이 없는 함수
print(mylist.pop()) # pop 함수는 출력값이 있는 함수

# 입력값도, 출력값도 없는 경우
def say():
    print('Hi')
say()
print(say())

# 매개변수 지정하여 호출하기
def add(a, b):
    return a+b

result = add(a=3, b=5)
print(result)

result = add(b=5, a=3) # 매개변수를 지정하여 호출하면 순서에 상관없이 사용가능
print(result)

# 여러 개의 입력값 (*args => args가 튜플로 사용됨)
def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum
print(sum_many(1,2,3))

# 매개변수로 *args가 아닌 다른 것도 함께 사용
def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

print(add_mul("add", 1,2,3,4,5,6))
print(add_mul("mul", 1,2,3,4,5,6))

# 키워드 파라미터 (kwargs가 딕셔너리로 출력됨)
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name="foo", age=3)

def print_kwargs(**kwargs):
    for k in kwargs.keys():
        if k == "name":
            print("당신의 이름은 : " + kwargs[k])

print_kwargs(name = "int 조수", b="2")

# 함수의 결과값은 언제나 하나이다 (여러 개라도 튜플 형태로 묶여서 나옴)
def sum_and_mul(a,b):
    return a+b, a*b

print(sum_and_mul(1,2))
print(sum_and_mul(1,2)[0]) # 결과값이 튜플로 나와서 원하는 값만 골라서 사용 가능
result1, result2 = sum_and_mul(1,2) # 각자 출력 가능
print(result1)
print(result2)

# 함수는 return을 만나자마자 결과값을 돌려준 다음 빠져나가므로 return을 두번 쓰는 건 어리석음
def sum_and_mul(a,b):
    return a+b # 여기서 함수를 빠져나오므로
    return a*b # 이 줄은 무시됨

# 특별한 상황일 때 함수를 빠져나가고 싶다면? (자주 사용)
def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s입니다." %nick)

say_nick("안녕")

# 매개변수에 초깃값 미리 설정하기
def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." %name)
    print("나이는 %d살입니다." %old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("줄리", 23)
say_myself("안나", 22, False) # 초깃값을 바꿀 수 있음

# 초기값을 미리 설정하고 싶은 매개변수를 맨 끝에 놓아야지 maping이 쉬움
def say_myself(name, old, man = True):
    print("나의 이름은 %s 입니다." %name)
    print("나이는 %d살입니다." %old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
# say_myself("줄리", 23) # 이렇게 하면 오류남, 컴퓨터가 maping하기 어렵기 때문


# 함수 안에서 선언한 변수의 효력 범위
# 함수 내에 있는 변수는 함수 내에서만 효력을 발휘
a = 1
def vartest(a):
    a = a + 1

vartest(a) # 함수 내에서 a=2가 됨, 출력값 없음
print(a) # 함수 밖의 변수 a의 값은 1이므로 1이 출력

# 그렇다면 아래 코드는 어떻게 실행될까 ?
# def vartest(a):
#   a = a + 1
# vartest(3) # 함수 내에서 a=4가 됨, 출력값 없음
# print(a) # 오류남, a 변수를 찾아볼 수 없으므로 !

# 함수 안에서 함수 밖의 변수를 변경하는 방법
# 1. return 사용하기
a = 1
def vartest(a):
    a = a + 1
    return(a)

a = vartest(a)
print(a)

# 2. global 명령어 사용하기
# 함수는 독립적인 것이 좋으므로 가급적 사용하지 말 것

# lambda (함수를 생성할 때 사용하는 예약어, 축약해서 함수 생성)
def add(a, b):
    return a+b

add = lambda a, b: a+b # 함수이름 = lambda 매개변수 : return
print(add(100, 200))

# lambda 함수를 이런 식으로 자주 사용
myList = [lambda a, b: a+b, lambda a,b : a*b] # 리스트 내에 함수이름이 없는 함수를 2개 선언
print(myList[0](100,500)) # lambda로 만든 함수는 return 명령어가 없어도 결과값을 돌려줌



# 4-2. 사용자 입력과 출력

# input 함수
# input은 내장함수
# def 이용해서 정의한 것은 사용자 정의 함수
a = input() # input으로 입력되는 모든 것은 문자열 취급

# 프롬프트 값을 띄워서 사용자 입력 받기
number = input("숫자를 입력하세요 : ")

# print문
a = 123
print(a)

a = "python"
print(a)

a = [1, 2, 3]
print(a)

# 큰따옴표로 둘러싸인 문자열은 + 연산과 동일
print("Life" "is" "short")
print("Life"+"is"+"short") # 동일한 결과값 출력

# 문자열 띄어쓰기는 콤마로 한다
print("Life","is","short")

# 한 줄에 결과값 출력하기
for i in range(11):
    print(i, end = " ")
    print(" ")




# 4-3. 파일 읽고 쓰기

# 파일 생성하기
# 파일열기모드 : r(읽기모드), w(쓰기모드), a(추가모드)
f = open("새파일.txt", "w") # f는 파일 객체
f.close()

# 나혼자코딩
# f = open("C:/doit/복습.txt", "w")
# f.close()

# 파일을 쓰기 모드로 열어 출력값 적기
f = open("C:/Python/새파일.txt", "w", encoding = "UTF-8") # 마지막 옵션은 한글이 깨지지 않도록 함
for i in range(1, 11):
    data = "%d번째 줄입니다. \n" %i
    f.write(data)
f.close()

# 프로그램의 외부에 저장된 파일을 읽는 여러 가지 방법
# 1. readline 함수 사용하기
f = open("C:/Python/새파일.txt", "r", encoding = "UTF-8")
line = f.readline() # 첫번째 줄만 출력해주는 함수
print(line)
f.close()

# 모든 줄을 다 출력하고 싶은 경우
f = open("C:/Python/새파일.txt", "r", encoding = "UTF-8")
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

# 2. readlines 함수 사용하기
f = open("C:/Python/새파일.txt", "r", encoding = "UTF-8")
lines = f.readlines() # lines가 리스트 형태로 되어있음
for line in lines:
    print(line, end = "") # end = ""은 띄어쓰기를 막겠다 !
f.close()

# 3. read 함수 사용하기
# readlines는 리스트 형태로 불러와지지만
# read는 데이터가 통째로 불러와짐
f = open("C:/Python/새파일.txt", "r", encoding = "UTF-8")
data = f.read()
print(data)
f.close()

# 따라서
# readline을 사용할 때는 while문 이용해서 다 출력
# readlines을 사용할 때는 리스트이므로 for문 이용해서 다 출력
# read를 사용할 때는 한 번에 데이터가 출력됨

# 파일에 새로운 내용 추가하기
# 파일 열기 모드의 w는 새로 파일을 만들어서 적는 것
# 파일 열기 모드의 a는 기존의 파일에 추가해서 적는 것
f = open("C:/Python/새파일.txt", "a", encoding = "UTF-8")
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()

# 함수를 close를 하지 않는 방법
# with문과 함께 사용하기
with open("C:/Python/foo.txt", "w", encoding = "UTF-8") as f:
    f.write("Life is too short, you need python")

    

# 연습문제

# 1번
# 주어진 자연수가 홀수인지 짝수인지 판별해주는 함수(is_odd)를 작성해보자.
def is_odd(number):
    if number % 2 == 0:
        return("짝수")
    else:
        return("홀수")

# 2번
# 입력으로 들어오는 모든 수의 평균 값을 계산해주는 함수를 작성해보자. (단 입력으로 들어오는 수의 개수는 정해져 있지 않다.)
def sum_mean(*args):
    sum = 0
    for i in args:
        sum = sum + i
    print(sum / len(args))

sum_mean(1,2,3,4,5)
sum_mean(1,2)

# 3번
# 다음은 두 개의 숫자를 입력받아 더하여 돌려주는 프로그램이다.
# 다음 프로그램을 수정하시오.
input1 = int(input("첫번째 숫자를 입력하세요 :"))
input2 = int(input("두번째 숫자를 입력하세요 :"))

total = input1 + input2
print("두 수의 합은 %s입니다." %total)

# 4번
# 3이 결과가 다름. 왜냐하면 print()에서 ,는 띄어쓰기 역할을 하기 때문이다. 

# 5번
# 함수를 닫아주지 않았기 때문이다.
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", "r")
print(f2.read())

# 6번
user_input = input("저장할 내용을 입력하세요 :")
f = open('test.txt', 'a', encoding = "UTF-8")
f.write(user_input)
f.write("\n")
f.close()

# 7번
f1 = open("test.txt", "w")
f1.write("Life is too short \nyou need java")
f1.close()

f = open('test.txt', 'r')
body = f.read()
f.close()

body = body.replace("java", "python")

f = open('test.txt', 'w')
f.write(body)
f.close()
