# 2. 판다스 자료구조
# 판다스는 시리즈(series)와 데이터프레임(dataframe)이라는 구조화된 데이터 형식을 제공
# 시리즈는 1차원 배열, 데이터프레임은 2차원 배열임


# 2-1. 시리즈
# 인덱스(index)는 데이터 값(value)과 일대일 대응이 됨 => 이러한 관점에서 딕셔너리와 비슷한 구조

# 시리즈 만들기 Series()
# 딕셔너리와 시리즈의 구조가 비슷하기 때문에 딕셔너리를 시리즈로 변환하는 방법을 많이 이용
# 즉, pandas.Series(딕셔너리)
# 이 때 Series()는 판다스 라이브러리의 내장함수
from __future__ import division
from audioop import mul
import pandas as pd # as pd는 pandas 대신 pd라는 약칭으로 부르는 것
dict_data = {'a':1, 'b':2, 'c':3}
sr = pd.Series(dict_data)
print(type(sr))
print(sr) # 인덱스는 왼쪽에, 데이터 값은 오른쪽에 출력됨

# 인덱스 구조
# 인덱스에는 [정수형 위치 인덱스], [인덱스 이름 또는 인덱스 라벨]이 있음
# 이 때 정수형 위치 인덱스는 리스트를 시리즈로 변환시키면 자동 지정됨
import pandas as pd
list_data = ['2019-01-02', 3.14, 'ABC', 100, True]
sr = pd.Series(list_data) # 리스트를 시리즈로
print(sr)
idx = sr.index # 인덱스만 저장
val = sr.values # 데이터 값만 저장
print(idx) # range index 객체로 범위의 마지막 값은 포함하지 않음
print(val) # 순서 유지

# 원소 선택
import pandas as pd
tup_data = ('영인', '2010-05-01', '여', True) 
sr = pd.Series(tup_data, index=['이름', '생년월일', '성별', '학생여부']) # 튜플을 시리즈로, 인덱스 옵션 지정
print(sr) # 자료형은 문자열(object)임
print(sr[0]) # (1) 원소 1개 선택
print(sr['이름']) # 두 결과 모두 영인을 돌려냄
print(sr[[1, 2]]) # (2) 여러 개의 원소 선택 (인덱스 자리에 리스트를 넣어줌)
print(sr[['생년월일', '성별']]) # 두 결과 모두 같음
print(sr[1:2]) # (3) 여러 개의 원소 선택 (인덱스 범위로 설정) => 정수형 위치 인덱스의 경우 범위의 끝 미포함
print(sr['생년월일':'성별']) # 인덱스 이름 사용시 범위의 끝이 포함


# 2-2. 데이터프레임
# 데이터프레임은 2차원 배열
# 여러 개의 시리즈들이 모여서 데이터프레임을 이루는 구조, 즉 데이터프레임의 열이 각각의 시리즈 객체
# 데이터프레임은 행과 열을 나타내기 위해 [행 인덱스], [열 이름]과 같이 2가지 종류의 주소 사용
# 행은 관측값, 열은 변수라고 생각하면 됨 !

# 데이터프레임 만들기
# 데이터프레임을 만들기 위해서는 같은 길이의 1차원 배열 여러 개가 필요
# 즉, 딕셔너리의 키가 열의 이름이 되고 딕셔너리의 값이 시리즈 배열이 됨
# DataFrame() 함수를 사용
# pandas.DataFrame(딕셔너리)
import pandas as pd
dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}
df = pd.DataFrame(dict_data) # 딕셔너리를 데이터프레임으로
print(type(df))
print(df) # 행 인덱스에는 정수형 위치 인덱스(0,1,2)가 자동 지정

# 행 인덱스 / 열 이름 설정
# 2차원 배열 형태의 데이터를 데이터프레임으로 변환하기 쉬움
# 2차원 배열 예시 : 리스트(튜플)에 리스트(튜플)을 원소로 가짐
# pandas.DataFrame(2차원 배열, index = 행 인덱스 배열, columns = 열 이름 배열)
import pandas as pd
df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']], index = ['준서', '예은'], columns = ['나이', '성별', '학교'])
print(df)
print(df.index) # 행 인덱스 
print(df.columns) # 열 이름
# 앞에서 딕셔너리를 이용했을 때에는 리스트가 열이 되었는데, 2차원 배열 형태는 리스트가 행이 되는 것에 주의

# 행 인덱스 / 열 이름 변경
# 행 인덱스 변경 : DataFrame 객체.index = 새로운 행 인덱스 배열
# 열 이름 변경 : DataFrame 객체.columns = 새로운 열 이름 배열
df.index = ['학생1', '학생2']
df.columns = ['연령', '남녀', '소속']
print(df)
print(df.index)
print(df.columns)

# 행 인덱스 / 열 인덱스 일부만 변경
# DataFrame의 rename 메서드를 이용
# 단, 원본 객체를 직접 수정하는 것이 아니라 새로운 데이터프레임 객체를 반환하는 것임
# 원본 객체를 변경하려면 inplace = True 옵션을 이용
# 행 인덱스 변경 : DataFrame 객체.rename(index={기존 인덱스: 새 인덱스, ...})
# 열 이름 변경 : DataFrame 객체.rename(columns={기존 이름: 새 이름, ...})
import pandas as pd
df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']], index = ['준서', '예은'], columns= ['나이', '성별', '학교'])
print(df)

df.rename(index = {'준서':'학생1', '예은':'학생2'}, inplace = True)
df.rename(columns = {'나이':'연령', '성별':'남녀', '학교':'소속'})
print(df)

# 행/열 삭제
# drop() 메서드 이용
# 행을 삭제할 때는 축 옵션으로 axis = 0, 열을 삭제할 때는 축 옵션으로 axis = 1
# 동시에 여러 개의 행 또는 열 삭제하려면 리스트 형태로 입력
# 행 삭제 : DataFrame 객체.drop(행 인덱스 또는 배열, axis = 0)
# 열 삭제 : DataFrame 객체.drop(열 이름 또는 배열, axis = 1)
# 1. 행 삭제
import pandas as pd
df = pd.DataFrame({'수학':[90, 80, 70], '영어':[98, 89, 95], '음악':[85, 95, 100], '체육':[100, 90, 90]}, index = ['서준', '우현', '인아'])
print(df)
df2 = df[:] # df를 복제하여 df2를 만듦
df2.drop('우현', inplace = True) # 행 삭제
print(df2)
df3 = df[:] # df를 복제하여 df3를 만듦
df3.drop(['우현', '인아'], axis = 0, inplace = True) # 여러 개의 행 삭제, 돌려낸 객체를 기존 변수에 저장
print(df3)
# 2. 열 삭제 (반드시 axis = 1 옵션을 입력해주어야 함, 누락하면 오류 메시지 출력)
import pandas as pd
df = pd.DataFrame({'수학':[90, 80, 70], '영어':[98, 89, 95], '음악':[85, 95, 100], '체육':[100, 90, 90]}, index = ['서준', '우현', '인아'])
df4 = df.copy() # df[:] 과 같음
df4.drop('수학', axis = 1, inplace = True) # 1개의 열 삭제
df5 = df.copy()
df5.drop(['영어', '음악'], axis = 1, inplace = True) # 2개의 열 삭제
print(df4)
print(df5)

# 행 선택
# loc, iloc 인덱서를 사용
# 인덱스 이름을 기준으로 행 선택시 loc, 정수형 위치 인덱스를 사용할 때 iloc
# 두 가지 방법 다 범위 지정은 가능하지만 iloc는 범위의 끝이 제외됨
import pandas as pd
df = pd.DataFrame({'수학':[90, 80, 70], '영어':[98, 89, 95], '음악':[85, 95, 100], '체육':[100, 90, 90]}, index = ['서준', '우현', '인아'])
label1 = df.loc['서준'] # 1개의 행 선택, 인덱스 이름 이용
position1 = df.iloc[0] # 1개의 행 선택, 정수형 위치 인덱스 이용
print(label1) # 시리즈 객체가 반환됨
print(position1) # 두 결과가 같음
label2 = df.loc[['서준', '우현']] # 2개의 행 선택, 리스트 이용
position2 = df.iloc[[0, 1]] # 2개의 행 선택
print(label2)
print(position2) # 두 결과가 같음
label3 = df.loc['서준':'우현'] # 범위를 이용한 행 선택(슬라이싱), 범위의 끝 값이 포함됨
position3 = df.iloc[0:1] # 범위를 이용한 행 선택(슬라이싱), 범위의 끝 값이 포함되지 않음
print(label3)
print(position3) # 두 결과가 다름

# 열 선택
# 1개의 열만 선택 : DataFrame 객체["열 이름"] 또는 DataFrame 객체.열이름, 2번째 방법은 열 이름이 문자열일 경우에만 가능 => 반환되는 객체는 시리즈 객체
# 2개 이상의 열 추출 : DataFrame 객체[['열 이름1', '열 이름2', ...]] => 반환되는 객체는 시리즈 객체
# 열 이름 1개를 원소로 갖는 리스트를 사용하는 경우에도 시리즈가 아닌 데이터프레임 반환 (ex) df[['수학']]
# 1. 1개의 열만 추출하는 경우
import pandas as pd
df = pd.DataFrame({'이름':['서준', '우현', '인아'], '수학':[90, 80, 70], '영어':[98, 89, 95], '음악':[85, 95, 100], '체육':[100, 90, 90]})
math1 = df['수학']
print(math1)
print(type(math1)) # type은 시리즈 객체
english = df.영어
print(english)
print(type(english)) # type은 시리즈 객체
# 2. 2개 이상의 열을 추출하는 경우
music_gym = df[['음악', '체육']]
print(music_gym)
print(type(music_gym)) # type은 데이터프레임
math2 = df[['수학']]
print(math2)
print(type(math2)) # type은 데이터프레임

# 범위 슬라이싱의 고급 활용
# DataFrame 객체.iloc[시작인덱스 : 끝인덱스 : 슬라이싱간격]
# 1. 2개의 간격으로 슬라이싱
import pandas as pd
df = pd.DataFrame({'이름':['서준', '우현', '인아'], '수학':[90, 80, 70], '영어':[98, 89, 95], '음악':[85, 95, 100], '체육':[100, 90, 90]})
print(df.iloc[::2]) # 서준, 인아만 선택됨
print(df.iloc[0:3:2]) # 위와 같음
# 2. 역순으로 인덱싱
print(df.iloc[::-1])

# 원소 선택
# 데이터프레임의 행 인덱스와 열 이름을 [행, 열] 형식의 2차원 좌표로 입력하여 원소 위치 지정
# 행 1개 + 열 2개 or 행 2개 + 열 1개 => 시리즈 객체 반환
# 행 2개 이상 + 열 2개 이상 => 데이터프레임 객체 반환
# 인덱스 이름인 경우 : DataFrame 객체.loc[행 인덱스, 열 이름]
# 정수 위치 인덱스인 경우 : DataFrame 객체.iloc[행 번호, 열 번호]
# set_index() : 행 인덱스로 지정
import pandas as pd
exam_data = {'이름':['서준', '우현', '인아'], '수학':[90, 80, 70], '영어':[98, 89, 95], '음악':[85, 95, 100], '체육':[100, 90, 90]}
df = pd.DataFrame(exam_data)
df.set_index('이름', inplace = True) # '이름' 열을 새로운 인덱스로 지정
print(df)
# 원소 1개 선택
a = df.loc['서준', '음악'] # 행 인덱스가 '서준', 열 이름이 '음악'인 원소 선택
print(a)
b = df.iloc[0, 2] # 위와 같음
print(b)
# 원소 2개 이상 선택
c = df.loc['서준', ['음악', '체육']]
print(c)
d = df.iloc[0, [2, 3]]
print(d)
e = df.loc['서준', '음악':'체육']
print(e)
f = df.iloc[0, 2:]
print(f) # 시리즈 객체
g = df.loc[['서준', '우현'], ['음악', '체육']]
print(g)
h = df.iloc[[0, 1], [2, 3]]
print(h)
i = df.loc['서준':'우현', '음악':'체육']
print(i)
j = df.iloc[0:2, 2:]
print(j) # 데이터프레임 객체
k = df.loc[:, ['음악', '체육']] # 모든 행 선택
print(k)
l = df.iloc[:, [2, 3]] # 모든 행 선택
print(l)
m = df.iloc[:, 2:4] # 위와 같음
print(m)

# 열 추가 : DataFrame 객체['추가하려는 열 이름'] = 데이터 값
# 이 때 모든 행에 동일한 값이 입력됨을 유의
import pandas as pd
exam_data = {'이름':['서준', '우현', '인아'], '수학':[90, 80, 70], '영어':[98, 89, 95], '음악':[85, 95, 100], '체육':[100, 90, 90]}
df = pd.DataFrame(exam_data)
print(df)
df['국어'] = 80 # '국어'라는 열 추가, 그러나 데이터 값은 80으로 모두 같음
print(df)

# 행 추가 : DataFrame.loc['새로운 행 이름'] = 데이터 값 (또는 배열)
# 추가하려는 행 이름과 데이터 값을 loc 인덱서를 사용하여 입력
# 하나의 데이터 값을 입력하거나, 열의 개수에 맞게 배열 형태로 여러 개의 값을 입력 가능
# 기존 행을 복사해서 새로운 행에 그대로 추가할수도 있음
# 기존 인덱스와 중복되는 경우 새로운 행을 추가하는 것이 아니라 기존 행의 원소값을 변경
# 행 인덱스 지정 시, 기존 인덱스의 순서를 따르지 않아도 됨 (ex) 현재 2번 인덱스까지 있는 경우, df.loc[10] = 0을 해도 됨 (행 인덱스는 3이 아닌 10이 되는 것)
import pandas as pd
exam_data = {'이름':['서준', '우현', '인아'], '수학':[90, 80, 70], '영어':[98, 89, 95], '음악':[85, 95, 100], '체육':[100, 90, 90]}
df = pd.DataFrame(exam_data)
print(df)
df.loc[3] = 0 # 새로운 행 추가, 같은 원소 값 입력
print(df)
df.loc[4] = ['동규', 90, 80, 70, 60] # 새로운 행 추가, 원소 값 여러 개의 배열 입력
print(df)
df.loc['행5'] = df.loc[3] # 새로운 행 추가, 기존 행 복사
print(df) 

# 원소 값 변경
# DataFrame 객체의 일부분 또는 원소를 선택 = 새로운 값
# 특정 원소 선택 후, 새로운 데이터 값 지정해주면 됨
# 데이터프레임 인덱싱과 슬라이싱 기법 이용
import pandas as pd
exam_data = {'이름':['서준', '우현', '인아'], '수학':[90, 80, 70], '영어':[98, 89, 95], '음악':[85, 95, 100], '체육':[100, 90, 90]}
df = pd.DataFrame(exam_data)
print(df)
df.set_index('이름', inplace = True)
print(df)
df.iloc[0][3] = 80 # '서준'의 '체육' 점수를 80으로 변경
print(df)
df.loc['서준']['체육'] = 90 # '서준'의 '체육' 점수를 90으로 변경
print(df)
df.loc['서준', '체육'] = 100 # '서준'의 '체육' 점수를 100으로 변경
print(df)
# 여러 개의 원소를 선택하여 새로운 값 할당 시, 모든 원소가 한꺼번에 같은 값으로 변경
# 아니면 선택한 원소의 개수에 맞춰 각기 다른 값을 배열 형태로 입력 가능
df.loc['서준', ['음악', '체육']] = 50
print(df)
df.loc['서준', ['음악', '체육']] = 100, 50
print(df)

# 행, 열의 위치 바꾸기
# 선형대수학의 전치행렬과 같은 개념
# DataFrame 객체.transpose() / DataFrame 객체.T
# 전치의 결과로 새로운 객체를 반환하므로, 기존 객체 변경하기 위해서는 할당 필요
import pandas as pd
exam_data = {'이름':['서준', '우현', '인아'], '수학':[90, 80, 70], '영어':[98, 89, 95], '음악':[85, 95, 100], '체육':[100, 90, 90]}
df = pd.DataFrame(exam_data)
print(df)
df = df.transpose() # 데이터프레임 전치 후 할당
print(df)
df = df.T # 데이터프레임 다시 전치, 원래대로 돌아옴
print(df)





# 3. 인덱스 활용

# 특정 열을 행 인덱스로 설정
# set_index() 메서드를 사용하여 데이터 프레임의 특정 열을 행 인덱스로 설정
# 단, 원본 데이터프레임을 바꾸지 않고 새로운 데이터프레임 객체를 반환하는 점에 유의
# 원래 변수에 할당하기 위해서는 다시 할당을 해주거나, inplace 옵션 이용
# DataFrame 객체.set_index(['열 이름'] 또는 '열 이름')
# 2개의 열을 행 인덱스로 지정 가능 => 멀티인덱스(multiindex)
import pandas as pd
exam_data = {'이름':['서준', '우현', '인아'], '수학':[90, 80, 70], '영어':[98, 89, 95], '음악':[85, 95, 100], '체육':[100, 90, 90]}
df = pd.DataFrame(exam_data)
print(df)
ndf = df.set_index(['이름'])
print(ndf)
ndf2 = ndf.set_index('음악')
print(ndf2)
ndf3 = ndf.set_index(['수학', '음악']) # 2개의 열을 행 인덱스로 지정 가능
print(ndf3)

# 행 인덱스 재배열
# reindex() 메서드를 사용하면 데이터프레임의 행 인덱스를 새로운 배열로 재지정 가능
# DataFrame 객체.reindex(새로운 배열)
import pandas as pd
dict_data = {'c0':[1, 2, 3], 'c1':[4, 5, 6], 'c2':[7, 8, 9], 'c3':[10, 11, 12], 'c4':[13, 14, 15]}
df = pd.DataFrame(dict_data, index = ['r0', 'r1', 'r2']) # 행 인덱스를 'r0', 'r1', 'r2'로 지정
print(df)
new_index = ['r0', 'r1', 'r2', 'r3', 'r4']
ndf = df.reindex(new_index) # 행 인덱스를 새로운 배열로 재지정
print(ndf) # 'r3', 'r4' 인덱스에 해당하는 모든 열에 대해 NaN 값이 입력됨
ndf2 = df.reindex(new_index, fill_value = 0) # fill_value 옵션 이용하여 NaN값을 숫자 0으로 채우기
print(ndf2)

# 행 인덱스 초기화
# reset_index 메서드를 활용하여 행 인덱스를 정수형 위치 인덱스로 초기화
# 기존 행 인덱스는 열로 이동함
# DataFrame 객체.reset_index()
import pandas as pd
dict_data = {'c0':[1, 2, 3], 'c1':[4, 5, 6], 'c2':[7, 8, 9], 'c3':[10, 11, 12], 'c4':[13, 14, 15]}
df = pd.DataFrame(dict_data, index = ['r0', 'r1', 'r2'])
print(df)
ndf = df.reset_index()
print(ndf)

# 행 인덱스를 기준으로 데이터프레임 정렬
# sort_index() 메서드를 활용하여 행 인덱스를 기준으로 데이터프레임의 값을 정렬
# ascending 옵션을 사용하여 오름차순 또는 내림차순을 설정
# DataFrame 객체.sort_index()
import pandas as pd
dict_data = {'c0':[1, 2, 3], 'c1':[4, 5, 6], 'c2':[7, 8, 9], 'c3':[10, 11, 12], 'c4':[13, 14, 15]}
df = pd.DataFrame(dict_data, index = ['r0', 'r1', 'r2'])
print(df)
ndf = df.sort_index(ascending = False) # 내림차순으로 행 인덱스 정렬
print(ndf)

# 특정 열의 데이터 값을 기준으로 데이터프레임 정렬하기
# DataFrame 객체.sort_values()
import pandas as pd
dict_data = {'c0':[1, 2, 3], 'c1':[4, 5, 6], 'c2':[7, 8, 9], 'c3':[10, 11, 12], 'c4':[13, 14, 15]}
df = pd.DataFrame(dict_data, index = ['r0', 'r1', 'r2'])
print(df)
ndf = df.sort_values(by = 'c1', ascending = False) # 'c1' 열을 기준으로 내림차순 정렬, by 옵션을 이용
print(ndf)





# 4. 산술연산
# 판다스 객체의 산술연산은 내부적으로 3단계 프로세스를 거침
# (1) 행/열 인덱스를 기준으로 모든 원소를 정렬
# (2) 동일한 위치에 있는 원소끼리 일대일로 대응
# (3) 일대일 대응이 되는 모든 원소끼리 연산을 처리 (단, 이 때 대응되는 원소가 없으면 NaN으로 처리)

# 4-1. 시리즈 연산
# 시리즈 객체에 어떤 숫자를 더하면 개별 원소에 각각 숫자를 더하고 결과를 시리즈 객체로 반환
# 덧셈, 뺄셈, 곱셈, 나눗셈 모두 가능
import pandas as pd
student1 = pd.Series({'국어':100, '영어':80, '수학':90})
print(student1)
percentage = student1 / 200
print(percentage)
print(type(percentage)) # 객체 타입은 시리즈

# 시리즈 vs 시리즈
# 시리즈의 모든 인덱스에 대하여 같은 인덱스를 가진 원소끼리 계산
# 판다스는 인덱스 순서가 달라도 같은 인덱스를 찾아 정렬한 후 계산함
# 두 시리즈에 대해 사칙연산 수행
import pandas as pd
student1 = pd.Series({'국어':100, '영어':80, '수학':90})
student2 = pd.Series({'수학':80, '국어':90, '영어':80})
print(student1)
print(student2)
addition = student1 + student2
subtraction = student1 - student2
multiplication = student1 * student2
division = student1 / student2
print(type(division)) # 객체 타입은 시리즈
result = pd.DataFrame([addition, subtraction, multiplication, division], index = ['덧셈', '뺄셈', '곱셈', '나눗셈']) # 사칙연산 결과를 데이터프레임으로 합치기
print(result)
# 두 시리즈의 원소 개수 다르거나 / 시리즈의 크기가 같더라도 인덱스 값이 다르거나 / 어느 한 쪽의 데이터가 NaN인 경우 => NaN으로 처리함
import pandas as pd
import numpy as np
student1 = pd.Series({'국어':np.nan, '영어':80, '수학':90})
student2 = pd.Series({'수학':80, '국어':90})
print(student1)
print(student2)
addition = student1 + student2
subtraction = student1 - student2
multiplication = student1 * student2
division = student1 / student2
result = pd.DataFrame([addition, subtraction, multiplication, division], index = ['덧셈', '뺄셈', '곱셈', '나눗셈'])
print(result)

# 연산 메소드
# NaN을 피하기 위해서는 연산 메소드에 full_value 옵션을 설정한다.
import pandas as pd
import numpy as np
student1 = pd.Series({'국어':np.nan, '영어':80, '수학':90})
student2 = pd.Series({'수학':80, '국어':90})
print(student1)
print(student2)
sr_add = student1.add(student2, fill_value = 0)
sr_sub = student1.sub(student2, fill_value = 0)
sr_mul = student1.mul(student2, fill_value = 0)
sr_div = student1.div(student2, fill_value = 0)
result = pd.DataFrame([sr_add, sr_sub, sr_mul, sr_div], index = ['덧셈', '뺄셈', '곱셈', '나눗셈'])
print(result)


# 4-2. 데이터프레임 연산

# 데이터프레임 vs 숫자
# 시리즈와 동일
import pandas as pd
import seaborn as sns # Seaborn 라이브러리에서 제공하는 데이터셋 중 titanic 사용
titanic = sns.load_dataset('titanic') # load_dataset 함수로 데이터셋 불러옴
df = titanic.loc[:, ['age', 'fare']]
print(df.head()) # 첫 5행만 표시
addition = df + 10
print(addition.head())

# 데이터프레임 vs 데이터프레임
# 각 데이터프레임의 같은 행, 같은 열 위치에 있는 원소끼리 계산
# 동일한 위치의 원소끼리 계산한 결과값을 원래 위치에 다시 입력하여 데이터프레임을 만듦
# 어느 한 쪽에 원소가 존재하지 않거나 NaN이면 연산 결과는 NaN으로 처리됨
import pandas as pd
import seaborn as sns # Seaborn 라이브러리에서 제공하는 데이터셋 중 titanic 사용
titanic = sns.load_dataset('titanic') # load_dataset 함수로 데이터셋 불러옴
df = titanic.loc[:, ['age', 'fare']]
print(df.tail())
addition = df + 10
print(addition.head())
subtraction = addition - df # 데이터프레임끼리 연산
print(subtraction.tail())
