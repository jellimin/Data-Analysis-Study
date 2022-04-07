# 지난 시간 배웠던 내용 중 부족했던 부분
# Immutable (변하지 않는 / 정수, 실수, 문자열, 튜플)

a = 1 # a가 정수로 immutable임
def vartest(a):
    a = a + 1
vartest(a)
print(a)

# Mutable (변할 수 있는 / 리스트, 딕셔너리, 집합)

b = [1, 2, 3]
def vartest2(b):
    b = b.append(4)
vartest2(b)
print(b)


# 5-1. 클래스
# 반복되는 변수 & 매서드(함수)를 미리 정해놓은 틀(설계도)

# 클래스는 왜 필요한가?
result = 0
def add(num):
    global result # 이전에 계산한 결괏값 유지 위해 result 전역변수 사용
    result += num
    return result

print(add(3))
print(add(4))

# 두 개의 계산기가 필요하고 각각 계산하고 싶다면 ?
result1 = 0
result2 = 0 # 두 개의 result를 만들어서 각각 계산해야 함

def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7)) # 똑같은 함수인데 여러 번 쓰기 귀찮, 따라서 클래스를 사용 !

# 클래스를 사용한다면 ?
# 즉, add라는 함수를 class를 이용해서 한 번만 정의해놓으면 무한정 찍어낼 수 있음
# 클래스를 쓰는 방법
# 1. class를 입력
# 2. 대문자로 시작하는 클래스의 이름을 작성
# 3. 안에 들어갈 함수와 변수 설정

class Calculator:
    def __init__(self): # __init__ : 처음에 class가 만들어질 때 어떤 값을 설정할 지
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator() # 설계도에서 찍어내어 cal1을 만듦
cal2 = Calculator()

print(cal1.add(3))

print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

# 즉, 클래스는 과자틀이라고 생각 !
# 과자틀(클래스)과 이 틀로 찍어 만든 과자(객체)

# 가장 간단한 클래스 예제
class Cookie:
    pass 

# 해당 클래스는 아무 기능도 갖고 있지 않은 껍질 뿐인 클래스
# 하지만 이런 클래스도 객체 생성 기능이 있음

a = Cookie()
b = Cookie()



# 객체와 인스턴스의 차이
# 객체 : a = Cookie()에서 a는 객체임
# 인스턴스 : a 객체는 Cookie의 인스턴스, 즉 인스턴스는 특정 객체가 어떤 클래스의 객체인지를 관계 위주로 설명할 때 사용



# 사칙연산 클래스 만들기
class FourCal:
    pass

a = FourCal() # a는 FourCal의 객체
print(a)  # 객체인데 FourCal로 만든 객체 !
print(type(a)) # type은 FourCal 클래스, 즉 a는 FourCal 클래스의 객체

# 객체에 숫자 지정할 수 있게 만들기
class FourCal:
    def setdata(self, first, second): # 클래스 안에 구현된 함수를 메서드라고 부름
        self.first = first
        self.second = second

a = FourCal() # 객체를 a로 지정
a.setdata(1, 2) # setdata 메서드의 첫번째 매개변수 self에는 setdata 메서드를 호출한 객체 a가 자동으로 전달
print(a.first)
print(a.second)

# 메서드의 또 다른 호출 방법
# 잘 사용하지는 않지만 알아놓기
# 객체를 생성한 후 클래스이름.메서드이름으로 호출할 경우 괄호에 객체도 포함해서 호출

a = FourCal()
FourCal.setdata(a, 1, 2)

# 더하기, 빼기, 곱하기, 나누기 기능 만들기
class FourCal:
    def setdata(self, first, second): 
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal()
a.setdata(1, 2)
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())


# 생성자 (Constructor)
# 객체가 생성될 때 자동으로 호출되는 메서드
# 객체에 초깃값을 설정해야 할 필요가 있을 때 setdata와 같은 메서드를 호출하는 것보다
# 생성자를 구현하는 것이 안전한 방법
# 메서드 이름으로 __init__을 사용하면 생성자가 됨

class FourCal:
    def __init__(self, first, second): # 생성자로 인식
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    
# a = FourCal() # 오류발생 (생성자 __init__이 호출되었는데 생성자의 매개변수인 first와 second가 전달되지 않았기 때문)
a = FourCal(3, 4) # first와 second 매개변수에 각각 3, 4가 전달됨
print(a.first)
print(a.second)
print(a.add())

# 클래스의 상속
# 계산기를 이용해서 공학용 계산기를 만들 때를 생각
# 즉, 어떤 클래스를 만들 때 다른 클래스의 기능을 물려받을 수 있게 만드는 것

class FourCal: # 부모클래스
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result

class MoreFourCal(FourCal): # 부모클래스를 괄호 안에 넣어 자식클래스를 만듦
    pass

a = MoreFourCal(4, 2) # 부모가 만든 것을 상속받았기 때문에 그대로 사용 가능
print(a.add())


# FourCal 클래스에 제곱 기능을 추가한 MoreFourCal 클래스 만들기
class FourCal: 
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(3, 4)
print(a.pow())


# 메서드 오버라이딩 (즉, 부모의 메서드를 덮어쓴다)
# 클래스 변형
# 메서드를 오버라이딩하면 부모 클래스의 메서드 대신 오버라이딩한 메서드가 호출됨

# a = FourCal(4, 0)
# print(a.div()) # 오류남, 왜냐하면 0으로 나눌 수 없음, 변형해보자 !

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second): 
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
class SafeFourCal(FourCal): # 나누는 수가 0이면 0을 출력하도록 !
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a = SafeFourCal(4, 0)
print(a.div())


# 클래스 변수 / 클래스 변수와 객체 변수 비교
# 객체변수는 다른 객체들에 영향받지 않고 독립적으로 그 값을 유지 (앞에서 봤던 self.first, self.second)
# 클래스 변수는 클래스 내에서 공통적으로 사용할 변수

class Family:
    lastname = "김" # Family 클래스에 선언한 lastname이 클래스 변수

print(Family.lastname) # 클래스 변수는 [클래스이름.클래스변수]로 사용 가능

a = Family()
b = Family()
print(a.lastname)
print(b.lastname) # 클래스 변수를 객체를 통해서도 사용 가능

Family.lastname = "박" # 클래스 변수 값 변경
print(a.lastname)
print(b.lastname) # 객체의 lastname도 모두 박으로 변경됨, 즉 클래스 변수는 클래스로 만든 모든 객체에 공유된다는 특징을 가짐




# 5-2. 모듈
# 미리 만들어 놓은 .py 파일 (함수, 변수, 클래스)
# 현재 파일과 모듈이 같은 경로에 있어야 함

import mod1 # 이 때 현재 파일과 mod1.py는 동일 위치에 있어야 함
print(mod1.add(1, 2))

from mod1 import add # mod1에 많은 함수 중 add만 가져오고 싶을 때
print(add(1, 2)) # add를 바로 사용 가능

from mod1 import add, sub # 여러 함수를 불러오고 싶은 경우
print(sub(1, 2))

from mod1 import * # 모든 함수를 불러오고 싶을 때

# if __name__ = "__main__": 의 의미
import mod1 as mod1 # if __name__ = "__main__"이 거짓이 되어 출력되지 않음 (mod1에서 실행하면 __name__ 변수에는 __main__ 값이 저장되지만, chapter5에서 import 할 경우에는 __name__ 변수에는 모듈 이름 값인 mod1이 저장됨)


# 클래스나 변수 등을 포함한 모듈
import mod2
print(mod2.PI) # PI 변수의 값을 출력

a = mod2.Math()
print(a.solv(2)) # Math 클래스 사용

print(mod2.add(1, 2)) # add 함수도 당연히 사용 가능
print(mod2.add(mod2.PI, 4.4))

# 나혼자코딩
from mod2 import Math
a = Math()
print(a.solv(5))


# 다른 파일에서 모듈 불러오기
# 모듈이 정상적으로 실행되기 위해서는 현재 파일과 모듈이 같은 경로에 저장되어 있어야 함
# 만약 현재 파일과 mod2.py(모듈)이 다른 경로(doit 내의 mymod)에 있다면 ?

# 1. sys.path.append(모듈을 저장한 디렉터리) 사용하기
import sys # sys 모듈을 사용하면 파이썬 라이브러리가 설치되어 있는 디렉토리 확인 가능
sys.path.append("C:/doit/mymod") # 경로를 추가해줘야 불러올 수 있음, subfolder에 있는 거 가져올거야 !
import mod3
print(mod3.add(3, 4))

# 2. PYTHONPATH 환경변수 사용하기
# cmd 켜서 set PYTHONPATH=C:\doit\mymod 입력한 후, 대화형 인터프리터 켜서 위와 똑같이 실행



# 5-3. 패키지
# 패키지는 라이브러리와 비슷한 개념
# 패키지는 모듈 여러 개를 모아놓은 것
# 즉, 패키지는 도트(.)를 사용하여 파이썬 모듈을 계층적으로 관리
# __init__.py 은 패키지 관련 설정하는 곳

# 현재 game 패키지를 만들 것임 ! (doit의 하위폴더로 game을 만듦)

# 패키지에서 모듈 및 함수를 불러오는 다양한 방법들
# 1. echo 모듈을 import하여 실행하는 방법
import game.sound.echo
game.sound.echo.echo_test()

# 2. echo 모듈이 있는 디렉터리까지를 from ~ import하여 실행하는 방법
from game.sound import echo
echo.echo_test()

# 3. echo 모듈의 echo_test 함수를 직접 import하여 실행하는 방법
from game.sound.echo import echo_test
echo_test()

# 4. 3번 방법에서 간단하게 함수 이름을 줄여쓰기
from game.sound.echo import echo_test as e
e()

# 만약 이렇게 사용한다면 ?
# import game
# game.sound.echo.echo_test()
# 오류 발생, import game을 수행하면 game 디렉터리의 모듈 또는 game 디렉터리의 __init__.py에 정의한 것만 참조 가능

# 만약 이렇게 사용한다면 ?
# import game.sound.echo.echo_test
# 오류 발생, 도트를 이용해 import 할 때에 마지막 항목은 모듈 또는 패키지여야 함

# 해당 디렉토리 안에 있는 걸 모두 불러오기 
# '*' 이용
# 하위 버전에서는 해당 코드가 오류 발생
# 따라서, 해당 디렉토리에 __init__.py에 __all__ 변수를 설정하고 import 할 수 있는 모듈을 정의해주어야 함
# 리스트 형태로 가져오고 싶은 모듈을 적어주면 됨

from game.sound import *
echo.echo_test()

# 나혼자코딩
from game.graphic import *
render.render_test()


# relative 패키지
# graphic 디렉토리의 render.py 모듈이 sound 디렉토리의 echo.py 모듈을 사용하고 싶다면?
# 오류해결



# 5-4. 예외 처리
# 오류가 발생했을 때 어떻게 할 지 정하는 것
f = open("없는 파일", "r") # 디렉터리 안에 없는 파일을 열려고 시도하여 오류 발생 (FileNotFoundError)
4 / 0 # ZeroDivisionError 발생
a = [1, 2, 3]
a[4] # a 리스트에서 얻을 수 없는 값 (IndexError 발생)


# 일단 전체적인 순서는 try -> except -> else -> finally

# try, except문 사용
# 기본 형태는 아래와 같다.
# try:
#     ...
# except [발생오류[as 오류 메시지 변수]]: # 대괄호는 생략 가능하다는 의미
#     ...   


# try, except를 사용하는 방법
# 1. try, except만 쓰는 방법
# 오류 종류와 상관없이 오류가 발생하면 except 블록을 수행

# 2. 발생 오류만 포함한 except문
# 오류가 발생할 때 except문에 미리 정해 놓은 오류 이름과 일치할 때만 except 블록을 수행

# 3. 발생 오류와 오류 메시지 변수까지 포함한 except문
# 두 번째 경우에서 오류 메시지의 내용까지 알고 싶을 때 사용함

try:
    4 / 0
except ZeroDivisionError as e:
    print(e) # try, except로 처리하였기 때문에 오류로 인한 프로그램 꺼짐이 발생하지 않음

# 나혼자코딩
try:
    a = [1, 2, 3]
    a[4]
except IndexError as e:
    print(e)


# try, else문 (try에서 오류가 안나면 else를 실행해라)
try:
    f = open("none", "r")
except FileNotFoundError as e:
    print(e)
else:
    data = f.read()
    print(data)
    f.close()


# try, finally문 (finally는 오류 나건 말건 마지막에 실행하는 것)
# 보통 파일을 닫을 때 많이 사용
f = open("foo.txt", "w")
try:
    data = f.read()
    print(data)
except Exception as e: # 어떤 에러가 발생할 지 모르니까 Exception을 써주면 오류가 다 잡힘
    print(e)
finally:
    f.close()


# 여러 개의 오류 처리하기
# 이 때 인덱싱 오류가 먼저 발생했으므로 4 / 0으로부터 발생되는 ZeroDivisionError 오류는 발생하지 않음

try:
    a = [1, 2]
    print(a[3])
    4 / 0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱할 수 없습니다.")

# 2개 이상의 오류를 동시에 처리하는 방법
try:
    a = [1, 2]
    print(a[3])
    4 / 0
except (ZeroDivisionError, IndexError) as e:
    print(e)


# 오류 회피하기 (오류가 발생했을 때 그냥 지나가게 하기)
try:
    f = open('나없는파일', 'r')
except FileNotFoundError:
    pass


# 오류를 일부러 발생시키기 (raise 이용)
# 프로그래머 입장에서 Bird를 쓰게 하고 싶은데 이걸 변형해서 쓰게 하도록 하고 싶을 때 !
class Bird:
    def fly(self):
        raise NotImplementedError # 오류 일부러 발생

class Eagle(Bird): # 메서드 오버라이딩, 자식이 이김 !
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()


# 예외 만들기
# 프로그램 수행 도중 특수한 경우에만 예외처리를 하기 위해서 종종 예외를 만들어서 사용
# 예외는 아래와 같이 파이썬 내장 클래스인 Exception 클래스를 사용하여 만들 수 있음
class MyError(Exception):
    pass

def say_nick(nick):
    if nick == "바보":
        raise MyError()
    print(nick)

say_nick("천사") # 천사가 출력됨
say_nick("바보") # Myerror가 발생

# 예외 처리 기법을 사용하여 MyError 발생을 예외 처리
try:
    say_nick("천사")
    say_nick("바보")
except MyError:
    print("허용되지 않는 별명입니다.")

# 만약 오류메시지를 사용하고 싶다면 ?
try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e) # 오류 메시지가 출력되지 않음, 이를 출력되게 하고 싶다면 __str__ 메서드 구현해야 함

class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."



# 5-5. 내장함수
# 파이썬에 기본적으로 포함하고 있는 함수

# 1. abs (절댓값)
abs(3)
abs(-3)
abs(-1.2)

# 2. all
# 반복 가능한 자료형 x를 입력 인수로 받음
# x가 모두 참이면 True, 하나라도 거짓이 있으면 False를 돌려줌
all([1, 2, 3])
all([1, 2, 3, 0]) # 요소 0이 거짓이므로 False를 돌려줌

# 3. any
# x 중 하나라도 참이 있으면 True를 돌려주고, x가 모두 거짓일 때만 False를 돌려줌
any([1, 2, 3, 0])
any([0, ""])

# 4. chr
# 아스키코드 : 0 ~ 127 사이의 숫자를 각각 하나의 문자 또는 기호에 대응시켜 놓은 것
# chr은 아스키 코드 값을 입력받아 그 코드에 해당하는 문자를 출력
chr(97)
chr(48)

# 5. dir
# 객체가 자체적으로 가지고 있는 변수나 함수를 보여줌
dir([1, 2, 3]) # 리스트가 가진 객체 관련 함수를 보여줌
dir({'1':'a'}) # 딕셔너리가 가진 객체 관련 함수를 보여줌

# 6. divmod(a, b)
# 두 개의 숫자를 입력으로 받고, a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려주는 함수
divmod(3, 2) 
3 // 2
3 % 2

# 7. enumerate (열거하다)
# for문과 함께 자주 사용함
# 순서가 있는 자료형을 입력으로 받아 인덱스 값을 포함하는 객체를 돌려줌
# 즉, 딕셔너리가 for문을 이용해 key와 value를 받는 것처럼
# enumerate를 이용해 인덱스와 값을 받을 수 있음 
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)

# 8. eval
# 실행 가능한 문자열을 입력으로 받아 문자열을 실행한 결괏값을 돌려주는 함수
eval("1+2") # 3이 출력
eval("'hi' + 'a'") # "hia"가 출력
eval("divmod(3, 2)") # (1, 1)이 출력

# 9. filter
# filter 함수의 첫 번째 인수로 함수 이름을, 두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 자료형을 받음
# 두 번째 인수인 반복 가능한 자료형 요소가 함수에 입력되었을 때 반환 값이 참인 것만 묶어 돌려줌

def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result

print(positive([1, -3, 2, 0, -5, 6]))

# 만약 filter 함수를 이용한다면 ?
def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

# lambda를 이용한다면 ? (함수 생성할 때 사용하는 예약어)
# lambda 매개변수 : 리턴값
list(filter(lambda x: x>0, [1, -3, 2, 0, -5, 6]))

# 10. hex
# 정수값을 입력받아 16진수로 변환하여 돌려주는 함수
hex(234)
hex(3)

# 11. id
# 객체를 입력받아 객체 고유 주소 값을 돌려주는 함수
a = 3
b = a
id(3)
id(a)
id(b) # 이 때 3, a, b는 모두 같은 객체를 가리킴, 따라서 주소값이 모두 같음

# 12. input
# 사용자 입력을 받는 함수
# 매개변수로 문자열을 주면 그 문자열은 프롬포트가 됨
a = input()
a
b = input("Enter :")
b

# 13. int
# 문자열 형태나 소수점이 있는 숫자 등을 정수 형태로 돌려주는 함수
# 정수를 입력받으면 그대로 돌려줌
int('3') # 문자열
int(3.4) # 소수점이 있는 숫자

# 14. isinstance(object, class)
# 첫 번째 인수로 인스턴스, 두 번째 인수로 클래스 이름을 받음
# 입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여 참, 거짓을 판단
class Person:
    pass

a = Person()

isinstance(a, Person)
isinstance(b, Person)

# 15. len
# 입력값(문자열, 리스트, 튜플 등 사용)의 길이를 돌려주는 함수 
len("python")
len([1, 2, 3])
len((1, 'a'))

# 16. list
# 반복 가능한 자료형을 입력받아 리스트로 돌려주는 함수
# 입력으로 리스트를 주면 똑같은 리스트를 복사하여 돌려줌
list("python")
list((1, 2, 3))

# 17. map (f, iterable(반복 가능한))
# 첫 번째 인수로 함수, 두 번째 인수로 반복 가능한 자료형을 입력으로 받음
# map은 입력 받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수

# 리스트의 각 요소에 2를 곱하는 함수 만들기 (map 미사용)
def two_times(l):
    result = []
    for i in l:
        result.append(i*2)
    return result

print(two_times([1, 2, 3, 4]))

# map함수를 이용한다면 ?
def two_times(x):
    return x*2

list(map(two_times, [1, 2, 3, 4]))

# lambda를 사용해 간단하게 만들기
list(map(lambda x: x*2, [1, 2, 3, 4]))


# 18. max
# 인수로 반복 가능한 자료형을 입력받아 그 최댓값을 돌려주는 함수
max([1, 2, 3])
max("python")

# 19. min
# max 함수와 반대로, 인수로 반복 가능한 자료형을 입력받아 그 최솟값을 돌려주는 함수
min([1, 2, 3])
min("python")

# 20. oct
# 정수 형태의 숫자를 8진수 문자열로 바꾸어 돌려주는 함수
oct(34)
oct(12345)

# 21. open
# 파일이름과 읽기방법(w, r, a, b)를 입력받아 파일 객체를 돌려주는 함수
# 여기서 b는 바이너리 모드로 파일을 여는데 w, r, a와 함께 사용
f = open("binary_file", "rb")

fread = open("read_mode.txt", "r")
fread2 = open("read_mode.txt") # 읽기 방법의 기본값이 r임, 따라서 두 결과값은 같음

fappend = open("append_mode.txt", "a")

# 22. ord
# 문자의 아스키 코드 값을 돌려줌
# chr과 정반대의 함수
ord('a')
ord('0')

# 23. pow(x, y)
# x의 y 제곱한 결괏값을 돌려주는 함수
pow(2, 4)
pow(3, 3) 

# 24. range
# range([start], stop, [step]) # 이 때 대괄호는 생략해도 되는 부분
list(range(5))
list(range(5, 10))
list(range(1, 10, 2))
list(range(0, -10, -1))

# 25. round
# 숫자를 입력받아 반올림 해주는 함수
round(4.2)
round(4.6)
round(5.678, 2) # 소수점 2자리까지만 반올림하여 표시

# 26. sorted
# 반복가능한 입력값을 받고 그를 정렬한 후 그 결과를 리스트로 돌려주는 함수
sorted([3, 2, 1])
sorted(["a", "c", "b"])
sorted("zero")
sorted((3, 2, 1))

# 27. str
# 문자열 형태로 객체를 변환하여 돌려주는 함수
str(3)
str("hi")
str("hi".upper())

# 28. sum
# 입력받은 리스트나 튜플의 모든 요소의 합을 돌려주는 함수
sum([1, 2, 3])
sum((4, 5, 6))

# 29. tuple
# 반복 가능한 자료형을 입력받아 튜플 형태로 바꾸어 돌려주는 함수
tuple("abc")
tuple([1, 2, 3])
tuple((1, 2, 3))

# 30. type
# 입력값의 자료형이 무엇인지 알려주는 함수
type("abc")
type([])
type(open("test", "w"))

# 31. zip
# 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수
list(zip([1, 2, 3], [4, 5, 6])) # 결과값 [(1, 4), (2, 5), (3, 6)]
list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))
list(zip("abc", "def"))



# 5-6. 라이브러리
# 외장함수는 라이브러리에서 가져다쓰는 함수


# 1. sys
# sys 모듈은 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈

# 명령 행에서 인수 전달하기 - sys.argv
# doit/Mymod 디렉터리에 argv_test.py를 저장
# 내용은 아래와 같음
import sys
print(sys.argv)
# cmd 창에서 python argv_test.py you need python을 입력하면 python 명령어 뒤의 모든 것들이 공백을 기준으로 나뉘어서 sys.argv 리스트의 요소가 됨
# ['argv_test.py', 'you', 'need', 'python']

# 강제로 스크립트 종료하기 - sys.exit
# 이는 ctrl + z나 ctrl + d를 눌러 대화형 인터프리터를 종료하는 것과 같은 기능
sys.exit()

# 자신이 만든 모듈 불러와 사용하기 - sys.path
# 파이썬 모듈들이 저장되어 있는 위치를 나타냄
# 이 때 ''는 현재 디렉터리를 의미함
# sys.path.append("C:/doit/Mymod")를 하면 해당 디렉터리에 있는 파이썬 모듈을 불러와서 사용 가능


# 2. pickle
# 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈
# (1) pickle 모듈의 dump 함수를 사용하여 딕셔너리 객체인 data를 그대로 파일에 저장해보자
import pickle
f = open("test.txt", "wb")
data = {1: 'python', 2:'you need'}
pickle.dump(data, f)
f.close()

# (2) pickle 모듈의 load 함수를 사용하여 원래 있던 딕셔너리 객체 상태 그대로 불러오기
import pickle
f = open("test.txt", "rb")
data = pickle.load(f)
print(data)


# 3. OS
# OS 모듈은 환경 변수나 디렉터리, 파일 등의 OS 자원을 제어할 수 있게 해주는 모듈

# (1) 내 시스템의 환경 변수 값을 알고 싶을 때 - os.environ
# 시스템은 제각기 다른 환경변수 값 가짐
import os
os.environ # 시스템 정보를 돌려주는데, 객체의 타입은 딕셔너리
os.environ['PATH'] # 딕셔너리 타입이므로 다음과 같이 출력 가능, PATH 환경 변수의 내용

# (2) 디렉터리 위치 변경하기 - os.chdir
os.chdir("C:\WINDOWS") # 현재 디렉터리 위치 변경 가능

# (3) 디렉터리 위치 돌려받기 - os.getcwd
# 현재 자신의 디렉터리 위치 돌려줌
os.getcwd()

# (4) 시스템 명령어 호출하기 - os.system
# 시스템 자체의 프로그램이나 기타 명령어를 파이썬에서 호출가능
# os.system("명령어") 형태로 사용
os.system("dir") # 현재 디렉터리에서 시스템 명령어 dir을 실행하는 예

# (5) 실행한 시스템 명령어의 결괏값 돌려받기 - os.popen
# 시스템 명렁어를 실행한 결괏값을 읽기 모드 형태의 파일 객체로 돌려줌
f = os.popen("dir")
print(f.read()) # 읽어들인 파일 객체의 내용을 보기 위함

# 기타 유용한 os 관련함수
# os.mkdir(디렉터리) : 디렉터리를 생성
# os.rmdir(디렉터리) : 디렉터리를 삭제, 단 디렉터리가 비어있어야 삭제 가능
# os.unlink(파일 이름) : 파일을 지움
# os.rename(src, dst) : src라는 이름의 파일을 dst라는 이름으로 바꿈


# 4. shutil
# 파일을 복사해주는 파이썬 모듈
# src라는 이름의 파일을 dst로 복사
# 만약 dst가 디렉터리 이름이라면 해당 디렉터리에 src라는 이름으로 복사됨
import shutil
shutil.copy("src.txt", "dst.txt")


# 5.glob
# 특정 디렉터리에 있는 파일 이름을 모두 알고 싶으 ㄹ때
# 디렉터리에 있는 파일들을 리스트로 만듦
import glob
glob.glob("C:/doit/mark*") # doit 디렉터리에 있는 파일 중 mark로 시작하는 파일을 모두 찾아 읽어들임


# 6. tempfile
# 파일을 임시로 만들어서 사용할 때 유용한 모듈

# (1) tempfile.mkstemp() : 중복되지 않는 임시 파일의 이름을 무작위로 만들어 돌려줌
import tempfile
filename = tempfile.mkstemp()
filename

# (2) tempfile.TemporaryFile() : 임시 저장 공간으로 사용할 파일 객체를 돌려줌
# 이 파일은 기본적으로 바이너리 쓰기 모드를 가짐
import tempfile
f = tempfile.TemporaryFile()
f.close() # 생성한 임시 파일이 자동으로 삭제됨


# 7. time

# (1) time.time
# 현재 시간을 실수 형태로 돌려주는 함수
# 1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간 초
import time
print(time.time()) 

# (2) time.localtime
# time.time()이 돌려준 실수 값을 사용해서 연도, 월, 일, 시, 분, 초의 형태로 바꿔주는 함수
# 튜플 형태로 반환
import time
print(time.localtime(time.time()))

# (3) time.asctime
# time.localtime에 의해서 반환된 튜플 형태의 값을 인수로 받아서 날짜와 시간을 알아보기 쉬운 형태로 돌려주는 함수
import time
print(time.asctime(time.localtime(time.time())))

# (4) time.ctime
# time.asctime(time.localtime(time.time()))을 time.ctime()을 사용해 간편하게 표시
# time.asctime과는 다르게 현재 시간만을 돌려줌
import time
print(time.ctime())

# (5) time.strftime
# 시간에 관계된 것을 세밀하게 표현하는 여러 가지 포맷 코드를 제공
# time.strftime('출력할 형식 포맷 코드', time.localtime(time.time()))
import time
time.strftime("%x", time.localtime(time.time())) # %x는 현재 설정된 지역에 기반한 날짜 출력
time.strftime("%c", time.localtime(time.time())) # %c는 날짜와 시간을 출력
 
# (6) time.sleep
# 주로 루프 안에서 많이 사용
# 이 함수를 사용하면 일정한 시간 간격을 두고 루프 실행 가능
import time
for i in range(5):
    print(i)
    time.sleep(1) # 1초씩 쉬면서 출력해라


# 8. calendar
# 파이썬에서 달력을 볼 수 있게 해주는 모듈
import calendar
print(calendar.calendar(2022)) # 연도를 사용하면 그 해 전체의 달력을 볼 수 있음
print(calendar.prcal(2022)) # 위와 같은 결괏값 얻을 수 있음
print(calendar.prmonth(2022, 10)) # 해당 년도, 달의 달력을 얻을 수 있음
print(calendar.weekday(2022, 10, 2)) # 그 날짜에 해당하는 요일정보 (0 : 월요일, 1 : 화요일, ...)
print(calendar.monthrange(2022, 10)) # 입력받은 달의 1일의 요일, 그 달이 며칠까지 있는지를 튜플 형태로 돌려줌


# 9. random
# 난수를 발생시키는 모듈
import random
random.random() # 0에서 1 사이의 실수 중 난수 값을 돌려줌
random.randint(1, 10) # 1에서 10 사이의 정수 중 난수 값 돌려줌
random.sample(range(100), 2) # 0~99사이에서 2개 뽑아줌
random.choice(range(100)) # 0~99사이에서 아무거나 뽑아줌
a = [1, 2, 3, 4, 5]
random.shuffle(a) # 순서를 무작위로 바꾸어줌
print(a)

# random 모듈을 사용한 응용
# random_pop 함수는 리스트의 요소 중 무작위로 하나를 선택하여 꺼낸 다음 그 값을 돌려줌
import random
def random_pop(data):
    number = random.randint(0, len(data)-1)
    return data.pop(number)

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    while data: print(random_pop(data))

# random_pop함수를 random 모듈의 choice 함수를 사용하여 좀 더 직관적으로 만들 수 있음
def random_pop(data):
    number = random.choice(data)
    data.remove(number)
    return number

# 리스트의 항목을 무작위로 섞고 싶을 때는 random.shuffle 함수를 사용
import random
data = [1, 2, 3, 4, 5]
random.shuffle(data)
data

# 로또 번호 출력하기
import random
lotto = sorted(random.sample(range(1, 46), 6))
print(lotto)

# 5. webbrowser
# 자신의 시스템에서 사용하는 기본 웹 브러우저를 자동으로 실행하는 모듈
import webbrowser
webbrowser.open("http://google.com")



# 연습문제
# 1번
class Calculator:
    def __init__(self):
        self.value = 0
    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)


# 2번
# add 메서드를 오버라이딩
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)

# 3번
# 1. 마지막 요소가 0이므로 False
# 2. 'a'를 문자의 아스키 코드 값으로 돌리고 다시 숫자의 아스키 코드 값으로 돌리므로 True

# 4번
list(filter(lambda x: x>0, [1, -2, 3, -5, 8, -3]))

# 5번
# 10진수로 변경하는 것은 int
int('0xea', 16)

# 6번
list(map(lambda x: x*3, [1, 2, 3, 4]))

# 7번
a = [-8, 2, 7, 5, -3, 5, 0, 1]
min(a) + max(a)

# 8번
round(17/3, 4)

# 9번

# 10번
import os
os.chdir("C:/doit") # 해당 디렉터리로 이동

result = os.popen('dir') # dir 명령을 실행하고, result 변수에 담음

print(result.read()) # 결과 출력

# 11번 
import glob
glob.glob("C:/doit/*.py")

# 12번
import time
time.strtime("%Y/%M/%d %H:%M:%S")

# 13번
import random

result = []
while len(result) < 6:
    num = random.randint(1, 45)
    if num not in result:
        result.append(num)

print(sorted(result))
