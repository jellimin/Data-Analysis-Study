# **7-2. 정규 표현식 시작하기**

## **정규 표현식의 기초, 메타 문자**

메타문자란 원래 그 문자가 가진 뜻이 아닌 특별한 용도로 사용하는 문자를 의미한다. 즉, 정규표현식에 메타문자를 사용하면 특별한 의미를 갖게 된다. 여러 메타 문자에 대해서 알아보자.

___

## **(문자열 소비가 있는) 메타 문자의 종류와 그 의미**

이 때 문자열 소비가 있다는 것은 매치가 진행될 때 현재 매치되고 있는 문자열의 위치가 변경된다는 것이다.

* **문자 클래스 []**

문자 클래스 []는 `대괄호 [] 안에 문자들과 매치`라는 의미를 갖는다. 예를 통해 살펴보자.<br>

|정규식|문자열|매치 여부|설명|
|:---:|:---:|:---:|:---:|
||a|Yes|"a"는 정규식과 일치하는 문자 "a"가 있으므로 매치|
|[abc]|before|Yes|"before"은 정규식과 일치하는 문자 "b"가 있으므로 매치|
||dude|No|"dude"는 정규식과 일치하는 문자가 없으므로 매치되지 않음|

이 때 두 문자 사이에 하이픈(-)을 사용하면 두 문자 사이의 범위를 의미하며, 문자 클래스에서 주의해야 할 메타문자는 `^`인데 Not의 의미를 가지고 있다.<br> 
(ex) [0-5] : [012345], [a-zA-Z] : 알파벳 모두, [^0-9] : 숫자가 아닌 문자

* **자주 사용하는 문자 클래스**

|정규 표현식|설명|
|:---:|:---:|
|\d|숫자와 매치|
|\D|숫자 아닌 것과 매치|
|\s|whitespace 문자(공백, tab 등)과 매치|
|\S|whitespace 문자가 아닌 것과 매치|
|\w|문자+숫자와 매치, [a-zA-Z0-9_]와 동일, 즉 문자, 숫자, 언더바|
|\W|문자+숫자가 아닌 문자와 매치|

* **Dot(.)**

Dot(.) 메타 문자는 줄바꿈 문자 \n을 제외한 모든 문자와 매치됨을 의미한다. 하지만 추후에 배울 컴파일 옵션 중 re.DOTALL을 주면 \n 문자와도 매치된다. 예시를 통해 살펴보자.

|정규식|문자열|매치 여부|설명|
|:---:|:---:|:---:|:---:|
||aab|Yes|"aab"는 a와 b 사이에 a가 있으므로 매치됨|
|a.b|a0b|Yes|"a0b"는 a와 b 사이에 0이 있으므로 매치됨|
||abc|No|"abc"는 a와 b 사이에 어떠한 문자도 없으므로 매치되지 않음|

이 때 a[.]b라는 정규식은 문자 클래스 [] 사이에 Dot가 들어가있으므로 Dot 그 자체를 의미하는 것이다.

* **반복 * , + , {} , ?**

반복을 의미하는 메타 문자에는 다양한 종류가 있다.
|메타문자|의미|예시|
|:--:|:--:|:--:|
|*|* 문자 바로 앞에 있는 문자가 0번 이상 반복되면 매치|ca*t|
|+|+ 문자 바로 앞에 있는 문자가 1번 이상 반복되면 매치|ca+t|
|{}|반복 횟수를 범위 또는 값으로 제한 가능|ca{1, 3}t, a{3}|
|?|반복 횟수가 0회 또는 1회이면 매치, 따라서 있거나 없거나를 의미|ca?t|

___

## **(문자열 소비가 없는) 메타 문자의 종류와 그 의미**

문자열 소비가 없다는 것은 매치 시 문자열의 위치가 변하지 않는다는 것이다.

* **|**

| 메타 문자는 or과 동일한 의미로 사용된다.

* **^**

^ 메타 문자는 문자열의 맨 처음과 일치함을 의미한다. 만약 컴파일 옵션 re.MULTILINE을 사용할 경우 여러 줄의 문자열일 때 각 줄의 처음과 일치하게 된다. `앞에서 문자열 클래스에서 배웠던 [^...]의 Not의 의미와 헷갈리지 말자.`

* **$**

$ 메타 문자는 ^ 메타 문자와 반대로 문자열의 끝과 매치함을 의미한다.

* **\b**

\b 메타 문자는 단어 구분자를 나타낸다. 단어 구분자란 ?(물음표), .(Dot), 공백, $ 등을 의미한다. `앞에서 배웠던 whitespace를 의미하는 메타 문자인 \s와 헷갈리지 말자.`

___

## **파이썬에서 정규 표현식을 지원하는 re 모듈**

파이썬에서는 정규 표현식을 지원하기 위해 re 모듈을 제공한다. 사용 방법은 아래와 같다.

```python
import re
p = re.compile("ab*")
```

re.compile을 사용하여 정규 표현식을 컴파일한다. re.compile의 결과로 돌려주는 패턴 객체를 사용하여 그 이후의 작업을 수행할 수 있다. 또한, 추후에 정규식을 컴파일할 때 특정 옵션을 주는 것도 배울 것이다.

___

# **정규식을 사용한 문자열 검색**

컴파일된 패턴 객체를 사용하여 문자열 검색을 수행할 수 있다. 컴파일된 패턴 객체는 다음과 같은 4가지 메서드를 제공한다.

|메서드|목적|
|:---:|:---:|
|match()|문자열의 처음부터 정규식과 매치되는지 조사|
|search()|문자열 전체를 검색하여 정규식과 매치되는지 조사|
|findall()|정규식과 매치되는 모든 문자열을 리스트로 돌려줌|
|finditer()|정규식과 매치되는 모든 문자열을 반복 가능한 객체로 돌려줌|

1. match

match() 메서드는 문자열의 처음부터 정규식과 매체되는지 조사한다. 즉, 처음 정규식과 매치되지 않으면 None을 돌려낸다.

```python
import re

p = re.compile("[a-z]+")
m = p.match("python is good")
print(m)
>>> <re.Match object; span=(0, 6), match='python'>

p = re.compile("[a-z]+")
m = p.match("3 is good")
print(m)
>>> None
```

"python is good"이라는 문자열은 정규식 [a-z]+와 매치되므로 match 객체를 돌려준다.<br>
"3 is good"이라는 문자열은 정규식 [a-z]+와 매치되지 않으므로 None을 돌려낸다. <br>
match 메서드의 결과로 match 객체 혹은 None을 돌려주기 때문에 파이썬 정규식 프로그램은 보통 아래와 같은 흐름으로 작성한다.

```python
import re

p = re.compile("[a-z]+")
m = p.match("python is good")
if m:
    print("Match found :", m.group())
else:
    print("No match")
```

이 때 group()은 뒤에서 배울 match 객체의 메서드인데 매치된 문자열을 돌려준다.

2. search

```python
import re

p = re.compile("[a-z]+")
m = p.search("3 is good")
print(m)
>>> <re.Match object; span=(2, 4), match='is'>
```

search 메서드는 문자열의 처음과 매치하는 match 메서드와 달리 문자열의 전체와 매치한다. 따라서 문자열의 처음인 3과 매치되지 않았지만 is와 매치된 것을 확인할 수 있다.

3. findall

```python
import re

p = re.compile("[a-z]+")
result = p.findall("life is too short")
print(result)
>>> ['life', 'is', 'too', 'short']
```

findall 메서드는 전체 문자열을 정규식과 매치하여 매치된 모든 문자열을 리스트 형태로 돌려준다.

4. finditer

```python
import re

p = re.compile("[a-z]+")
result = p.finditer("life is too short")
print(result)
>>> <callable_iterator object at 0x00000228A0B97100>

for i in result:
    print(i)
>>> <re.Match object; span=(0, 4), match='life'>
>>> <re.Match object; span=(5, 7), match='is'>
>>> <re.Match object; span=(8, 11), match='too'>
>>> <re.Match object; span=(12, 17), match='short'>
```

finditer 매서드는 결과로 반복 가능한 객체를 돌려준다. 따라서 for문을 이용하여 각 요소를 출력해보면 match 객체를 돌려주는 것을 볼 수 있다.

___

## **match 객체의 메서드**

앞에서 문자열을 정규식과 매치한 후 얻은 결과인 match 객체를 통해 생길 수 있는 궁금증이 있다.

* 어떤 문자열이 매치되었는가 ?
* 매치된 문자열의 인덱스는 어디부터 어디까지인가 ?

이를 해결할 수 있는 match 객체의 메서드는 아래와 같다.

|메서드|목적|
|:---:|:---:|
|group()|매치된 문자열을 돌려줌|
|start()|매치된 문자열의 시작 위치를 돌려줌|
|end()|매치된 문자열의 끝 위치를 돌려줌|
|span()|매치된 문자열의 (시작, 끝)에 해당하는 튜플을 돌려줌|

```python
import re

p = re.compile("[a-z]+")
m = p.match("python is good")
print(m.group())
print(m.start())
print(m.end())
print(m.span())
>>> python 
>>> 0
>>> 6
>>> (0, 6)
```

위와 마찬가지로 search 메서드를 이용하여 돌려받은 match 객체를 가지고도 match 메서드를 사용할 수 있다.

___

## **모듈 단위로 수행하기**

지금까지 re 모듈을 이용하여 정규식을 컴파일 한 후 얻은 패턴 객체를 이용하여 문자열 검색을 하였다. re 모듈은 이를 조금 더 축약한 형태로 사용할 수 있는 방법을 제공하는데 아래와 같다.

```python
import re
m = re.match("[a-z]+, "python is good")
```

___

## **컴파일 옵션**

정규식을 컴파일할 때 다음 옵션을 사용할 수 있다.

|옵션 이름|약어|설명|
|:--:|:--:|:--:|
|DOTALL|S|dot 문자(.)가 줄바꿈 문자를 포함하여 모든 문자와 매치|
|IGNORECASE|I|대, 소문자에 관계없이 매치|
|MULTILINE|M|여러 줄과 매치 (^, $ 메타문자의 사용과 관계)|
|VERBOSE|X|verbose 모드를 사용함 (정규식을 보기 편하게 하며 주석 사용 가능)|

1. DOTALL

앞에서 배웠듯이 메타문자 .은 줄바꿈 문자 \n을 제외한 모든 문자라고 하였다. 하지만, 컴파일 옵션인 DOTALL을 이용하면 메타 문자 .도 포함될 수 있다. re.DOTALL 옵션은 여러 줄로 된 문자열에서 줄바꿈 문자인 \n에 상관없이 검색할 때 자주 사용된다.

```python
import re

p = re.compile("a.b", re.DOTALL)
m = p.match("a\nb")
print(m)
>>> <re.Match object; span=(0, 3), match='a\nb'>
```

2. IGNORECASE
IGNORECASE는 대, 소문자 구별없이 매치를 수행할 때 사용하는 옵션이다.

```python
import re

p = re.compile("[a-z]", re.IGNORECASE)
m = p.match("python")
print(m)
>>> <re.Match object; span=(0, 1), match='p'>

m = p.match("Python")
print(m)
>>> <re.Match object; span=(0, 1), match='P'>

m = p.match("Python")
print(m)
>>> <re.Match object; span=(0, 1), match='P'>
```

3. MULTILINE
MULTILINE은 메타문자 ^, $과 함께 사용한다. 이 때 ^는 문자열의 처음, $는 문자열의 끝을 의미한다. 예를 통해 살펴보자.

```python
import re

p = re.compile("^python\s\w+", re.MULTILINE)

data = """python one
life is too short
python two
you need python
python three"""

result = p.findall(data)
print(result)
>>> ['python one', 'python two', 'python three']
```

여기서 re.MULTILINE은 여러 줄로 된 문자열의 매 줄마다 정규식과 매치를 하는 것이다. 이 때 해당 옵션이 없었더라면 비록 findall 메서드를 사용하였지만 ^ 메타문자로 인해 첫번째 줄만 매치가 되었을 것이다.

4. VERBOSE

정규식이 굉장히 복잡해진다면 한 눈에 알아보기 어렵기 때문에 주석 또는 줄 단위로 구분하면 좋을 것이다. 이 때 사용하는 것이 re.VERBOSE 옵션이다. 

___

## **백슬래시 문제**
정규 표현식에서 백슬래시를 사용하면 혼란을 줄 수 있는데 이를 해결하기 위해서는 raw string을 의미하는 r을 사용해야 한다. 일단 아래 예시를 보자.

```python
import re
p = re.compile("\section")
```

현재 "\section"이라는 정규식을 사용하고 싶은데 \s는 앞에서 배운 whitespace로 인식되기 때문에 위와 같이 사용할 수 없다.

```python
import re
p = re.compile("\\section")
```

그렇다면 \\은 백슬래시 문자열 자체임을 알려주므로 위와 같이 백슬래시를 2개를 사용하면 어떨까?<br>
하지만 파이썬 문자열 리터럴 규칙에 따라 `\\`이 `\`로 변경되어 결국 \section이 전달된다.

```python
import re
p = re.compile(r"\\section")
```

따라서 파이썬 정규식에는 raw string이라는 규칙이 생겨나게 되었는데, 이는 컴파일해야 하는 정규식이 raw string 임을 알려 줄 수 있도록 하는 것이다. 정규식 문자열 앞에 r 문자를 삽입하면 된다.
