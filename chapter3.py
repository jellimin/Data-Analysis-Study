# 3-1. if문 (조건문)
# 들여쓰기가 상당히 중요
# if 뒤에 [불자료형, 비교연산자, and, or, not 등을 사용]해서 
# 결국 [불자료형]이 오게끔
# 조건문 뒤에 콜론(:)을 잊지말자 !

# 불자료형
from re import I


money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")


# 비교연산자
a = 1
b = 2
if a < b:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

# and(&), or(|), not
money = 2000
card = 1
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

money = 2000
card = 1
if not False:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

# in, not in (오른쪽에는 리스트, 튜플, 문자열 같은 자료형이 들어감)
if 1 in [1, 2, 3]:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

if "1" in "123":
    print("택시를 타고 가라")
else:
    print("걸어 가라")

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print('택시를 타고 가라')
else:
    print('걸어 가라')

# 나혼자코딩
pocket = ['cellphone', 'card', 'tint']
if 'card' not in pocket:
    print('걸어 가라')
else:
    print('버스를 타고 가라')

# 조건문에서 아무 일도 하지 않게 설정하고 싶다면?
if 1 in (1, 2, 3):
    pass
else:
    print('없다')

# 조건이 여러 개 일 때 사용하는 elif
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print('택시를 타라')
elif card:
    print('택시를 타라')
else:
    print('걸어 가라')

# 조건부 표현식 : 한줄로 간결하게
# 조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우
# 1. 성공일 때 조건을 먼저 써준다
# 2. 조건식을 써준다
# 3. 실패일 때 조건을 써준다
score = 70
if score >= 60:
    message = "success"
else:
    message = "failure"
print(message)

message = "success" if score >= 60 else "failure"
print(message)

money = True
message = "택시를 타고가라" if money == True else "택시를 타지마"
print(message)



# 3-2. while문 (반복문)

# (Run) break point 걸어주고 debugging 해보기 => 한 줄씩 실행가능
treehit = 0
while treehit < 10:
    treehit = treehit + 1 # treehit += 1
    print("나무를 %d번 찍었습니다." %treehit)
    if treehit == 10:
        print("나무 넘어갑니다.")

prompt = """
1. add
2. del
3. list
4. quit

Enter number : """

number = 0
while number != 4:
    print(prompt)
    number = int(input()) # int(input())은 숫자 입력을 받아들이는 것

# while문 강제로 빠져나가기 (break)
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee4 - 1
    print("남은 커피의 양은 %d개입니다." %coffee)
    if not coffee:
        print("커피가 다 떨어졌습니다. 판매를 중단합니다.")
        break # break가 없으면 money가 남아있으니 무한반복됨

# 조건문이 돌아가는 순서 잘 살펴보기
coffee = 10
while True:
    money = int(input("돈을 넣어주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." %(money - 300))
        coffee -= 1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개입니다" %coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

# while문의 맨 처음으로 돌아가기 (continue)
a = 0
while a < 10:
    a = a+1
    if a % 2 == 0:
        continue
    print(a)

# 나혼자코딩
a = 0
while a < 10:
    a = a+1
    if a % 3 == 0:
        continue
    print(a)

# 무한루프 (ctrl + c를 눌러야 중지)
while True:
    print("안녕하세요")


