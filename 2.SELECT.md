# **SQL SELECT문**

## **SELECT문**
`SELECT`문은 데이터 베이스에서 데이터를 선택하는데 사용된다. 정확하게 말해서 특정 열 또는 열 전체를 선택하는데 사용된다. 선택된 데이터는 결과 테이블에 저장된다.<br>
<br>

## **SELECT문의 기본 형태**
SELECT문의 기본 형태는 아래와 같다.

> SELECT col1, col2, ... <br>
> FROM table_name;

여기서 SELECT 뒤에는 선택하고 싶은 열들이 오고, FROM 뒤에는 테이블명이 온다<br>
<br>
## **SELECT문 예시**
1. Customers 테이블에서 CustomerName 및 City 열을 선택하라.
> SELECT CustomerName, City FROM Customers;<br>


![SELECT 예시1](https://drive.google.com/uc?id=1OQQkMmCAGdGMtelrHsuu0VRq7LXbR2I6)
<br>

2. Customers 테이블에서 모든 열을 선택하라.
> SELECT * FROM Customers;<br>

![SELECT 예시2](https://drive.google.com/uc?id=16e5E90Jl405RVhGi_VkfItLciImSS2aI)

위와 같이 테이블에서 모든 열을 선택하고 싶을 때에는 SELECT 뒤에 `'*'`을 입력하면 모든 열이 선택된다.
___

## **SELECT DISTINCT문**
테이블 내부의 열에는 종종 많은 중복된 값이 포함되어 있다. 이 때 사용되는 `SELECT DISTINCT`문은 선택한 열에서 고유한 값만 반환하는데 사용된다.<br>
<br>

## **SELECT문의 기본 형태**
SELECT문의 기본 형태는 아래와 같다.
> SELECT DISTINCT col1, col2, ... <br>
FROM table_name;<br>

<br>

## **SELECT DISTINCT문 예시**
1. Customers 테이블의 Country 열에서 고유한 값만 선택하라.
> SELECT DISTINCT Country FROM Customers;<br>

![SELECT DISTINCT 예시1](https://drive.google.com/uc?id=1GdZYV3kefECbLNHocQgn4Wj8kjdJgw6z)

<br>

2. Customers 테이블의 Country 열에서 고유한 고객 국가의 수를 구하라.
> SELECT COUNT (DISTINCT Country) FROM Customers;<br>

![SELECT DISTINCT 예시2](https://drive.google.com/uc?id=1PYN1RYXS0EG4zW6WJfqNzQzK-JJcbPgL)

열에서 고유한 값의 개수를 알기 위해서는 `SELECT COUNT (DISTINCT 열명)`을 사용하면 된다.