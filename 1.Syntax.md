# **SQL 구문**

## **데이터 베이스와 테이블**
데이터 베이스에는 대부분 하나 이상의 테이블이 포함된다. 각 테이블은 이름을 가지고 있다 (ex. Customers, Categories). 테이블에는 record라고 불리는 행 / field라고 불리는 열이 포함되어 있다.<br>
<br>
아래는 "Categories" 테이블의 예시이다.

![테이블 예시 이미지](https://drive.google.com/uc?id=1XiNANsRPPZqfOnB1yIaokq4wIJIZNHHb)
테이블에는 8개의 행과 3개의 열(CategoryID, CategoryName, Description)이 포함되어 있다.

## **SQL에서 대소문자**
SQL에서는 대소문자를 구분하지 않는다. 따라서 `SELECT`와 `Select`는 같다. 하지만 보통 SQL에서는 대문자로 작성한다.

## **SQL문 끝에 세미콜론(;)**
일부 데이터베이스 시스템에서는 각 SQL문의 끝에 세미콜론이 필요하다. 