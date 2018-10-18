# -*- coding: utf-8 -*-
"""
트위터 크롤링 테스트
"""

import tweepy

# 트위터 앱의 Keys and Access Tokens 탭 참조
# 앞서 저장했던 자신의 설정 값을 넣어준다
consumer_key = "YOUR_OWN_CONSUMER_KEY"
consumer_secret = "YOUR_OWN_CONSUMER_SECRET_KEY"

# 1. 인증요청(1차) : 개인 앱 정보 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

access_token = "YOUR_OWN_ACCESS_TOKEN"
access_token_secret= "YOUR_OWN_ACCESS_TOKEN_SECRET"

# 2. access 토큰 요청(2차) - 인증요청 참조변수 이용
auth.set_access_token(access_token, access_token_secret)

# 3. twitter API 생성  
api = tweepy.API(auth)

keyword = "쯔위";     # 자신이 검색하고 싶은 키워드 입력 
search = [] # 크롤링 결과 저장할 변수   

cnt = 1
while(cnt <= 10):
    tweets = api.search(keyword)
    for tweet in tweets:
        search.append(tweet)
    cnt += 1

print(len(search)) # 문서 길이 
print(search[0]) # 첫번째 text 보기 


#전체 문서 보기

data = {}
i = 0
for tweet in search:
    data['text'] = tweet.text
    print(i, ":", data)
    i += 1
    
    
#파일에 쓰기
import os

os.chdir("C:/Users/student/Desktop/multicamplus/multi-python/code")
wfile = open("C:/Users/student/Desktop/multicamplus/multi-python/code" + "/twitter.txt", mode="w", encoding="utf-8")
data = {}
i = 0

for tweet in search:
    data['text'] = tweet.text
    wfile.write(str(i) + ": " + data['text'] + '\n')
    i += 1
    
wfile.close()