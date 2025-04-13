import socket
import gc
import os
import time
import logging
from playsound3 import playsound
#import pygame.mixer#audio mixer
#pygame.mixer.init()
#pygame.mixer.music.set_volume(1)


# ログ設定
# logging.basicConfig(
#     filename='/home/kayu/Desktop/weather/main.log',  # ログを記録するファイル名
#     level=logging.INFO,  # 記録するログのレベル（DEBUG, INFO, WARNING, ERROR, CRITICAL）
#     format='%(asctime)s - %(levelname)s - %(message)s',  # ログメッセージのフォーマット
# )

# logging.info("this is run by bash")
#########################################################
# TCP connection
#########################################################
flag=0
def pico_connect():
    # HOST = '192.168.0.12'  # Raspberry PiのIPアドレス
    PORT = 51028           # クライアントと同じポート番号
    HOST = '0.0.0.0'

    # ソケットの設定
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # sock.bind((HOST, PORT))
    # sock.listen(1)


    try:
        # logging.info("binding")
        sock.bind((HOST, PORT))
        # logging.info("binded")
        sock.listen(1)
    except Exception as e:
        # logging.info(f"Error binding socket: {e}")
        pass

    # logging.info("waitng for a pico w connection")
    print('Waiting for a pico w connection...')
    global flag
    if flag==0:
        # from playsound3 import playsound        
        #playsound("./audio/notice.mp3")
        #pygame.mixer.music.set_volume(1)
        #os.system("amixer sset Master 100%+")
        os.system("/usr/bin/mplayer -speed 1.1 -volume 80 -af scaletempo /home/kayu/Desktop/umbrella_notification_raspi/audio/notice.mp3")
    
        flag=1

    # 接続の確立
    conn, addr = sock.accept()
    print(f'Connected by {addr}')
    # logging.info(f'Connected by {addr}')


    #pico wからスクレイピングのflagもらう
    # データの受信
    print("waiting for pico w receiving data...")
    # logging.info("waiting for pico w receiving data...")

    while True:
        data = conn.recv(1024)
        # if not data:
        #     print("data error")
        #     break
        # 受信データをデコード
        message = data.decode('utf-8')

        if message=="Read aloud" :
            break
        time.sleep(0.5)


    # ソケットを閉じる
    sock.close()
    conn.close()



#########################################################
# Reading aloud cythonで読み上げは遅い
#########################################################

################# Japanese ###################
def read_aloud():
    # logging.info("trying to read aloud")
    # from playsound3 import playsound        
    # playsound(r"audio/readaloud.mp3")
    #pygame.mixer.music.set_volume(0.1)
    os.system("/usr/bin/mplayer -speed 1.1 -volume 80 -af scaletempo /home/kayu/Desktop/umbrella_notification_raspi/audio/readaloud.mp3")
  

    # # mixerモジュールの初期化
    # pygame.mixer.init()
    # # 音楽ファイルの読み込み
    # pygame.mixer.music.load("/home/kayu/Desktop/weather/audio/readaloud.mp3")
    # # 音楽再生、および再生回数の設定(-1はループ再生)
    # pygame.mixer.music.play(1)

    # time.sleep(5)
    # # 再生の終了
    # pygame.mixer.music.stop()
    # logging.info("read aloud end")

# ################# English ###################
# english='Japan\'s Health Ministry updated its Q&A page. You can find answers to such questions as how you can avoid catching/spreading the virus, what is the "cough etiquette". '
# tts = gTTS(english, lang='en')
# tts.save("./audio/english.mp3")
# os.system("mplayer ./audio/english.mp3")


################# mei ###################
# import subprocess

# # textfile
# TEXT_FILE = "a.txt"

# # openjtalk
# X_DIC = '/var/lib/mecab/dic/open-jtalk/naist-jdic'
# # M_VOICE = '/usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice'
# # M_VOICE = '/usr/share/hts-voice/htsvoice-tohoku-f01-master/htsvoice-tohoku-f01-master/tohoku-f01-angry.htsvoice'# neutral happy angry sad
# M_VOICE = '/usr/share/hts-voice/mei/mei_normal.htsvoice' # angry happy sad bashful normal
# R_SPEED = '1.0'
# OW_WAVFILE = '/tmp/tmp.wav'

# # aplay
# # CARD_NO = 1
# # DEVICE_NO = 0

# def talk_text(t):
#     open_jtalk = ['open_jtalk']
#     xdic = ['-x', X_DIC]
#     mvoice = ['-m', M_VOICE]
#     rspeed = ['-r', R_SPEED]
#     owoutwav = ['-ow',OW_WAVFILE]
#     cmd = open_jtalk + xdic + mvoice + rspeed + owoutwav
#     c = subprocess.Popen(cmd, stdin=subprocess.PIPE)
#     c.stdin.write(t.encode('utf-8'))
#     c.stdin.close()
#     c.wait()
# #   aplay = ['aplay', '-q', OW_WAVFILE, ('-Dplughw:'+str(CARD_NO)+','+str(DEVICE_NO))]
#     aplay = ['aplay', '-q', OW_WAVFILE]
#     wr = subprocess.Popen(aplay)
#     wr.wait()

# def main():
#     with open(TEXT_FILE) as f:
#         for line in f:
#             talk_text("今日ははれ")

# if __name__ == '__main__':
#     main()


#################################
# 実行
#################################
import schedule
from datetime import datetime




def task2():#接続を待って読み上げまで
    # logging.info("connect successful")
    read_aloud()



while True:
    # logging.info("\ntask2 start")
    pico_connect()

    # print(f"Received: {message}")
    task2()
    # logging.info("task2 end")
    # if datetime.now().hour==3:
    #     break#毎朝3時でmain.py終了
