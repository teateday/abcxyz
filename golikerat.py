import os
import sys,re
import datetime
from datetime import datetime, timedelta
import json
import random
import platform
try:
  import requests
except ImportError:
  os.system('pip install requests')
  import requests
try:
  from colorama import Back, Fore, Fore, Style, init
except ImportError:
  os.system('pip install colorama')
  from colorama import Back, Fore, Fore, Style, init
try:
  from bs4 import BeautifulSoup
except ImportError:
  os.system('pip3 install beautifulsoup4')
  from bs4 import BeautifulSoup

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")
    
import time
from time import sleep
import json,ast
os.system("cls" if os.name == "nt" else "clear")

init(autoreset=True)

def pr3(text):
  lines = text.split('\n')
  for line in lines:
      sys.stdout.write(line+'\n')
      sys.stdout.flush()
      sleep(0.1)
def pr(text):
  for i in range(len(text)+1):
      sys.stdout.write("\r" + text[:i])
      sys.stdout.flush()
      sleep(0.01)
  print()

def time():
  current_time = datetime.now()

  time = current_time.strftime("%M:%S")
  return time

def cint(number):
  while True:
    try:
      numbers = int(input(number))
      return numbers
    except ValueError:
      print(f'{red}Vui lòng chỉ nhập số')

def changetoken(red,green,white):
  if os.path.exists("cache_golike_auth.txt"):
    text=f'''{green}BẠN MUỐN DÙNG AUTH CŨ HAY ĐỔI AUTH
{red}[{white}1{red}] ĐỔI AUTH
{red}[{white}2{red}] DÙNG AUTH CŨ'''
    pr3(text)
    changetoken=cint(f'{red}NHẬP LỰA CHỌN: {green}')
    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    if changetoken==1:
      file_name = 'cache_golike_auth.txt'
      if os.path.exists(file_name):
          os.remove(file_name)
    else:
      pass

def banner(red,green,blue,yellow,cyan,pink):
  text=f'''{blue}      █████╗ ███╗   ██╗██╗  ██╗████████╗██╗   ██╗ █████╗ ███╗   ██╗
     {pink}██╔══██╗████╗  ██║██║  ██║╚══██╔══╝██║   ██║██╔══██╗████╗  ██║
     {blue}███████║██╔██╗ ██║███████║   ██║   ██║   ██║███████║██╔██╗ ██║
     {pink}██╔══██║██║╚██╗██║██╔══██║   ██║   ██║   ██║██╔══██║██║╚██╗██║
     {blue}██║  ██║██║ ╚████║██║  ██║   ██║   ╚██████╔╝██║  ██║██║ ╚████║
     {pink}╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝
                {red}Copyright By: @TAT07EXE Version : 2.2 '''
  pr3(text)
  text=f'''
---------------------------------------------------------------
{red}[TAT07] {cyan}CHÚ Ý!!!
[+]{pink} TIỀN SAU KHI LÀM NVỤ SẼ ĐƯỢC CỘNG SAU VÀI PHÚT.
[+]{pink} KIỂM TRA KHÔNG THẤY LÊN XU KO PHẢI DO TOOL LỖI.
[+]{pink} MÀ DO HỆ THỐNG GOLIKE CHƯA LOAD.
[+]{pink} CHÚC MỌI NGƯỜI SỬ DỤNG VUI VẺ.
[+]{pink} Bạn Đang Sử Dụng Tool: GOLIKE - TIKTOK.
---------------------------------------------------------------'''
  pr3(text)
  
def checkauth(red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink):
 while True :
  while True :
    if not os.path.exists("cache_golike_auth.txt"):
      auth=str(input(f'[+] {red}NHẬP AUTH:{green} '))
      headers ={
    'Authorization'     :auth,
    't':        'VFZSak1FMVVZelJPVkZVeVRXYzlQUT09',
    'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
 }
      check=json.loads(requests.get('https://gateway.golike.net/api/tiktok-account',headers=headers).text)
      if check['status']==200:
        name=check['data'][0]['username']
        hea={
'Authorization':auth,
't':    'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
}
# Chuỗi JSON đầu vào
        data=requests.get('https://gateway.golike.net/api/statistics/report',headers=hea).text
        try:
          data=json.loads(data)
        except :
          break
        # Tính tổng pending coin
        total_pending_coin = 0
        for key, value in data.items():
            if isinstance(value, dict) and 'pending_coin' in value:
                total_pending_coin += value['pending_coin']
        xht=data['current_coin']
        print('---------------------------------------------------------------')
        text=f'{red}[TAT07]{green} Tên Tài Khoản: {pink} {name}'
        pr(text)
        text=f'{red}[TAT07]{green} Số Dư Hiện Tại: {pink}{xht}đ'
        pr(text)
        # In tổng pending coin
        text=f'{red}[TAT07]{green} Đang Chờ Duyệt: {pink}{total_pending_coin}đ'
        pr(text)
        print('---------------------------------------------------------------')
        text=f'{red}[TAT07] {pink}SELECT {green}Danh Sách Acc'
        pr(text)
        nicknames = [item['nickname'] for item in check['data'] if 'nickname' in item]
        for i, nickname in enumerate(nicknames, start=1):
            globals()[f'{i}'] = nickname
        # In giá trị của các biến
        for i, nickname in enumerate(nicknames, start=1):
            text=f'{red}[{green}{i}{red}]: {globals()[f"{i}"]}'
            pr(text)
        with open("cache_golike_auth.txt", "w") as state_file:
          state_file.write(auth)
        return auth,check
      else:
        text=f'~[+]{red}FAIL AUTH KHÔNG CHÍNH XÁC>>{green}VUI LÒNG NHẬP LẠI'
        continue
    else:
     with open('cache_golike_auth.txt') as f:
        lines = f.readlines()
        auth=lines[0]
        headers ={
      'Authorization'   :auth,
      't':      'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
      'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
      }
        check=json.loads(requests.get('https://gateway.golike.net/api/tiktok-account',headers=headers).text)
        if check['status']==200:
          name =check['data'][0]['username']
          hea={
                'Authorization':auth,
                't':    'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
                'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
                  }


          data=requests.get('https://gateway.golike.net/api/statistics/report',headers=hea).text
          try:
            data=json.loads(data)
          except :
            break
          # Tính tổng pending coin
          total_pending_coin = 0
          for key, value in data.items():
              if isinstance(value, dict) and 'pending_coin' in value:
                  total_pending_coin += value['pending_coin']
          xht=data['current_coin']
          text=f'{red}[TAT07]{green} Tên Tài Khoản: {pink} {name}'
          pr(text)
          text=f'{red}[TAT07]{green} Số Dư Hiện Tại: {pink}{xht}đ'
          pr(text)
          # In tổng pending coin
          text=f'{red}[TAT07]{green} Đang Chờ Duyệt: {pink}{total_pending_coin}đ'
          pr(text)
          nicknames = [item['nickname'] for item in check['data'] if 'nickname' in item]
          for i, nickname in enumerate(nicknames, start=1):
              globals()[f'{i}'] = nickname
          print('---------------------------------------------------------------')
          text=f'{red}[TAT07]{green} Danh Sách Acc TikTok'
          pr(text)
          # In giá trị của các biến
          for i, nickname in enumerate(nicknames, start=1):
              text=f'{pink}[TAT07] =>{red}[{green}{i}{red}]: {globals()[f"{i}"]}'
              pr(text)

        return auth, check

def get_id_from_nickname_number(ranmau,check,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink):
  while True :

    user_input=input(f'{red}[TAT07]{random.choice(ranmau)}>{random.choice(ranmau)}>{random.choice(ranmau)}> {green}Chọn Acc TikTok Đớp JOB:{green} ')
    try:
      n = int(user_input)
      if 'data' in check and len(check['data']) >= n:
          idtiktok = check['data'][n-1]['id']
          if idtiktok :
              text=f"{red}ID CỦA NICKNAME SỐ {n} LÀ: {green}{idtiktok}"
              pr(text)
              print('---------------------------------------------------------------')
              return idtiktok
          else:
              text=f"{red}KHÔNG TÌM THẤY NICKNAME TƯƠNG ỨNG."
              pr(text)
      else:
          continue
    except ValueError:
          pr(f"{red}[ĐCU THẰNG NGU NHẬP SỐ THÔI]")
          continue

def getjob(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink):
  startmaxjob=1
  job_success=0
  while True :
    while True :
      hea={
      'Authorization':  auth,
     't':       'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
    'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
}

      try:
        a=requests.get(f'https://gateway.golike.net/api/advertising/publishers/tiktok/jobs?account_id={idtiktok}&data=null',headers=hea).json()
      except :
        break
      try:
        link=a['data']['link']
        id=a['data']['id']
        object_id=a['lock']['object_id']
        os.system(f'termux-open-url {link}')
      except :
        break
      for k in range(delay,-1,-1):
        mau=random.choice(ranmau)
        print(f'{green}JOB SUCCESS:{red}[{job_success}/{startmaxjob-1}]{random.choice(ranmau)}LOADING  {random.choice(ranmau)}>> {yellow}NVỤ MỚI SAU {random.choice(ranmau)}>> {random.choice(ranmau)}[{k}s] ',end='\r')
        sleep(1)
      headers = {
          'authorization': auth,
     't':       'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
    'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
}

      json_data = {
          'ads_id': id,
          'account_id': idtiktok ,
          'async': True,
          'data': None,
      }

      g = requests.post(
          'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',
          headers=headers,
          json=json_data,
      ).text
      try:
        g=json.loads(g)
      except :
        break
      if g['status']==200:
        job_success+=1
        print(f'{green}Anh Tuấn Đây:{red}[{job_success}/{startmaxjob-1}] {cyan}[{time()}] | {random.choice(ranmau)}Đớp | {green}FOLLOW | +{g["data"]["prices"]}')
        startmaxjob+=1
        if startmaxjob == maxjob+1:
          print(f'{red}[ĐỚP]{pink} MAX JOB RỒI CU')
          return
      else:
        print(f'{green}[TAT07] {red}ĐANG XÓC QUẢ LỌ...',end="\r")
        sleep(1)
        g = requests.post(
          'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',
          headers=headers,
          json=json_data,
      ).text
        try:
          g=json.loads(g)
        except :
          break
        if g['status']==200:
          job_success+=1
          print(f'{green}Anh Tuấn Đây:{red}[{job_success}/{startmaxjob-1}] {cyan}[{time()}] | {random.choice(ranmau)}Đớp | {green}FOLLOW | +{g["data"]["prices"]}')
          startmaxjob+=1
          if startmaxjob == maxjob+1:
            print(f'{red}[ĐỚP]{pink} MAX JOB RỒI CU')
            return
        if g['status'] !=200:
          print(f'{green}[TAT07] {red}ĐANG XÓC QUẢ LỌ...   ',end="\r")
          headers = {
              'authorization': auth,
    't':        'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
    'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
}

          json_data = {
              'description': 'Báo cáo hoàn thành thất bại',
              'users_advertising_id': id,
              'type': 'ads',
              'provider': 'tiktok',
              'fb_id': idtiktok ,
              'error_type': 3,
          }

          requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data)


          headers = {
              'authorization': auth,
    't':        'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
    'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
}

          json_data = {
              'ads_id': id,
              'object_id': object_id,
              'account_id': idtiktok ,
              'type': 'follow',
          }
          skipjob=requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',
              headers=headers,
              json=json_data,
          )
          startmaxjob+=1
          if startmaxjob == maxjob+1:
            print(f'{red}[TAT07]{green} ĐỚP MAX JOB RỒI')
            return

def getjob_follow(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink):
  startmaxjob=1
  job_success=0
  while True :
    while True :
      hea={
      'Authorization':  auth,
    't':        'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
    'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
}

      try:
        a=requests.get(f'https://gateway.golike.net/api/advertising/publishers/tiktok/jobs?account_id={idtiktok}&data=null',headers=hea).json()
      except :
        break
      try:
        link=a['data']['link']
        id=a['data']['id']
        object_id=a['lock']['object_id']
        if 'video' in link:
          print(f"{pink}[TAT07] {red}ĐANG LỌC JOB LIKE...                             ",end='\r')
          headers = {
              'authorization': auth,
    't':        'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
    'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
}

          json_data = {
    'description': 'Tôi không muốn làm Job này',
    'users_advertising_id': id,
    'type': 'ads',
    'provider': 'tiktok',
    'fb_id': idtiktok,
    'error_type': 0,
}

          response = requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data)


          json_data = {
    'ads_id': id,
    'object_id': object_id,
    'account_id': idtiktok,
    'type': 'like',
}
          response = requests.post(
    'https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',
    headers=headers,
    json=json_data,
)
        else:
          os.system(f'termux-open-url {link}')
          for k in range(delay,-1,-1):
            mau=random.choice(ranmau)
            print(f'{green}AnhTuanDay:{red}[{job_success}/{startmaxjob-1}]{random.choice(ranmau)}LOADING  {random.choice(ranmau)}>> {yellow}NVỤ MỚI SAU {random.choice(ranmau)}>> {random.choice(ranmau)}[{k}s] ',end='\r')
            sleep(1)
          print(f'{red}ĐANG KIỂM TRA TRẠNG THÁI JOB                  ',end='\r')
          headers = {
              'authorization': auth,
        't':    'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
        'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
    }

          json_data = {
              'ads_id': id,
              'account_id': idtiktok ,
              'async': True,
              'data': None,
          }
          try:

            g =requests.post(
            'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',headers=headers,json=json_data).json()
            if g['status']==200:
              job_success+=1
              print(f'{green}Anh Tuấn Đây:{red}[{job_success}/{startmaxjob-1}] {cyan}[{time()}] | {random.choice(ranmau)}Đớp | {green}FOLLOW | +{g["data"]["prices"]}')
              startmaxjob+=1
              if startmaxjob == maxjob+1:
                print(f'~[+]{pink}ĐÃ ĐẠT MAX JOB. ')
                return

            else:
              print(f'{green}ĐANG KIỂM TRA LẠI TRẠNG THÁI JOB                     ',end="\r")
              sleep(1)

              try:
                g = requests.post(
                'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',
                headers=headers,
                json=json_data,
            ).json()
                if g['status']==200:
                  job_success+=1
                  print(f'{green}Anh Tuấn Đây:{red}[{job_success}/{startmaxjob-1}] {cyan}[{time()}] | {random.choice(ranmau)}Đớp | {green}FOLLOW | +{g["data"]["prices"]}')
                  startmaxjob+=1
                  if startmaxjob == maxjob+1:
                    print(f'~[+]{pink}ĐÃ ĐẠT MAX JOB. ')
                    return
                else:
                  print(f'{red}ĐANG BỎ QUA NHIỆM VỤ                   ',end='\r')
                  headers = {
                      'authorization': auth,
            't':        'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
            'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
        }

                  json_data = {
                      'description': 'Báo cáo hoàn thành thất bại',
                      'users_advertising_id': id,
                      'type': 'ads',
                      'provider': 'tiktok',
                      'fb_id': idtiktok ,
                      'error_type': 3,
                  }

                  requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data)


                  headers = {
                      'authorization': auth,
            't':        'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
            'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
        }

                  json_data = {
                      'ads_id': id,
                      'object_id': object_id,
                      'account_id': idtiktok ,
                      'type': 'follow',
                  }
                  skipjob=requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',
                      headers=headers,
                      json=json_data,
                  )
                  startmaxjob+=1
                  if startmaxjob == maxjob+1:
                    print(f'~[+]{green}ĐÃ ĐẠT MAX JOB')
                    return
              except :
                print('Đang thử lại......')
                sleep(1)
          except :
            break
      except:
         break

#biến
#green='\033[38;5;10m'
blue='\033[38;5;12m'
cyan='\033[38;5;14m'
white='\033[1;39m'
magenta='\033[38;5;5m'
orange='\033[38;5;202m'
xanhnhat = "\033[1;36m"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
xduong = "\033[1;34m"
pink = "\033[1;35m"
trang = "\033[1;39m"
whiteb="\033[1;39m"
redb="\033[1;31m"
end='\033[0m'
ranmau=(red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)


def tinhngay(songay):
    time = datetime.now()
    start=time.strftime("%d/%m/%Y")
    end = (time + timedelta(days=int(songay))).strftime("%d/%m/%Y")
    return start, end
banner(red,green,blue,yellow,cyan,pink)

changetoken(red,green,white)
auth,check =checkauth(red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
while True:
      if not os.path.exists("setting_golike.txt"):
        idtiktok =get_id_from_nickname_number(ranmau,check,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
        print(f'''~[+]{red}BẠN CÓ MUỐN LỌC JOB LIKE KHÔNG:
{red}[1]:{green} DẠ CÓ
{red}[2]:{green} DẠ KHÔNG''')
        select_job=cint(f'{red}NHẬP LỰA CHỌN:{green}')
        delay =cint(f'~[+]{red}NHẬP DELAY: {green}')
        maxjob= cint(f'~[+]{red}NHẬP MAX JOB: {green}')
        setting={
          "loaijob":select_job,
          "delay":delay,
          "maxjob":maxjob
        }
        with open("setting_golike.txt", "w") as file:
    # Ghi dữ liệu vào tệp tin
              file.write(json.dumps(setting))
        print(f'{cyan}KHỞI CHẠY NHIỆM VỤ',end='\r')
        print('---------------------------------------------------------------')
        sleep(1)
        if select_job==1:
          getjob_follow(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
        else:
          getjob(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
      else:
          idtiktok =get_id_from_nickname_number(ranmau,check,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
          select_setting=input(f'{green}Bạn có muốn sử dụng setting cũ không?[y/n]{cyan}:' )
          if select_setting == 'n':
             os.remove('setting_golike.txt')
             os.system('clear')
             break

          try:
              with open("setting_golike.txt", "r") as file:
                data_txt=file.read()
                data_json = json.loads(data_txt)
              select_job = int(data_json.get('loaijob'))
              delay = int(data_json.get('delay'))
              maxjob= int(data_json.get('maxjob'))
              print(f'{cyan}KHỞI CHẠY NHIỆM VỤ',end='\r')
              print('---------------------------------------------------------------')
              sleep(1)
              if select_job==1:
                getjob_follow(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
              else:
                getjob(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
          except json.JSONDecodeError:
              print("Dữ liệu không hợp lệ. Vui lòng kiểm tra lại định dạng JSON trong tệp.")

