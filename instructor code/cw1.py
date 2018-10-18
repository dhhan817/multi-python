# -*- coding: utf-8 -*-
"""
트위터 크롤링 테스트
"""

import tweepy

# 트위터 앱의 Keys and Access Tokens 탭 참조
# 앞서 저장했던 자신의 설정 값을 넣어준다
consumer_key = "..."
consumer_secret = "..."

# 1. 인증요청(1차) : 개인 앱 정보 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

access_token = "..."
access_token_secret= "..."

# 2. access 토큰 요청(2차) - 인증요청 참조변수 이용
#TODO

# 3. twitter API 생성  
#TODO

keyword = "방탄소년";     # 자신이 검색하고 싶은 키워드 입력 
search = [] # 크롤링 결과 저장할 변수   

cnt = 1
#TODO

print(len(search)) # 문서 길이 
print(search[0]) # 첫번째 text 보기 


#전체 문서 보기

#TODO


