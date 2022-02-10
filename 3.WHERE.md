# **SQL WHERE절 및 연산자**

## **WHERE절**

WHERE절은 행(레코드)를 필터링하는데 사용된다. 즉, 지정된 조건을 충족하는 레코드만 추출하는 것이다.<br>
<br>

## **WHERE절의 기본 형태**
WHERE절의 기본형태는 아래와 같다.
> SELECT col1, col2, ... FROM table_name<br>
> WHERE condition;

앞에서 배웠던 것처럼 SELECT문 뒤에는 추출하고 싶은 열(필드), FROM 뒤에는 테이블명이 온다.<br>
그리고 WHERE 뒤에는 추출하고자 하는 행의 조건(condition)이 온다.<br>
참고로 `WHERE절은 SELECT문 외에도 UPDATE, DELECT문에서도 사용가능`하다.<br>
<br>

## WHERE절 예시
1. Customers 테이블에서 "Mexico" 국가의 고객을 선택하라.
> SELECT * FROM Customers <BR>
> WHERE Country = "Mexico"; <BR>


<BR>

2. Customers 테이블에서 고객 ID가 1인 고객을 선택하라.
> SELECT * FROM Customers<BR>
> WHERE CustomerID =1;<BR>

1번에서는 조건이 텍스트값을 요구했기 때문에 작은 따옴표('') 혹은 큰 따옴표("")가 필요하지만, 2번에서는 숫자이므로 따옴표로 묶지 않아야 한다.<br>
또한, SQL문은 대/소문자를 구별하지 않지만 테이블 안에 들어있는 문자는 대/소문자를 구분하므로 주의한다.
___
## **WHERE절의 연산자**

WHERE절에서는 다음과 같은 연산자들을 사용할 수 있다.

* 산술연산자<br>

|연산자|기능|
|:---:|:---:|
|+|덧셈|
|-|뺄셈|
|*|곱셈|
|/|나눗셈|

* 비교연산자<br>

|연산자|기능|
|:---:|:---:|
|=|같다|
|>|~보다 크다|
|<|~보다 작다|
|>=|~보다 크거나 같다|
|<=|~보다 작거나 같다|
|<> , != , ^=|같지 않다|

* 그 외의 연산자

|연산자|기능|
|:---:|:---:|
|AND|그리고 (둘다 만족)|
|OR|또는|
|NOT|~가 아닌|
|BETWEEN|특정 범위 사이에 있다 (이상, 이하)|
|LIKE|문자열의 패턴 검색|
|IN|특정 열에 해당하는 조건 여러 개 지정|<br>
<br>

## **BETWEEN A AND B 연산자 예시**

Products 테이블에서 Price가 50 이상 60 이하인 데이터를 선택하라.

> SELECT * <BR>
> FROM Products <BR>
> WHERE Price BETWEEN 50 AND 60;<BR>

## **LIKE 연산자와 와일드카드**

Customers 테이블에서 City가 s로 시작하는 데이터를 선택하라.

> SELECT * <BR>
> FROM Customers <BR>
> WHERE City LIKE "s%";<BR>

이 때, `NOT LIKE`를 사용하면 반대의 결과가 출력된다. 그리고 LIKE와 함께 사용하는 와일드카드는 `%`, `_`가 있다.

* `%` : 모든 문자
* `_` : 한 글자

예를 들어 `'_a%'`를 사용했다면 a 앞에 한 글자가 오고, a 뒤에 모든 문자가 오면 된다. 결국 a가 2번째 위치에 있는 데이터를 뽑아낸다는 것이다.<br>
`LIKE` 연산자에서도 `'a'`만을 적어준다면 a 문자 그대로 가진 데이터를 뽑아낸다는 것이다.

## **IN 연산자**

Customers 테이블에 City가 파리거나 런던인 데이터를 선택하라.

> SELECT * <BR>
> FROM Customers <BR>
> WHERE City IN ('Paris', 'London');<BR>

## **연산자 예시**

1. Customers 테이블에서 City 열에 "Berlin" 값이 있는 레코드를 선택하십시오.

> SELECT * <BR> 
> FROM Customers <BR>
> WHERE City = "Berlin"; <BR>

<BR>

2. Customers 테이블에서 Country가 독일이고 City가 베를린인 데이터를 선택하라.

> SELECT *<BR>
> FROM Customers <BR>
> WHERE Country = "Germany" AND City = "Berlin"; <BR>
<BR>

3. Customers 테이블에서 City가 베를린 또는 런던인 데이터를 선택하라.

> SELECT * <BR>
> FROM Customers <BR>
> Where City = "Berlin" OR City = "London"; <BR>

<BR>

4. Customers 테이블에서 Country가 독일이 아닌 데이터를 선택하라.

> SELECT * <BR>
> FROM Customers <BR>
> WHERE NOT Country = "GERMANY"; <BR>

<BR>

5. Customers 테이블에서 Country가 독일이고, City가 베를린 또는 런던인 데이터를 선택하라.

> SELECT * <BR>
> FROM Customers <BR>
> WHERE Country = "Germany" AND (City = "Berlin" OR City = "London");<BR>

<BR>

6. Customers 테이블에서 Country가 독일이 아니고 미국이 아닌 데이터를 선택하라.

> SELECT * <BR>
> FROM Customers <BR>
> WHERE NOT Country = "Germany" AND NOT Country = "USA";<BR>
