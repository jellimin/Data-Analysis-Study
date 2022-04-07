# Q1
a = "a:b:c:d"
result1 = a.split(":") # 문자열을 잘라서 리스트 형태로 
print(result1)
result2 = "#".join(result1) # 리스트의 원소를 붙여서 문자열로
print(result2)

# Q2
# key를 통해 value를 얻기 위해서는 두 가지 방법 존재
# a[key명] => 해당 key가 없을 시 오류를 발생
# a.get(key명) => 해당 key가 없을 시 None을 돌려줌
a = {'A':90, 'B':80}
a.get('C', 70) # get 함수를 사용하면 디폴트 값 지정 가능, 지정 안하면 None을 돌려냄

# Q3
a = [1, 2, 3]
print(id(a))
a = a + [4, 5]
print(a)
print(id(a)) # + 기호를 사용하면 주소가 변화하므로 새 리스트가 반환되는 것임

a = [1, 2, 3]
print(id(a))
a.extend([4, 5])
print(a)
print(id(a)) # extend를 사용하면 주소 유지

# Q4
# for문 사용
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum = 0
for i in A:
    if i >= 50:
        sum += i
    
print(sum)


# while문 사용
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum = 0 
while A:
    result = A.pop()
    if result >= 50:
        sum += result
  
print(sum)

# Q5
def fibo(num):
    first = 0
    second = 1
    result = [first, second]
    i = 0
    while True:
        new = result[i] + result[i+1]
        result.append(new)
        i += 1
        if new >= num:
            print(result)
            break
            
fibo(5)

# 답지 풀이
def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n-2) + fib(n-1)

for i in range(10):
    print(fib(i))

# Q6
a = input("숫자를 입력하세요 / 콤마로 구분하여 입력:")
result = a.split(",")
sum = 0 
for i in result:
    sum += int(i)
    
print(sum)

# Q7
dan = int(input("구구단을 출력할 숫자를 입력하세요(2~9) :"))
for i in range(1, 10):
    print(dan*i, end = " ")

# Q8
# readline() : 첫번째 줄만 불러옴
# readlines() : 모든 줄을 불러온 후, 리스트 형태로
# read() : 파일 전체 내용을 문자열로

f = open("abc.txt", "r")
result = f.readlines()
f.close()
f = open("abc.txt", "w")
for i in range(len(result)):
    su = result.pop()
    f.write(su.strip("\n")) # strip은 인자로 전달된 문자를 왼쪽, 오른쪽에서 제거
    f.write("\n")
f.close()
    
# 답지 풀이
f = open("abc.txt", "r")
lines = f.readlines()
f.close()

lines.reverse() # 리스트 역순 정렬

f = open("abc.txt", "w")
for line in lines:
    line = line.strip("\n")
    f.write(line)
    f.write("\n")
f.close()

# Q9
f = open("sample.txt", "r")
result = f.readlines()
sum = 0
f.close()

f = open("result.txt", "w")
sum = 0
for i in result:
    su = int(i.strip())
    sum += su
f.write(str(sum/len(result)))
f.close()

# Q10
class Calculator:
    def __init__(self, list):
        self.list = list
    def sum(self):
        sum = 0
        for i in self.list:
            sum += i
        return sum
    def avg(self):
        total = self.sum()
        return total / len(self.list)
    
cal1 = Calculator([1, 2, 3, 4, 5])
cal2 = Calculator([6, 7, 8, 9, 10])

print(cal1.sum())
print(cal1.avg())
print(cal2.sum())
print(cal2.avg())

# Q11
# 1. sys 모듈 사용
import sys
sys.path.append("c:/doit")
import mymod

# 2. PYTHONPATH 환경변수 사용 (set PYTHONPATH=c:\doit)

# 3. 현재 디렉터리 사용하기 (cd c:\doit)

# Q12
# 7이 출력됨
# 일단 첫 번째 오류가 인덱스 에러이므로, 3번째 예외처리로 이동해 result에 3을 더해준다.
# 최종적으로 finally 구문이 실행되어 result에 4를 더해줘 7이 된다.

# Q13 ★ 틀림 ★
def DashInsert(num):
    numbers = list(map(int, num)) # map(function, iter), 반환은 map 객체이기 때문에 리스트, 튜플 등으로 변환해주어야 함
    result = []
    for i, num in enumerate(numbers):
        result.append(str(num))
        if i < len(numbers)-1:
            is_odd = num % 2 == 1
            is_next_odd = numbers[i+1] % 2 == 1
            if is_odd and is_next_odd:
                result.append("-")
            elif not is_odd and not is_next_odd:
                result.append("*")
    print("".join(result)) 

DashInsert("4546793")

# Q14 ★ 틀림 ★
def press(s):
    _c = ""
    cnt = 0
    result = ""
    for c in s:
        if c != _c:
            _c = c
            if cnt:
                result += str(cnt)
            result += c
            cnt = 1
        else:
            cnt += 1
    if cnt:
        result += str(cnt)
    return result

print(press("aaabbccccca"))  

# Q15 ★ 틀림 ★
# 길이가 10인지 검사
# for문(인덱스) 안에 for문(인덱스 이용해서 같은지 검사)
# num의 예시는 "0123456789"

def dup(num):
    result = []
    for i in num:
        if i not in result:
            result.append(i)
        else:
            return False
    return len(result) == 10

print(dup("0123456789")) 

# Q16 ★ 틀림 ★
dic = {
    '.-':'A', '-...':'B', '-.-.':'C', '-..':'D', '.':'E',
    '..-.':'F', '--.':'G', '....':'H', '..':'I', '.---':'J',
    '-.-':'K', '.-..':'L', '--':'M', '-.':'N', '---':'O',
    '.--.':'P', '--.-':'Q', '.-.':'R', '...':'S', '-':'T',
    '..-':'U', '...-':'V', '.--':'W', '-..-':'X', '-.--':'Y',
    '--..':'Z'}

def morse(mo):
    result = []
    for word in mo.split("  "):
        for char in word.split(" "):
            result.append(dic[char])
        result.append(" ")
    return "".join(result)

print(morse(".... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--"))

# Q17
# 2번
import re

p = re.compile("a[.]{3,}b")
m = p.match("a....b")
print(m)
print(m.group())

# Q18
# 10
import re
p = re.compile("[a-z]+")
m = p.search("5 python")
m.start() + m.end()

# Q19
import re
data = """
park 010-9999-9988
kim 010-1234-4568
lee 010-1234-6958
"""
p = re.compile(r"(\d+[-]\d+[-])(\d+)")
p.sub("\g<1>####", data)

# Q20 ★ 틀림 ★
import re
p = re.compile(".*[@].*[.](?=com$|net$).*$")
m = p.match("m@naver.com")
print(m)
m = p.match("m@naver.net")
print(m)
m = p.match("m@naver.co.kr")
print(m)
