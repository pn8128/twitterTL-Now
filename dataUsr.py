# -*- coding:utf-8 -*-
import twitter
import config

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
api = twitter.Api(CK, CS, AT, ATS)
usrName="@hogehoge"#ここにユーザー名を入れる

tweets=api.GetUserTimeline(screen_name=usrName,count=200,include_rts=False,exclude_replies=False)
text="".join([tweet.text for tweet in tweets])

dateS=tweets[0].created_at.split()
dateS=dateS[1:3]+dateS[3].split(":")
dateS[2]=str(int(dateS[2])+9)
dateS=dateS[0]+"-"+dateS[1]+" "+dateS[2]+":"+dateS[3]

for i in range(14):
    id=tweets[-1].id
    tweets=api.GetUserTimeline(screen_name=usrName,count=200,include_rts=False,max_id=id,exclude_replies=False)
    text+="".join([tweet.text for tweet in tweets])

dateE=tweets[0].created_at.split()
dateE=dateE[1:3]+dateE[3].split(":")
dateE[2]=str(int(dateE[2])+9)
dateE=dateE[0]+"-"+dateE[1]+" "+dateE[2]+":"+dateE[3]

with open("data.txt","w") as f:
    f.write(text)
