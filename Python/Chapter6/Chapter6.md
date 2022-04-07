# **Chapter6-1. 내가 프로그램을 만들 수 있을까?**

## **구구단 결과값 출력하는 함수 만들기**
<br>

1. for문 사용하기
   
```python
def gugu(dan):
    result = []
    for i in range(1, 10):
        result.append(dan*i)
    return result
>>> print(gugu(2)) 
[2, 4, 6, 8, 10, 12, 14, 16, 18]
```

for문을 사용하여 구구단 결과값을 출력하는 함수인 gugu를 만들기 위해 매개변수 dan에 구구단의 단을 입력받는다. 그리고 결과값을 리스트로 출력하기 위해 빈 리스트인 result를 생성한 후, for문을 이용해 단에 곱할 수인 1 ~ 9까지를 반복 출력할 수 있도록 한다. for문 내에는 리스트 함수인 append를 이용해 원소를 추가한다. 2단을 출력해보면 구구단 결과값이 리스트에 담긴 것을 확인해볼 수 있다.

2. while문 사용하기

```python
def gugu(dan):
    result = []
    i = 0
    while len(result) < 9:
        i += 1
        result.append(dan*i)
    return(result)
>>> print(gugu(2)) 
[2, 4, 6, 8, 10, 12, 14, 16, 18]
```

while문을 사용하는 것도 for문과 비슷하다. 차이점은 해당 조건이 만족할 때까지 반복문을 돌리는 것인데 이 때 리스트 result의 길이가 9보다 작을 때까지 반복하면 된다. (왜냐하면 빈 리스트의 길이는 0이므로 0부터 시작하기 때문이다.) for문과 달리 반복 가능 자료형에서 요소를 빼와 변수에 저장하는 것이 아니기 때문에 반복문을 돌 때마다 그 값을 늘려주는 i 변수를 설정해주면 된다.

___

# **Chapter6-2. 3과 5의 배수 합하기**

10미만의 자연수에서 3과 5의 배수를 구하면 3, 5, 6, 9이다. 이들 총합은 23이다. 그렇다면 1000 미만의 자연수에서 3과 5의 배수의 총합을 구하려면 어떻게 프로그램을 만들어야 할까?

위 프로그램을 구현할 때 가장 주의해야 할 점은 `3과 5의 배수가 겹칠 때 이를 2번 counting하지 않도록 하는 것`이다.

1. for문 이용

```python
sum = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i


>>> print(sum)
233168
```

일단 합계를 구할 sum 변수를 만들어준다. 그리고 if문에서 or을 이용하여 3과 5의 배수가 겹치지 않도록 해주면 된다.

2. while문 이용

```python
sum = 0
n = 1
while n < 1000:
    if n % 3 == 0 or n % 5 == 0:
        sum += n
    n += 1


>>> print(sum)
233168
```

while문을 이용할 때 또한 sum 변수를 생성해준다. 그리고 반복할 때마다 1씩 증가할 n 변수를 사용하여 for문과 같이 만들어주면 된다.

___

# **Chapter6-3. 게시판 페이징하기**

게시물의 총 건수와 한 페이지에 보여줄 게시물 수를 입력으로 주었을 때 총 페이지 수를 출력하는 프로그램이 필요하다고 한다. 이를 getTotalPage로 구현해보자.

이 함수를 구현할 때에는 게시물의 총 건수를 한 페이지에 보여줄 게시물 수로 나누었을 때의 나머지를 이용하면 되는데 두 가지 경우로 나뉜다.
* 나누어 떨어지는 경우 : 나눈 몫을 그대로 사용한다.
* 나누어 떨어지지 않는 경우 : 나눈 몫에서 1을 더한다.

```python
def getTotalPage(totalgun, onegun):
    if total % onegun == 0:
        return total // onegun
    else:
        return total // onegun + 1


>>> print(getTotalPage(15, 10))
2
>>> print(getTotalPage(30, 10)) 
3
```
