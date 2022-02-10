# 마민경님

# 1번
a = 30
b = 17
print(a // b) # 몫
print(a % b) # 나머지

# 2번
x = "world Hello"
print(x[6:] + " " + x[:5])

# 3번
a = "That's pretty good idea"
print(a.upper())

# 4번
a = "Hi"
print(a * len(a))

### 5번
a = "http://naver.com"
print("{}".format(a[7:]) + "의 비밀번호는 " + a[7:][:3] + "{}". format(len(a[7:12])) + "{}".format(a.count("e"))+ "!" + "입니다.")


# 구남이님

# 1번
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]

# 2번
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
movie_rank.append("배트맨")
print(movie_rank)

# 3번
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)

# 4번
movie_rank.remove("럭키")

# 5번
t1 = (1,)
print(t1)

# 6번
# 튜플은 바꿀 수 없는 자료형이기 때문에 오류가 발생함.


# 강수민님

# 1번
close_price_daeshin = [10000, 10500, 10300, 10700, 11100]
print((close_price_daeshin[0]+close_price_daeshin[1]+close_price_daeshin[2]+close_price_daeshin[3]+close_price_daeshin[4])/5)

# 2번
nums = [1, 2, 3, 4, 5]
nums[3:5] = []
print(nums)

# 3번
items = ['000600', '034560', '003540', '039490']
print(";".join(items))

# 4번
mystr = "13"
print("{0:0>5}" .format(mystr))

# 5번
a = {'A':90, 'B':80}
print(a.get('C',70))