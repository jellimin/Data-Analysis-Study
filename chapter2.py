### 숫자형

## 숫자형 만들기
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

## 사칙연산
a = 3
b = 4
print(a*b) # + , * , / , //(몫) , %(나머지), **(제곱)


### 문자열 자료형

## 문자열 자료형 만들기
a = "Hello world" # 큰따옴표, 작은따옴표, 큰3, 작은3
print(type(a)) # type이 str(문자형)

## 백슬래쉬(\) 사용
# a = 'Python's favorite food is perl # 오류
a = 'Python\'s favorite food is perl' # 정상실행 ?
print(a)

## 이스케이프 코드 줄바꿈 \n 사용
a = "Life is too short \n You need python"
print(a)

## 이스케이프 코드 탭 \t 사용
a = "Hi, \t My name is MY"
print(a)

## 큰3, 작은3의 장점은 이스케이프 문자를 안 써도 됨
a = """"hi 
my name is my   hihi"""
print(a)

## 문자열 더하기
a = "Python"
b = "is fun !"
print(a+b)

## 문자열 곱하기
print(a* 100) # python을 100번 출력

## 문자열 인덱싱 (앞은 0부터, 뒤는 1부터)
a = "Life is too short, You need python"
print(a[0]) # L이 나옴
print(a[1]) # i가 나옴
print(a[-1]) # n이 나옴

## 문자열 슬라이싱
a = "Life is too short, You need python"
print(a[0:4]) # 이상, 미만, 간격
a = "20010331Rainy"
print(a[:8])
print(a[8:])
print(a[::2])
print(a[::-2])

## 문자열 포맷팅 (%d 숫자 / %s 문자열 / %f 실수형)
# 더하기 써서 하기 귀찮으니까 쓰는 과정
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
print(a) # 사실상 %s로 다 해주어도 됨 사기 !
a = "%f" % 3.42134234 # 실수형 대입
print(a)
a = "%0.4f" % 3.42134234 # 소수점 자리수 표현
print(a)

