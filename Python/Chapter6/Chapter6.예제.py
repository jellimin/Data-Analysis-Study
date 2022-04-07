# 6-1. 내가 프로그램을 만들 수 있을까 ?

# 2단 만들기
# for문 이용
from re import I


def gugu(dan):
    result = []
    for i in range(1, 10):
        result.append(dan*i)
    return result

# while문 이용
def gugu(dan):
    result = []
    i = 1
    while len(result) < 9:
        result.append(dan*i)
        i += 1
    return result


# 6-2. 3과 5의 배수 합하기
# 10 미만의 자연수에서 3과 5의 배수를 구하면 3, 5, 6, 9이다. 이들의 총합은 23이다.
# 1000 미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하라.
sum = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
    
print(sum)

# 6-3. 게시판 페이징하기
def getTotalPage(gun, onepage):
    if gun % onepage != 0:
        return gun // onepage + 1
    else:
        return gun // onepage
