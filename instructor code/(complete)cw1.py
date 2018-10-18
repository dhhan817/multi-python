# -*- coding: utf-8 -*-
"""
트위터 크롤링 테스트
"""

import tweepy

# 트위터 앱의 Keys and Access Tokens 탭 참조
# 앞서 저장했던 자신의 설정 값을 넣어준다
consumer_key = ""
consumer_secret = ""

# 1. 인증요청(1차) : 개인 앱 정보 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

access_token = ""
access_token_secret= ""

# 2. access 토큰 요청(2차) - 인증요청 참조변수 이용
auth.set_access_token(access_token, access_token_secret)

# 3. twitter API 생성  
api = tweepy.API(auth)

keyword = "쯔위";     # 자신이 검색하고 싶은 키워드 입력 
search = [] # 크롤링 결과 저장할 변수   

cnt = 1
while(cnt <= 10):   # 10page 대상으로 크롤링
   tweets = api.search(keyword)
   for tweet in tweets:
       search.append(tweet)
   cnt += 1

print(len(search)) # 문서 길이 
print(search[0]) # 첫번째 text 보기 


#전체 문서 보기

data = {}   # 전체 문서 추가
i = 0       # 문서 번호
for tweet in search:
    data['text'] = tweet.text   # text키에 text문서 저장
    print(i, " : ", data)   # 문서번호 : 문서내용
    i += 1

import os

# 쓰기 모드. 인코딩 설정 utf-8
wfile = open(os.getcwd()+"/twitter.txt", mode='w', encoding='utf-8')   
data = {}   # 전체 문서 추가
i = 0       # 문서 번호

for tweet in search:
    data['text'] = tweet.text   # text키에 text문서 저장
    wfile.write(data['text']+'\n')  # 파일 출력
    i += 1
wfile.close()
