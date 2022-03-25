# **4. 범주형(카테고리) 데이터 처리**

## **4-1. [범주형 데이터로의 변환] 구간 분할**

* 구간 분할 : np.histogram()함수 이용하여 각 구간에 속하는 값의 개수 / 경계값 구함
* 범주형 데이터로의 변환 : pd.cut() 함수를 이용하여 연속 데이터를 여러 구간으로 나눠 범주형 데이터로 변환

```python
import pandas as pd
import numpy as np

df = pd.read_csv('./auto-mpg.csv', header = None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']

# horsepower 열의 누락 데이터('?')를 삭제하고 실수형으로 변환
df['horsepower'].replace('?', np.nan, inplace = True)
df.dropna(subset = ['horsepower'], axis = 0, inplace = True)
df['horsepower'] = df['horsepower'].astype('float')

# 구간 분할 np.histogram()
count, bin_dividers = np.histogram(df['horsepower'], bins = 3)
print(bin_dividers)
>>> [ 46.         107.33333333 168.66666667 230.        ]

# 범주형 데이터로 변환 pd.cut()
df['hp_bin'] = pd.cut(x = df['horsepower'], # 데이터 배열
                      bins = bin_dividers, # 경계값 리스트
                      labels = ['저출력', '보통출력', ''], # bin 이름
                      include_lowest = True) # 각 구간의 낮은 경계값 포함 여부
print(df[['horsepower', 'hp_bin']].head(15))
>>>     horsepower hp_bin
>>> 0        130.0   보통출력
>>> 1        165.0   보통출력
>>> 2        150.0   보통출력
>>> 3        150.0   보통출력
>>> 4        140.0   보통출력
>>> 5        198.0    고출력
>>> 6        220.0    고출력
>>> 7        215.0    고출력
>>> 8        225.0    고출력
>>> 9        190.0    고출력
>>> 10       170.0    고출력
>>> 11       160.0   보통출력
>>> 12       150.0   보통출력
>>> 13       225.0    고출력
>>> 14        95.0    저출력
```

___

## **4.2 [범주형 데이터의 활용]더미 변수**

카테고리를 나타내는 범주형 데이터를 머신러닝 알고리즘에 바로 사용할 수 없는 경우가 있어, 컴퓨터가 인식 가능한 입력값으로 변환해야 한다. 이러한 경우 숫자 0 또는 1로 표헌되는 `더미 변수(dummy variable)`을 사용한다. 이처럼 범주형 데이터를 컴퓨터가 인식할 수 있도록 숫자 0, 1로만 구성한다고 해서 원핫인코딩이라고도 부른다.

* 더미 변수 : pd.get_dummies() 함수 이용

이 때, 각각의 범주가 더미 변수의 열 이름이 된다. 각 더미 변수가 본래 속해 있던 행에는 1이, 속하지 않았던 행에는 0이 입력된다.

```python
horsepower_dummies = pd.get_dummies(df['hp_bin'])
print(horsepower_dummies.head(15))
>>>     저출력  보통출력  고출력
>>> 0     0     1    0
>>> 1     0     1    0
>>> 2     0     1    0
>>> 3     0     1    0
>>> 4     0     1    0
>>> 5     0     0    1
>>> 6     0     0    1
>>> 7     0     0    1
>>> 8     0     0    1
>>> 9     0     0    1
>>> 10    0     0    1
>>> 11    0     1    0
>>> 12    0     1    0
>>> 13    0     0    1
>>> 14    1     0    0
```

<br>

* 원핫인코딩 : sklearn 라이브러리를 이용

```python
from sklearn import preprocessing

# 전처리를 위한 encoder 객체 만들기
label_encoder = preprocessing.LabelEncoder()
onehot_encoder = preprocessing.OneHotEncoder()

# label_encoder로 문자열 범주를 숫자형 범주로 변환
onehot_labeled = label_encoder.fit_transform(df['hp_bin'].head(15))
print(onehot_labeled)
print(type(onehot_labeled))
print('\n')

# 2차원 행렬로 변경
onehot_reshaped = onehot_labeled.reshape(len(onehot_labeled), 1)
print(onehot_reshaped)
print(type(onehot_reshaped))
print('\n')

# 희소행렬로 변환
onehot_fitted = onehot_encoder.fit_transform(onehot_reshaped)
print(onehot_fitted)
print(type(onehot_fitted))
```
___

## **[추가] 더미 변수 vs 원핫인코딩**

1. pd.get_dummies()의 문제점

pd.get_dummies()는 train 데이터의 특성을 학습하지 않기 때문에 train 데이터에만 있고 test 데이터에는 없는 카테고리를 test 데이터에서 원핫인코딩 된 칼럼으로 바꿔주지 않는다. 예를 들어 train 데이터에는 카테고리가 `a, b, c`가 존재하면 3개의 컬럼이 생기지만, test 데이터에 카테고리가 `a, b`라면 2개의 컬럼밖에 생기지 않는다.

2. sklearn.preprocessing.OneHotEncoder는 train 데이터의 특성을 학습할 수 있다.

위와 같이 test 데이터에 `c`라는 카테고리가 없더라도 `c` 컬럼까지 반영되어 test 데이터에 3개의 컬럼이 생기게 된다.

___

# **5. 정규화**

숫자 데이터의 상대적인 크기 차이를 제거할 필요가 있기 때문에 각 열에 속하는 데이터 값을 동일한 크기 기준으로 나눈다. 이를 정규화라고 하며, 이 과정을 거친 데이터의 범위는 0~1 또는 -1~1이 된다.

1. 각 열의 데이터를 해당 열의 최대값(의 절대값)으로 나누는 방법

```python
import pandas as pd
import numpy as np

df = pd.read_csv('./auto-mpg.csv', header = None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']

# horsepower 열의 누락 데이터를 삭제하고 실수형으로 변환
df['horsepower'].replace('?', np,nan, inplace = True)
df.dropna(subset = ['horsepower'], axis = 0, inplace = True)
df['horsepower'] = df['horsepower'].astype('float')

# horsepower 열의 최대값의 절대값으로 모든 데이터를 나눠서 저장
df.horsepower = df.horsepower / abs(df.horsepower.max())

print(df.horsepwer.head())
>>> 0    0.565217
>>> 1    0.717391
>>> 2    0.652174
>>> 3    0.652174
>>> 4    0.608696
>>> Name: horsepower, dtype: float64
```

2. Min-Max Normalization : 각 열의 데이터에서 해당 열의 최소값을 뺀 값을 분자로, 해당 열의 최대값과 최소값의 차이를 분모로 하는 정규화 방법

```python
import pandas as pd
import numpy as np

df = pd.read_csv('./auto-mpg.csv', header = None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']

# horsepower 열의 누락 데이터를 삭제하고 실수형으로 변환
df['horsepower'].replace('?', np.nan, inplace = True)
df.dropna(subset = ['horsepower'], axis = 0, inplace = True)
df['horsepower'] = df['horsepower'].astype('float')

# Min-Max Normalization
min_x = df.horsepower - df.horsepower.min()
min_max = df.horsepower.max() - df.horsepower.min()
df.horsepower = min_x / min_max

print(df.horsepower.head())
>>> 0    0.456522
>>> 1    0.646739
>>> 2    0.565217
>>> 3    0.565217
>>> 4    0.510870
>>> Name: horsepower, dtype: float64
```

___

# **6. 시계열 데이터**

주식, 환율 등 금융 데이터를 다루기 위해 개발된 판다스는 시계열 데이터를 다루는 여러 유용한 기능을 제공한다. 특히, 시계열 데이터를 데이터프레임의 행 인덱스로 사용하면, 시간으로 기록된 데이터를 분석하는 것이 매우 편리하다.<br>
판다스의 시간 표시 방식 중 자주 이용되는 2가지 유형은 아래와 같다.

* 특정 시점을 기록하는 Timestamp
* 두 시점 사이의 일정한 기간을 나타내는 Period

## **6-1. 다른 자료형을 시계열 객체로 변환**

판다스는 다른 자료형으로 저장된 시간 데이터를 판다스 시계열 객체로 변환할 수 있다.

이 때 `문자열 객체 -> Timestamp 객체 -> Period 객체` 순으로 변환할 수 있다.<br>
<br>

1. Timestamp로 변환
* Timestamp로 변환 : pd.to_datetime()을 이용

```python
import pandas as pd

df = pd.read_csv('./stock-data.csv')
print(df.head())
>>>          Date  Close  Start   High    Low  Volume
>>> 0  2018-07-02  10100  10850  10900  10000  137977
>>> 1  2018-06-29  10700  10550  10900   9990  170253
>>> 2  2018-06-28  10400  10900  10950  10150  155769
>>> 3  2018-06-27  10900  10800  11050  10500  133548
>>> 4  2018-06-26  10800  10900  11000  10700   63039

print(df.info()) # Date열의 자료형이 문자열(object)
>>> <class 'pandas.core.frame.DataFrame'>
>>> RangeIndex: 20 entries, 0 to 19
>>> Data columns (total 6 columns):
>>>  #   Column  Non-Null Count  Dtype 
>>> ---  ------  --------------  ----- 
>>>  0   Date    20 non-null     object
>>>  1   Close   20 non-null     int64 
>>>  2   Start   20 non-null     int64 
>>>  3   High    20 non-null     int64 
>>>  4   Low     20 non-null     int64 
>>>  5   Volume  20 non-null     int64 
>>> dtypes: int64(5), object(1)
>>> memory usage: 1.1+ KB
>>> None

# 문자열 데이터를 Timestamp로 변환
df['new_date'] = pd.to_datetime(df['Date'])

# 시계열 인덱스 지정 및 기존 열 삭제
df.set_index('new_Date', inplace = True)
df.drop('Date', axis = 1, inplace = True)
```

<br>

2. Period로 변환
* Period로 변환 : pd.to_period()을 이용

이 때 freq 옵션에 기준이 되는 기간을 설정하면 된다.
|옵션|의미|
|:---:|:---:|
|D|1일의 기간|
|M|1개월의 기간|
|A|1년의 기간|

```python
import pandas as pd

dates = ['2019-01-01', '2020-03-01', '2021-06-01']

# 문자열을 Timestamp로 변환
ts_dates = pd.to_datetime(dates)

# Timestamp를 Period로 변환
pr_day = ts_dates.to_period(freq = 'D')
pr_month = ts_dates.to_period(freq = 'M')
pr_year = ts_dates.to_period(freq = 'A')

print(pr_day)
print(pr_month)
print(pr_year)
>>> PeriodIndex(['2019-01-01', '2020-03-01', '2021-06-01'], dtype='period[D]')
>>> PeriodIndex(['2019-01', '2020-03', '2021-06'], dtype='period[M]')
>>> PeriodIndex(['2019', '2020', '2021'], dtype='period[A-DEC]')
```

___

## **6-2. 시계열 데이터 만들기**

1. Timestamp 배열
* Timestamp 배열 : date_range() 함수를 사용

```python
import pandas as pd

ts_ms = pd.date_range(start = '2019-01-01', # 날짜 범위 시작
                      end = None, # 날짜 범위 끝
                      periods = 6, # 생성할 timestamp 개수
                      freq = 'MS', # 시간 간격 (MS : 월의 시작일)
                      tz = 'Asia/Seoul') # 시간대(timezone)

print(ts_ms)
>>> DatetimeIndex(['2019-01-01 00:00:00+09:00', '2019-02-01 00:00:00+09:00',
>>>                '2019-03-01 00:00:00+09:00', '2019-04-01 00:00:00+09:00',
>>>                '2019-05-01 00:00:00+09:00', '2019-06-01 00:00:00+09:00'],
>>>               dtype='datetime64[ns, Asia/Seoul]', freq='MS')
```

이 때 freq 옵션에 `M`을 입력시 월의 마지막 날짜를 생성하고, `3M`을 입력시 3개월 간격의 마지막 날짜를 생성한다.

<br>

2. Period 배열
* Period 배열 : period_range()

```python
import pandas as pd

pr_m =  pd.period_range(start = '2019-01-01', # 날짜 범위 시작
                       end = None, # 날짜 범위 끝
                       periods = 3, # 생성할 period 개수
                       freq = 'M') # 기간의 길이(M : 월)

print(pr_m)
>>> PeriodIndex(['2019-01', '2019-02', '2019-03'], dtype='period[M]')
```

이 때 PeriodIndex의 원소 '2019-01'은 2019년 1월의 전체 기간을 의미한다. <br>
그리고, freq 옵션을 `H`로 하면 1시간 간격, `2H`로 하면 2시간 간격을 나타낸다.

___

## **6-3. 시계열 데이터 활용**

시계열 데이터를 활용은 날짜 데이터를 분리하거나, 날짜 인덱스를 활용할 때 많이 사용한다.

1. 날짜 데이터 분리
* 날짜 데이터 분리 : `dt 속성`을 이용하여 개별적 추출

연-월-일 날짜 데이터에서 일부를 분리하여 추출 가능하다. 

```python
import pandas as pd

df = pd.read_csv('./stock-data.csv')

df['new_Date'] = pd.to_datetime(df['Date'])

# dt 속성을 이용하여 new_Date 열의 연-월-일 정보를 년, 월, 일로 구분
df['Year'] = df[new_Date].dt.year
df['Month'] = df[new_Date].dt.month
df['Day'] = df[new_Date].dt.day

# Timestamp 객체를 Period 객체로 변환하는 to_period() 메소드를 적용하여, 연-월-일 중 연-월 또는 연을 추출
df['Date_yr'] = df['new_Date'].dt.to_period(freq = 'A')
df['Date_m'] = df['new_Date'].dt.to_period(freq = 'M')
```

<br>

2. 날짜 인덱스 활용

날짜 인덱스를 활용하면 시계열 데이터에 대한 인덱싱과 슬라이싱이 편리하다.

* 인덱싱과 슬라이싱을 이용해 필요한 날짜의 행만 추출
* 두 날짜 사이의 간격 구하기

```python
import pandas as pd

df = pd.read_csv('stock-data.csv')

# Timestamp 객체로 변환
df['new_Date'] = pd.to_datetime(df['Date'])

# 시계열 객체인 Timestamp 객체를 행 인덱스로 지정
df.set_index('new_Date', inplace = True)


# 1. 날짜 인덱스를 사용하여 연-월-일 중에서 필요로 하는 레벨을 선택적으로 선택 가능

df_y = df.loc['2018'] # 2018년인 행만 추출

df_ym = df.loc['2018-07'] # 2018년 7월 행만 추출

df_ymd_range = df.loc['2018-06-20':'2018-06-25'] # 날짜 범위 지정


# 2. 두 날짜 사이의 간격 구하기
today = pd.to_datetime('2018-12-25') # 기준일 생성
df['time_delta'] = today - df.index # 날짜 차이 계산
df.set_index('time_delta', inplace = True)
```
