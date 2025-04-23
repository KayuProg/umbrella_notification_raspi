import socket
import gc
import time
from datetime import datetime
################# 音声ファイル作成 #######################
import os
from gtts import gTTS

def make_audio(text):
    japanese=text
    tts = gTTS(japanese, lang='ja')
    tts.save("/home/kayu/Desktop/umbrella_notification_raspi/audio/readaloud.mp3")
    print("making audio finish")

#########################################################
# Scraping cython使ってますがあまり早くなってません．
#########################################################
import scraping 
import pytz

def make_text():
    result=scraping.scrape()
    print("scraping finish")

    text_time=[]
    text_umb=None

    if (result['yowa']!=None or result['ame']!=None or result['tuyo']!=None or result['gou']!=None):
        text_umb="今日は傘を持っていきましょう．"
    elif result['ko']!=None and (result['yowa']==None and result['ame']==None and result['tuyo']==None and result['gou']==None):
        text_umb="今日は折り畳み傘を持っていきましょう．"
    elif not any(result):
        text_umb="今日は傘を持って行かなくて大丈夫です．"
    print(result)
    keys=list(result.keys())
    
    jst = pytz.timezone('Asia/Tokyo')
    now_hour = int(datetime.now(jst).hour)
    #now_hour=int(datetime.now().hour)
    print(now_hour)

    for key in keys:
        time=None
        if result[key]!=None:
            #現在以降の天気を反映させる
            #っていうのを辞めた．
            if key=="ko":
                # if  result["ko"]>=now_hour:
                time=str(result["ko"])+"時から小雨．"
            elif key=="yowa":
                # if  result["yowa"]>=now_hour:                
                time=str(result["yowa"])+"時から弱雨．"
            elif key=="ame":
                # if  result["ame"]>=now_hour:
                time=str(result["ame"])+"時から雨．"
            elif key=="tuyo":
                # if  result["tuyo"]>=now_hour:
                time=str(result["tuyo"])+"時から強い雨．"
            elif key=="gou":
                # if  result["gou"]>=now_hour:
                time=str(result["gou"])+"時から豪雨．"
            if time != None:
                text_time.append(time)
                
    print(text_time)
    
    if text_umb==None:
        text_full=("今日は傘を持っていく必要はありません．")
    elif text_umb != None and text_time==[]:
        text_full=text_umb
    else:
        text_full=text_umb+''.join(text_time)+"です．"
    print("text making finish")
    print("text is ",text_full)
    return text_full


def task1():#audioの作成まで行う．
     text_full=make_text()
     make_audio(text_full)
     gc.collect()#ガベージコレクションの強制実行


if __name__=="__main__":
    task1()
