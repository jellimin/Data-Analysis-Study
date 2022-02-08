# **Chapter2-5. 딕셔너리 자료형**

## **딕셔너리란 ?**

파이썬에서는 대응 관계를 나타낼 수 있는 자료형을 가지고 있는데, 이를 딕셔너리(Dictionary)라고 한다. 단어 그대로 해석하면 '사전'이라는 뜻을 가지고 있다. 딕셔너리에서 핵심은 `key를 통해 value를 얻는다` 인데 아래 그림을 통해 쉽게 이해할 수 있다.

![사전 참고 이미지](https://drive.google.com/uc?id=1ioAthyqr28S2Gva9FRokUdkdPYuBlZRd)

위 그림은 네이버 어학사전에 analysis를 검색하였을 때 분석연구, 분석이라는 결과가 나옴을 보여준다. 결국 여기서 key는 analysis, value는 분석 연구, 분석임을 알 수 있다.
___
## **딕셔너리 생성**
딕셔너리의 기본 모습은 아래와 같다.<br>
`{key1:value1, key2:value2, ...}`<br>
key와 value 쌍 여러개가 중괄호 {}로 둘러싸여 있으며, 각각의 요소는 key:value 형태로 이루어져있고, 쉼표로 구분된다. 예시는 아래와 같다.
```
>>> dic = {'name':'jully', 'phone':'012-345-6789', 'age':'23'}
>>> print(dic)
{'name':'jully', 'phone':'012-345-6789', 'age':'23'}
```
여기서 key는 'name', 'phone', 'age'이며, value는 'jully', '012-345-6789', '23'이다. 이를 이해하기 쉽게 표로 나타내면 아래와 같다.<br>
|key|value|
|:---:|:---:|
|name|jully|
|phone|012-345-6789|
|age|23|<br>

## **딕셔너리 쌍 추가하기**
```
>>> dic = {'name':'jully'}
>>> dic['age'] = '23'
>>> print(dic)
{'name':'jully', 'age':'23'}
```
위와 같이 기존의 하나의 key와 value만을 가진 dic 변수에 딕셔너리 쌍을 추가하기 위해 `딕셔너리명[key명] = value명` 을 이용하면 딕셔너리 쌍이 추가됨을 확인할 수 있다.

## **딕셔너리 쌍 삭제하기**
```
>>> dic = {'name':'jully', 'phone':'012-345-6789', 'age':'23'}
>>> del dic['phone']
>>> print(dic)
{'name':'jully', 'age':'23'}
```
위와 같이 딕셔너리 쌍을 삭제하고 싶다면 `del 딕셔너리명[key명]`을 이용하면 된다.

## **딕셔너리에서 key를 사용해 value 얻기**
```
>>> dic = {'name':'jully', 'phone':'012-345-6789', 'age':'23'}
>>> print(dic['name'])
jully
```
위와 같이 딕셔너리에서 key인 name을 사용해 value인 jully를 얻고 싶다면 `딕셔너리명[key명]`을 이용하면 된다.
___
## **딕셔너리 관련 함수**

### **1. keys 리스트 만들기** 
```
>>> grade = {'jully':90, 'kate':80, 'jessi':70}
>>> print(grade.keys())
dict_keys(['jully', 'kate', 'jessi'])
```
딕셔너리에서 key만 모으고 싶다면 `딕셔너리명.keys()`을 이용하여 dict_keys라는 객체를 얻을 수 있다. 결과를 보면 리스트와 유사하지만, 리스트 고유의 append, sort, pop, insert, remove 등을 사용할 수 없다. 그렇다면 이 dict_keys 객체를 어떻게 사용할 수 있을까?
```
>>> for k in grade.keys():
        print(k)
jully
kate
jessi

>>> print(list(grade.keys()))
['jully', 'kate', 'jessi']
```
for문을 이용하여 key를 하나씩 출력하거나, dict_keys 객체를 리스트로 바꾸어 출력하는 방법으로 많이 사용한다.

### **2. values 리스트 만들기** 
```
>>> grade = {'jully':90, 'kate':80, 'jessi':70}
>>> print(grade.values())
dict_values([90, 80, 70])
```
딕셔너리에서 value만 모으고 싶다면 `딕셔너리명.values()`를 이용하여 dict_values 객체를 얻을 수 있다. 
```
>>> for v in grade.values():
        print(v)
90
80
70

>>> print(list(grade.values()))
[90, 80, 70]
```
위와 같이 for문을 이용하여 값을 하나씩 출력하거나, list로 바꾸어 출력하는 방법으로 dict_keys 객체를 사용할 수 있다.

### **3. key, value 쌍 얻기**
```
>>> grade = {'jully':90, 'kate':80, 'jessi':70}
>>> print(grade.items())
dict_items([('jully', 90), ('kate', 80), ('jessi', 70)])
``` 
key, value 쌍을 얻기 위해서는 `딕셔너리명.items()`을 이용하여 key와 value를 튜플로 묶은 값을 원소로 하는 dict_items 객체를 얻을 수 있다.
```
>>> for k, v in grade.items():
        print("키는 :" + k)
        print("값은 :" + v)
키는 :jully
값은 :90
키는 :kate
값은 :80
키는 :jessi
값은 :70
```
위와 같이 for문을 이용하여 key와 value를 하나씩 출력할 수 있다.

### **4. key, value 쌍 모두 지우기**
```
>>> dic = ['apple':'사과', 'strawberry':'딸기']
>>> dic.clear()
>>> print(dic)
{}
```
딕셔너리에서 key, value 쌍을 모두 지우기 위해서는 `딕셔너리명.clear()`을 이용하여 빈 딕셔너리로 만들 수 있다. 

### **5. key로 value 얻기**
key로 value를 얻는 방법은 2가지가 있다. 
* 대괄호 [] 이용
``` 
>>> dic = ['apple':'사과', 'strawberry':'딸기']
>>> print(dic['apple'])
사과

>>> print(dic['pear'])
Traceback (most recent call last):
  File "c:\python\chapter2.py", line 426, in <module>
    print(dic['pear'])
KeyError: 'pear'
```
1번째 방법은 대괄호 []를 이용하는 방법이다. 이는 딕셔너리에 없는 key를 넣을 시 에러가 발생하게 된다.

* get 함수 이용
``` 
>>> dic = ['apple':'사과', 'strawberry':'딸기']
>>> print(dic.get('apple'))
사과

>>> print(dic.get('pear'))
None

>>> print(dic.get('pear', '없음'))
없음
```
2번째 방법은 get() 함수를 이용하는 것이다. `딕셔너리명.get(key명)`을 이용하면 된다. 이 때 딕셔너리에 없는 key를 넣을 시 대괄호를 이용하는 방법과 달리 None을 결과값으로 얻게 된다. 이 때 해당 key가 없을 때 출력하고자 하는 값을 콤마 뒤에 넣게 되면 그 값이 출력되는 것을 확인할 수 있다.

### **6. 해당 key가 딕셔너리 안에 있는지 조사하기**
```
>>> dic = ['apple':'사과', 'strawberry':'딸기']
>>> print('apple' in dic)
True

>>> dic = ['apple':'사과', 'strawberry':'딸기']
>>> print('pear' in dic)
False
```
해당 key가 딕셔너리 안에 있는지 조사하기 위해서는 `key명 in 딕셔너리명`을 이용하면 된다. 이 때 해당 key가 딕셔너리 안에 있을 때는 True를, 없을 때는 False를 출력한다.
___
