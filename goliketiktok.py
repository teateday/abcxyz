import json
import requests,os,time
import socket
from time import strftime
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import time
import sys

banner = """
\033[1;35m █████╗ ███╗   ██╗██╗  ██╗████████╗██╗   ██╗ █████╗ ███╗   ██╗
\033[1;37m██╔══██╗████╗  ██║██║  ██║╚══██╔══╝██║   ██║██╔══██╗████╗  ██║
\033[1;35m███████║██╔██╗ ██║███████║   ██║   ██║   ██║███████║██╔██╗ ██║
\033[1;37m██╔══██║██║╚██╗██║██╔══██║   ██║   ██║   ██║██╔══██║██║╚██╗██║
\033[1;35m██║  ██║██║ ╚████║██║  ██║   ██║   ╚██████╔╝██║  ██║██║ ╚████║
\033[1;37m╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝
\033[1;31m────────────────────────────────────────────────────────────
\033[1;31m[\033[1;37mTAT07\033[1;31m] \033[1;37m=> \033[1;33mTOOL GOLIKE TIKTOK V1
\033[1;31m[\033[1;37mTAT07\033[1;31m] \033[1;37m=> \033[1;35mADMIN: \033[1;36mTRAN ANH TUAN
\033[1;31m[\033[1;37mTAT07\033[1;31m] \033[1;37m=> \033[1;32mCLTX - TELE: \033[1;37mhttps://kingtele.sbs
\033[1;31m[\033[1;37mTAT07\033[1;31m] \033[1;37m=> \033[1;34mYOUTUBE: \033[1;37m [Update]
\033[97m════════════════════════════════════════════════
"""
os.system('cls' if os.name== 'nt' else 'clear')
for x in banner:
  print(x,end = "")
  sleep(0.001)
try:
  Authorization = open("Authorization.txt","x")
  t = open("token.txt","x")
except:
  pass
Authorization = open("Authorization.txt","r")
t = open("token.txt","r")
author = Authorization.read()
token = t.read()
if author == "":
  author = input("\033[1;95m[TAT07] => NHẬP AUTHORIZATION : ")
  token = input("\033[1;33m[TAT07] => NHẬP T : ")
  Authorization = open("Authorization.txt","w")
  t = open("token.txt","w")
  Authorization.write(author)
  t.write(token)
else:
  select = input("\033[1;95m[TAT07] => \033[1;93m Nhấn Enter Để Bỏ Qua \n\033[1;95m╚⟩⟩⟩ Nhập AUTHORIZATION: ")

  if select != "":
    author = select
    token = input("\033[1;95m[TAT07] => Nhập T : ")
    Authorization = open("Authorization.txt","w")
    t = open("token.txt","w")
    Authorization.write(author)
    t.write(token)
Authorization.close()
os.system('cls' if os.name== 'nt' else 'clear')
t.close()
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json;charset=utf-8',
    'Authorization': author,
    't': token,
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'Referer': 'https://app.golike.net/account/manager/tiktok',
}


def chonacc():
  json_data = {}

  response = requests.get('https://gateway.golike.net/api/tiktok-account', headers=headers, json=json_data).json()
  return response
def nhannv(account_id):

  params = {
    'account_id': account_id,
    'data': 'null',
  }

  json_data = {}

  response = requests.get('https://gateway.golike.net/api/advertising/publishers/tiktok/jobs',params=params,headers=headers,json=json_data,).json()
  return response
def hoanthanh(ads_id,account_id):
  json_data = {
    'ads_id': ads_id,
    'account_id': account_id,
    'async': True,
    'data': None,
  }

  response = requests.post(
    'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',
    headers=headers,
    json=json_data,
  ).json()
  return response
def baoloi(ads_id,object_id,account_id,loai):
  json_data1 = {
    'description': 'Tôi đã làm Job này rồi',
    'users_advertising_id': ads_id,
    'type': 'ads',
    'provider': 'tiktok',
    'fb_id': account_id,
    'error_type': 6,
  }

  response = requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data1).json()

  json_data = {
    'ads_id': ads_id,
    'object_id': object_id,
    'account_id': account_id,
    'type': loai,
  }

  response = requests.post(
    'https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',
    headers=headers,
    json=json_data,
  ).json()  
chontktiktok = chonacc()  
def dsacc():
  if(chontktiktok["status"]!=200):
    print("\033[1;34mAuthorization hoặc T sai hãy nhập lại!!!")
    quit()

  for i in range(len(chontktiktok["data"])):
    print(f'\033[1;95m[TAT07] => \033[1;36m[{i+1}] \033[1;97mTài Khoản: \033[1;93m {chontktiktok["data"][i]["nickname"]} \033[1;97m|\033[1;31mTrạng Thái:\033[1;32m Hoạt Động')
dsacc() 
while True:
  try:
    luachon = int(input("\033[1;95m[TAT07] => Chọn Tài Khoản Để Chạy  \n\033[1;97m╚⟩⟩⟩ "))
    while luachon > len((chontktiktok)["data"]):
      luachon = int(input("\033[1;32mAcc Này Không Có Trong Danh Sách , Hãy Nhập Lại : "))
    account_id = chontktiktok["data"][luachon - 1]["id"]
    break  
  except:
    print("\033[1;35mSai Định Dạng !!!") 
while True:
  try:
    delay = int(input("\033[1;95m[TAT07] => Nhập\033[1;91m Delay \n\033[1;97m╚⟩⟩⟩ "))
    break
  except:
    print("\033[1;31mSai Định Dạng !!!")
while True:
  try: 
    doiacc = int(input("\033[1;95m[TAT07] => \033[1;96mNhận Tiền Thất Bại Bao Nhiêu Job Thì Ngỉ \n\033[1;97m╚⟩⟩⟩ "))
    break
  except:
    print("\033[1;95m[TAT07] => AMIN CÓ ĐZ KHÔNG?!!!")    
os.system('cls' if os.name== 'nt' else 'clear')    
dem = 0
tong = 0
checkdoiacc = 0
dsaccloi = []
accloi = ""
os.system('cls' if os.name== 'nt' else 'clear')

for x in banner:
  print(x,end = "")
  sleep(0.001)
print(f'\033[1;36m|STT\033[1;97m| \033[1;33mThời gian ┊ \033[1;32mStatus | \033[1;31mType Job | \033[1;32mID Acc | \033[1;32mXu |\033[1;33m Tổng Tiền')

while True:
  if checkdoiacc == doiacc:
    dsaccloi.append(chontktiktok["data"][luachon - 1]["nickname"])
    print(f"\033[1;36mCác Acc Tiktok {dsaccloi} Có Vẻ Gặp Vấn Đề Nên Đổi Acc Chạy Đê ")
    dsacc()
    while True:
      try:
        luachon = int(input("\033[1;35m\033[1;97m║ Chọn \033[1;96mTài \033[1;95mKhoản \033[1;94mĐể \033[1;93mChạy \n\033[1;97m╚⟩⟩⟩  "))
        while luachon > len((chontktiktok)["data"]):
          luachon = int(input("\033[1;32mAcc Này Không Có Trong Danh Sách, Hãy Nhập Lại : "))
        account_id = chontktiktok["data"][luachon - 1]["id"]
        checkdoiacc = 0
        break  
      except:
        print("\033[1;35mSai Định Dạng !!!")

     
  print(f'\033[1;95m[TAT07] => \033[1;95mĐang Lấy Nhiệm Vụ Follow...',end="\r")    
  while True:
      try:  
          nhanjob = nhannv(account_id)
          break
      except:
          time.sleep(1)  # Thêm thời gian chờ 1 giây trước khi thử lại
          pass
  # while True:
  #   try:
  #       nhanjob = nhannv(account_id)
  #       if nhanjob:  # Kiểm tra nếu nhanjob tồn tại và không rỗng
  #           break  # Thoát khỏi vòng lặp nếu nhận được nhiệm vụ thành công
  #       else:
  #           print("\033[1;31mHệ thống đang tính toán jobs dành cho bạn,bấm load jobs lại sau 10 giây !")
  #   except:
  #       print("\033[1;31mHệ thống đang tính toán jobs dành cho bạn,bấm load jobs lại sau 10 giây !")
  #       pass
  #   time.sleep(1)
  if(nhanjob["status"] == 200):
    ads_id = nhanjob["data"]["id"]
    link = nhanjob["data"]["link"]
    object_id = nhanjob["data"]["object_id"]
    if(nhanjob["data"]["type"] != "follow"):
      baoloi(ads_id,object_id,account_id,nhanjob["data"]["type"])
      continue
    os.system(f"termux-open-url {link}")
    for remaining_time in range(delay, -1, -1):
            colors = [
                "\033[1;37mA\033[1;36mN\033[1;35mH\033[1;32m \033[1;34mT\033[1;33mU\033[1;36mA\033[1;36N🍍 - Đang Xóc Quả Lọ...\033[1;36m ",
                "\033[1;34mA\033[1;31mN\033[1;37mH\033[1;36m \033[1;35mT\033[1;37mU\033[1;33mA\033[1;32N🍍 - Đang Xóc Quả Lọ...\033[1;34m ",
                "\033[1;31mA\033[1;37mN\033[1;36mH\033[1;33m \033[1;32mT\033[1;34mU\033[1;35mA\033[1;37N🍍 - Đang Xóc Quả Lọ...\033[1;33m ",
                "\033[1;32mA\033[1;33mN\033[1;34mH\033[1;35m \033[1;37mT\033[1;36mU\033[1;31mA\033[1;34N🍍 - Đang Xóc Quả Lọ...\033[1;31m ",
                "\033[1;37mA\033[1;34mN\033[1;35mH\033[1;36m \033[1;33mT\033[1;31mU\033[1;37mA\033[1;34N🍍 - Đang Xóc Quả Lọ...\033[1;37m ",
                "\033[1;34mA\033[1;33mN\033[1;37mH\033[1;35m \033[1;36mT\033[1;36mU\033[1;32mA\033[1;37N🍍 - Đang Xóc Quả Lọ...\033[1;36m ",
                "\033[1;36mA\033[1;35mN\033[1;31mH\033[1;34m \033[1;35mT\033[1;32mU\033[1;36mA\033[1;33N🍍 - Đang Xóc Quả Lọ...\033[1;33mss ",
            ]
            for color in colors:
                print(f"\r{color}|{remaining_time}| \033[1;31m", end="")
                time.sleep(0.12)
                        
                        
    print("\r                          \r", end="") 
    print("\033[1;35m[TAT07] => Đang Đớp Tiền   ",end = "\r")
# Vòng lặp cố gắng nhận tiền với tối đa 2 lần thử
    max_attempts = 2
    attempts = 0
    nhantien = None

    while attempts < max_attempts:
        try:
            nhantien = hoanthanh(ads_id, account_id)
            if nhantien["status"] == 200:  # Nhận tiền thành công
                break
        except:
            pass  # Bỏ qua ngoại lệ và thử lại nếu có

        attempts += 1  # Tăng số lần thử

    # Kiểm tra kết quả của việc nhận tiền
    if nhantien and nhantien["status"] == 200:
        dem += 1
        tien = nhantien["data"]["prices"]
        tong += tien
        local_time = time.localtime()
        hour = local_time.tm_hour
        minute = local_time.tm_min
        second = local_time.tm_sec
        h = hour
        m = minute
        s = second
        if hour < 10:
            h = "0" + str(hour)
        if minute < 10:
            m = "0" + str(minute)
        if second < 10:
            s = "0" + str(second)

        chuoi = (f"\033[1;31m| \033[1;36m{dem}\033[1;31m\033[1;97m | "
                f"\033[1;33m{h}:{m}:{s}\033[1;31m\033[1;97m | "
                f"\033[1;32mSuccess\033[1;31m\033[1;97m | "
                f"\033[1;31m{nhantien['data']['type']}\033[1;31m\033[1;32m\033[1;32m\033[1;97m |"
                f"\033[1;32m Ẩn ID\033[1;97m |\033[1;97m \033[1;32m+{tien} \033[1;97m| "
                f"\033[1;33m{tong}")

        print("                                                    ", end="\r")
        print(chuoi)
        checkdoiacc = 0
    else:
        # Nếu cả 2 lần thử đều thất bại, bỏ qua nhiệm vụ
        while True:
            try:
                baoloi(ads_id, object_id, account_id, nhanjob["data"]["type"])
                print("                                              ", end="\r")
                print("\033[1;35m[TAT07] => BỎ QUA NHIỆM VỤ ", end="\r")
                sleep(1)
                checkdoiacc += 1
                break
            except:
                qua = 0
                pass
