from urllib.parse import quote
import datetime
import os
import ssl
from urllib.parse import urlencode
from http import cookiejar
from urllib3.exceptions import InsecureRequestWarning
import hashlib
import random
try:
    import base64
    from requests.exceptions import RequestException
    import requests
    import pystyle
    from concurrent.futures import ThreadPoolExecutor
    from faker import Faker
    from requests import session
    import concurrent.futures

except ImportError:
    import os
    os.system("pip install faker")
    os.system("pip install colorama")
    os.system("pip install requests")
    os.system("pip install pystyle")
    os.system("pip install concurrent.futures")
    os.system("pip install base64")
import requests,os,time,re,json,uuid,random,sys
from concurrent.futures import ThreadPoolExecutor
import datetime
from datetime import datetime
import requests,json
import uuid
import requests
from time import sleep
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
from pystyle import Colors, Colorate, Write, Center, Add, Box
from time import sleep,strftime
import socket
from pystyle import *

# fix
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def runbanner(text, delay=0.001):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

hong = "\033[1;35m"
trang = "\033[1;37m\033[1m"
xanh_la = "\033[1;32m\033[1m"
xanh_duong = "\033[1;34m\033[1m"
xanhnhat = '\033[1m\033[38;5;51m'
do = "\033[1;31m\033[1m\033[1m"
xam='\033[1;30m\033[1m'
vang = "\033[1;33m\033[1m"
tim = "\033[1;35m\033[1m"
hongnhat = "#FFC0CB"
atuan = "TAT07"
dac_biet = "\033[32;5;245m\033[1m\033[38;5;39m"
colors = [
    "\033[1;37m\033[1m",  # Trắng
    "\033[1;32m\033[1m",  # Xanh lá
    "\033[1;34m\033[1m",  # Xanh dương
    "\033[1m\033[38;5;51m",  # Xanh nhạt
    "\033[1;31m\033[1m\033[1m",  # Đỏ
    "\033[1;30m\033[1m",  # Xám
    "\033[1;33m\033[1m",  # Vàng
    "\033[1;35m\033[1m",  # Tím
    "\033[32;5;245m\033[1m\033[38;5;39m",  # Màu đặc biệt
]
random_color = random.choice(colors)
def idelay(o):
    while(o>0):
        o=o-1
        print(f"{trang}[{hong}TAT07{trang}] \033[1;33mX\033[1;34mX\033[1;35mX\033[1;32mX\033[1;33mX\033{trang}[\033[1;35m.....""]""["+str(o)+"]""    ",end='\r')
        time.sleep(1/6)
        print(f"{trang}[{hong}TAT07{trang}] \033[1;31mX\033[1;32mX\033[1;33mX\033[1;34mX\033[1;35mX\033{trang}....""]"f"{trang}[{xanhnhat}"+str(o)+f"{trang}]""     ",end='\r')
        time.sleep(1/6)
        print(f"{trang}[{hong}TAT07{trang}] \033[1;32mX\033[1;33mX\033[1;34mX\033[1;35mX\033[1;36mX\033{trang}...""]"f"{trang}[{xanh_la}"+str(o)+f"{trang}]""     ",end='\r')
        time.sleep(1/6)
        print(f"{trang}[{hong}TAT07{trang}] \033[1;31mX\033[1;33mX\033[1;35mX\033[1;33mX\033[1;31mX\033{trang}..""]"f"{trang}[{do}"+str(o)+f"{trang}]""     ",end='\r')
        time.sleep(1/6)
        print(f"{trang}[{hong}TAT07{trang}] \033[1;32mX\033[1;34mX\033[1;36mX\033[1;32mX\033[1;34mX\033{trang}.""]"f"{trang}[{tim}"+str(o)+f"{trang}]""     ",end='\r')
        time.sleep(1/6)
        print(f"{trang}[{hong}TAT07{trang}] \033[1;31mX\033[1;34mX\033[1;36mX\033[1;32mX\033[1;34mX\033{trang}""]"f"{trang}[{vang}"+str(o)+f"{trang}]""     ",end='\r')
        time.sleep(0.1)
        print(f"{trang}[{hong}TAT07{trang}] \033[1;31mX\033[1;34mX\033[1;36mX\033[1;32mX\033[1;34mX{trang}[\033[1;33m•••••{trang}""]"f"{trang}[{xanh_la}"+str(o)+f"{trang}]""     ",end='\r')

chontool = f"""
\033[1;35m █████╗ ███╗   ██╗██╗  ██╗████████╗██╗   ██╗ █████╗ ███╗   ██╗
\033[1;37m██╔══██╗████╗  ██║██║  ██║╚══██╔══╝██║   ██║██╔══██╗████╗  ██║
\033[1;35m███████║██╔██╗ ██║███████║   ██║   ██║   ██║███████║██╔██╗ ██║
\033[1;37m██╔══██║██║╚██╗██║██╔══██║   ██║   ██║   ██║██╔══██║██║╚██╗██║
\033[1;35m██║  ██║██║ ╚████║██║  ██║   ██║   ╚██████╔╝██║  ██║██║ ╚████║
\033[1;37m╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝
\033[1;31m────────────────────────────────────────────────────────────
\033[1;31m[\033[1;37mTAT07\033[1;31m] \033[1;37m=> \033[1;33mTOOL SPAM RÉO TÊN NYC
\033[1;31m[\033[1;37mTAT07\033[1;31m] \033[1;37m=> \033[1;35mADMIN: \033[1;36mTRẦN ANH TUẤN
\033[1;31m[\033[1;37mTAT07\033[1;31m] \033[1;37m=> \033[1;32mBOX SUPPORT: \033[1;37mupdate
\033[1;31m[\033[1;37mTAT07\033[1;31m] \033[1;37m=> \033[1;34mYOUTUBE: \033[1;37mupdate
\033[1;31m[\033[1;37mTAT07\033[1;31m] \033[1;37m=> \033[1;35mCHÚ Ý: \033[1;37KHÔNG SỬ DỤNG VÀO NHỮNG NGƯỜI VÔ TỘI!
\033[1;31m────────────────────────────────────────────────────────────"""
clear()
runbanner(chontool)
idcanspam=input(f'\033[1;31m[\033[1;37mTAT07\033[1;31m] {xanhnhat}Nhập ID Box Cần Spam :{vang} ')
while True:
      ck=input(f'\033[1;31m[\033[1;37mTAT07\033[1;31m] {xanhnhat}Nhập Cookie Facebook :{vang} ')
      try:
        get=requests.get(f'https://mbasic.facebook.com/privacy/touch/block/confirm/?bid={idcanspam}&ret_cancel&source=profile',headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie': ck,'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1'}).text
        fb_dtsg=get.split('<input type="hidden" name="fb_dtsg" value="')[1].split('" autocomplete="off" />')[0]
        jazoest=get.split('<input type="hidden" name="jazoest" value="')[1].split('" autocomplete="off" />')[0]
        clear()
        break
      except:
        print(f'{do}ERROR Cookie DIE! Lấy Lại Cookie Đi')   
params = {
      "icm": '1',
    }

headers = {
      "Host":"mbasic.facebook.com",
      "content-length":"247",
      "content-type":"application/x-www-form-urlencoded",
      "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
      "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
      "sec-fetch-site":"same-origin",
      "sec-fetch-mode":"navigate",
      "sec-fetch-user":"?1",
      "sec-fetch-dest":"document",
      "accept-encoding":"gzip, deflate, br",
      "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
      "cookie":ck,
    }
chontool = f"""
\033[1;35m █████╗ ███╗   ██╗██╗  ██╗████████╗██╗   ██╗ █████╗ ███╗   ██╗
\033[1;37m██╔══██╗████╗  ██║██║  ██║╚══██╔══╝██║   ██║██╔══██╗████╗  ██║
\033[1;35m███████║██╔██╗ ██║███████║   ██║   ██║   ██║███████║██╔██╗ ██║
\033[1;37m██╔══██║██║╚██╗██║██╔══██║   ██║   ██║   ██║██╔══██║██║╚██╗██║
\033[1;35m██║  ██║██║ ╚████║██║  ██║   ██║   ╚██████╔╝██║  ██║██║ ╚████║
\033[1;37m╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝
\033[1;31m────────────────────────────────────────────────────────────
\033[1;31m[\033[1;37mTAT07\033[1;31m] \033[1;37m=> \033[1;33mTOOL SPAM RÉO TÊN NYC
\033[1;31m[\033[1;37mTAT07\033[1;31m] \033[1;37m=> \033[1;35mADMIN: \033[1;36mTRẦN ANH TUẤN
\033[1;31m[\033[1;37mTAT07\033[1;31m] \033[1;37m=> \033[1;32mBOX SUPPORT: \033[1;37mupdate
\033[1;31m[\033[1;37mTAT07\033[1;31m] \033[1;37m=> \033[1;34mYOUTUBE: \033[1;37mupdate
\033[1;31m[\033[1;37mTAT07\033[1;31m] \033[1;37m=> \033[1;35mCHÚ Ý: \033[1;37KHÔNG SỬ DỤNG VÀO NHỮNG NGƯỜI VÔ TỘI!
\033[1;31m────────────────────────────────────────────────────────────"""
clear()  
runbanner(chontool) 
chon_name = str(input(f"\033[1;31m[\033[1;37mTAT07\033[1;31m] \033[1;37m{xanhnhat}Điền Name Con NYC Mà Người AE Cần Tôi Réo:{vang} "))
if chon_name.lower() == "{chon_name}":
      lag = "{chon_name}"
elif chon_name.lower() == "ndjjdkd":
      lag = " "
else:
      CAU_CHUI = [
          f"dcmmm mày {chon_name}",
          f"ccho sua lofi de {chon_name}",
          f"sua di {chon_name} em😏🤞",
          f"lofi di {chon_name} cu😝",
          f"tk hac lao {chon_name} eyy🤣🤣",
          f"nhanh ti em {chon_name}🤪👌",
          f"cam a {chon_name} mo coi😏🤞",
          f"hang hai len ti {chon_name} de👉🤣",
          f"cn tat nguyen {chon_name}😏??",
          f"cn 2 lai mat mam {chon_name}🤪👎",
          f"anh cho may sua a {chon_name}😏🤞",
          f"ah ba meta 2024 ma {chon_name}😋👎",
          f"bi anh da na tho cmnr dk {chon_name}🤣",
          f"thieu oxi a {chon_name}🤣🤣",
          f"anh cko may oxi hoa ne {chon_name}😏👉🤣",
          f"may cay cha qua a cn ngu {chon_name}🤪",
          f"may phe nhu con me may bi tao hiep ma {chon_name}🤣",
          f"dung ngam dang nuot cay tao nha coan {chon_name}👉🤣",
          f"con cho {chon_name} cay tao ro👉🌶",
          f"oc cho ngoi do nhay voi tao a {chon_name}🤣",
          f"me may bi tao cho len dinh r {chon_name}=))",
          f"ui cn ngu {chon_name} oc cac=))",
          f"cn gai me may khog bt day nay a {chon_name} cn oc cac😝",
          f"cn cho {chon_name} may cam a:))?",
          f"cam lang that r a cn ngu {chon_name}🤣",
          f"ui tk cac dam cha chem chu ak {chon_name}😝🤞",
          f"cn cho dot so tao run cam cap me roi ha em {chon_name} =))",
          f"ui cai con hoi {chon_name}👉🤣",
          f"cn me may chet duoi ao roi kia {chon_name}😆",
          f"djt con {chon_name} cu cn lon tham:))",
          f"ui con bem {chon_name} nha la nhin phen v:))",
          f"con cho cay gan nha sua di {chon_name}😏",
          f"con bem {chon_name} co me khog😏🤞",
          f"a quen may mo coi tu nho ma {chon_name}🤣",
          f"sua chill de {chon_name} oc🤣",
          f"hay cam nhan noi dau di em {chon_name}:))))",
          f"hinh anh con bem {chon_name} gie rach bi anh cha dap:))))))",
          f"ti anh chup dang tbg la may hot nha {chon_name}🤣",
          f"a may muon hot cx dau co de cn ngu {chon_name}👉🤣🤣",
          f"oi may bi cha suc pham kia {chon_name}-))",
          f"tao co noti con boai {chon_name} so tao:)) ti tao cap dang profile 1m theo doi:))",
          f" {chon_name} con o moi khong bame bi tao khinh thuong=)))",
          f"may con gi khac hon khong con bem du ngu {chon_name}🤣",
          f"cam canh cdy ngu bi cha chui khong giam phan khang a {chon_name}:))",
          f"bi tao chui ma toi so a {chon_name}🤞",
          f"nhin ga {chon_name} muon ia chay🤣",
          f"con culi lua thay phan ban bi phan boi a {chon_name}:))",
          f"may bi tao chui cho om han dk {chon_name}👉🤣🤣🤞",
          f"bi tao chui cho so queo cac dung khong {chon_name}:))))",
          f"dung cam han tao nua {chon_name}:))",
          f"con dog {chon_name} bi tao chui ghi thu a:))",
          f"su dung ngon sat thuong xiu de bem anh di mo {chon_name}=)))",
          f"co sat thuong chi mang ko ay {chon_name}😝",
          f"con ngheo nha la {chon_name} bi bo si va👉🤣🤣",
          f"nao may co biet thu nhu anh vay {chon_name}🤪👌",
          f"thang nghich tu {chon_name} sao may giet cha may the:))",
          f"khong ngo thang phan nghich {chon_name} lua cha doi me=))",
          f"tk ngu {chon_name} bi anh co lap ma-))",
          f"phan khang di con cali {chon_name} mat mam:))",
          f"may con gi khac ngoai sua khong ay {chon_name}👉😏🤞",
          f" {chon_name} con mo coi=))",
          f"bi cha chui phat nao ghi han phat do {chon_name} dk em:))",
          f"may toi day de chi bi tao chui thoi ha {chon_name}:))",
          f"bo la ac quy fefe ne {chon_name}🤣🤣",
          f"nen bo lay cay ak ban nat so may luon😏🤞",
          f"keo lu ban an hai may ra lmj dc anh khong vay {chon_name}🤣🤞",
          f"ui ui dung thang an hai mang ten {chon_name}:))",
          f"dung la con can ba mxh chi biet nhin anh chui cha mang me no ma {chon_name}=))",
          f"may co phan khang duoc khong vay:)) {chon_name}",
          f"may khong phan khang duoc a {chon_name}=))",
          f"may yeu kem den vay a con cali {chon_name}😋👎",
          f"con cali {chon_name} mat mam cay ah roi🌶",
          f"cu anh lam dk em {chon_name}:))",
          f"may co biet gi ngoai sua kiki dau ma {chon_name}👉🤣🤣",
          f"may la chi qua qua ban may la chi gau gau ha {chon_name}=))",
          f"mua skill di em {chon_name}🤪🤞",
          f"anh mua skill duoc ma em {chon_name}😏🤞",
          f"anh mua skill vo cai lon me may ay em {chon_name}:))",
          f"con culi {chon_name} said : sap win duoc anh roi mung vai a🤣",
          f"con cali {chon_name} nghi vay nen mung lam dk:)) {chon_name}",
          f"win duoc anh dau de dau em {chon_name}🤪🤞",
          f"con cho dien {chon_name} sua dien cuong nao🤣",
          f"ui ui con kiki {chon_name} cay anh da man a🌶",
          f"tk mo coi {chon_name} sua belike a🤣",
          f"chill ti di em {chon_name}🤣🤣",
          f"sao sua ko chill gi het vay {chon_name}🤣🤣",
          f"bi anh chui cho tat ngon a {chon_name}=))",
          f"may sua mau khong anh dap may tat sua bh {chon_name}:))",
          f"sua toi khi kiet que nha cn thu {chon_name}🤣🤣",
          f"cam may ngung nha cn kiki {chon_name}😝",
          f"bo mat nghen ngon a ma nhai hoai v {chon_name}:🤪👌",
          f"tao cam 1887 ban ca gia pha nha may chet {chon_name} ay:))",
          f"may thay anh ba qua nen sui cmnr a {chon_name}😜",
          f"sao may cam vay {chon_name}🤪🤞",
          f"may cam = tao win do {chon_name}🤣🤣",
          f"may nham win duoc tao khong {chon_name}🤣",
          f"ga ma hay sua vay {chon_name}👉🤣",
          f"tao dem 123 may chua len tao giet con gia may do {chon_name}🤣",
          f"ra tinh hieu de tao treo co con ba may die di {chon_name}:))",
          f"may ra tinh hieu sos chay thoat than trc a {chon_name}🤣",
          f"dung thang con bat hieu {chon_name}👉🤣🤣",
          f"con me may moi de ra thang con bat hieu nhu vay🤣🤞",
          f"thang con troi danh di bao gia pha a {chon_name}🤪🤞",
          f"bao nhu may gap anh cung tat dien {chon_name}🤣🤞🤞",
          f" {chon_name} may bi anh chui off mxh la vua roi=))",
          f"may lam lai anh khong vayy {chon_name}:))",
          f"tao biet la khongg ma {chon_name}👉🤣",
          f"do may bai tao all san ro cmnr ma {chon_name}🤣",
          f"tao dep trai ma {chon_name}👉🤣",
          f"nen may le luoi liem chan tao di {chon_name}🤪🤞",
          f"o o ccho {chon_name} loe toe bo may dap vo mom🤣",
          f"tk cac {chon_name} oc cho vai cuc👉🤣",
          f"tk ngu {chon_name} thay hw la lam than a🤪🤞",
          f"du ngu cung onl mxh a {chon_name}😏😏",
          f"svat {chon_name} cay cu anh den tim tai het roi a🤣",
          f"moi ti xiu ma go duoi roi a {chon_name}🤣",
          f"anh speed ne tk ngu {chon_name}👉😏",
          f"cn cho ngu {chon_name} moi 5p ma da met a🤣🤣",
          f"tk bach tang {chon_name}",
          f"ccho dot la {chon_name}",
          f"ngu cn ra de a {chon_name}",
          f"tk ngon lu {chon_name}",
          f"sped di tk ga {chon_name}",
          f"ga v em {chon_name}",
          f"anh uoc ga giong may a {chon_name}",
          f"o o cn nghich tu {chon_name}",
          f"chay dau vay tk {chon_name} ngu",
          f"anh cho may chay a {chon_name}",
          f"chay nhanh vay em {chon_name}",
          f"ma sao em thoat khoi anh duoc ha {chon_name} em",
          f"co gang win anh di {chon_name}",
          f"sap win dc roi do {chon_name}",
          f"e e care t di ma {chon_name}",
          f"sao ko giam {chon_name}",
          f"roi roi cam lang a {chon_name}",
          f"on khong vay {chon_name}",
          f"bat on a {chon_name}",
          f"bi tao chui ma sao on dc {chon_name}",
          f"cn cali {chon_name} sua bay",
          f"ai cho m sua v {chon_name}",
          f"xin phep ah chua o {chon_name}",
          f"da may chetme may ma cn culi {chon_name} du xe",
          f"sao may bel vay em {chon_name}",
          f"120kg a {chon_name}",
          f"sao may khon v {chon_name}",
          f"khon nhu con kiki nha tao🤣 {chon_name}",
          f"sat thuog ti di em {chon_name}",
          f"em kem coi v {chon_name}",
          f"co gi khac khong {chon_name}",
          f"khong co j a {chon_name}",
          f"em phe vay la cung dk {chon_name}",
          f"dung a🤣 {chon_name}",
          f"roi roi {chon_name}",
          f"cn phe {chon_name}",
          f"leg keg di troi {chon_name}",
          f"lien tuc {chon_name} di boa",
          f"sao ko lien tuc {chon_name}",
          f"yeu sinh ly a🤣 {chon_name}",
          f"nang khong em {chon_name}",
          f"so anh nen dai ra mau luon a {chon_name}",
          f"cn culi {chon_name} mat mam",
          f"gap gap len tk ngu {chon_name}",
          f"anh speed vcl ma {chon_name}",
          f"may slow vaicalonn {chon_name}",
          f"an c j phe lam vay tk phe vat {chon_name}",
          f"cay cu anh lam ma {chon_name}",
          f"cay ma choi a {chon_name}",
          f"nhin mat ns nhu trai ot kia {chon_name}",
          f"choi la doi a {chon_name}",
          f"sao hay v cn dog ten {chon_name}",
          f"t cam ba chia dam dit bme may ma {chon_name}",
          f"o o thg cn bat hieu nay chs gay vs cau {chon_name} a",
          f"{chon_name} teu v em",
          f"tau hai a {chon_name}",
          f"cn an hai danh trong lang a {chon_name}",
          f"duoi a {chon_name}",
          f"nhin biet duoi r🤣 {chon_name}",
          f"anh cho may rot a {chon_name}",
          f"sao cam lang r {chon_name}",
          f"roi roi cn ngu cam {chon_name}",
          f"ccho {chon_name} nay phen ia v",
          f"anh go ba vcl ay {chon_name}",
          f"cay a {chon_name}",
          f"Ngầu Êyy {chon_name}",
          f"Cố lên con thú {chon_name}",
          f"Tao cho mày ngậm chx ? {chon_name}",
          f"Mày cút rồi hả {chon_name} ",
          f"cố tí nữa {chon_name}",
          f"speed nào {chon_name}",
          f"nhây tới năm sau dc ko {chon_name}",
          f"mạnh mẽ nào {chon_name}",
          f"Con culi mocoi ey {chon_name}",
          f"k đc à {chon_name}",
          f"con chó ngu cố đê {chon_name}",
          f"sao m câm kìa {chon_name}",
          f"gà j {chon_name}",
          f"mày sợ tao à =)) {chon_name}",
          f"m gà mà {chon_name}",
          f"mày ngu rõ mà {chon_name}",
          f"đúng mà {chon_name}",
          f"cãi à {chon_name}",
          f"mày còn gì khác k {chon_name}",
          f"học lỏm kìa {chon_name}",
          f"cố tí em {chon_name}",
          f"mếu à {chon_name}",
          f"sao mếu kìa {chon_name}",
          f"tao đã cho m mếu đâu {chon_name}",
          f"va lẹ đi con dốt {chon_name}",
          f"sao kìa {chon_name}",
          f"từ bỏ r à {chon_name}",
          f"mạnh mẽ tí đi con đĩ {chon_name}",
          f"cố lên con chó ngu {chon_name}",
          f"=)) cay tao à con đĩ {chon_name}",
          f"sợ tao à {chon_name}",
          f"sao sợ tao kìa {chon_name}"
          f"cay lắm phải kh {chon_name}",
          f"ớt rồi kìa em {chon_name}",
          f"mày còn chối à {chon_name}",
          f"làm tí đê {chon_name}",
          f"mới đó đã mệt r kìa {chon_name}",
          f"sao gà mà sồn v {chon_name}",
          f"sồn như lúc đầu cho tao {chon_name}",
          f"sao à {chon_name}",
          f"ai cho m nhai {chon_name}",
          f"cay lắm r {chon_name}", 
          f"từ bỏ đi em {chon_name}",
          f"mày nghĩ mày làm t cay đc à {chon_name}",
          f"có đâu {chon_name}",
          f"tao đang hành m mà {chon_name}",
          f"bịa à {chon_name}",
          f"cay :))))) {chon_name}",
          f"cố lên chó dốt {chon_name}",
          f"hăng tiếp đi {chon_name}",
          f"tới sáng k em {chon_name}",
          f"k tới sáng à {chon_name}",
          f"chán v {chon_name}",
          f"m gà mà {chon_name}",
          f"log acc thay phiên à {chon_name}",
          f"coi tụi nó dồn ngu kìa {chon_name}",
          f"sợ tao à con chó đần {chon_name}",
          f"lại win à {chon_name}",
          f"lại win r {chon_name}",
          f"lũ cặc cay tao lắm🤣🤣 {chon_name}",
          f"cố lên đê {chon_name}",
          f"sao mới 5p đã câm r {chon_name}",
          f"yếu đến thế à {chon_name}",
          f"sao kìa {chon_name}",
          f"khóc kìa {chon_name}",
          f"cầu cứu lẹ ei {chon_name}",
          f"ai cứu đc m à :)) {chon_name}",
          f"tao bá mà {chon_name}",
          f"sao m gà thế {chon_name}",
          f"hăng lẹ cho tao {chon_name}",
          f"con chó eiii🤣 {chon_name}",
          f"ổn k em {chon_name}",
          f"kh ổn r à {chon_name}",
          f"mày óc à con chó bẻm=)) {chon_name}",
          f"mẹ mày ngu à {chon_name}",
          f"bú cặc cha m k em {chon_name}",
          f"thg giả gái :)) {chon_name}",
          f"coi nó ngu kìa ae {chon_name}",
          f"con chó này giả ngu à {chon_name}",
          f"m ổn k {chon_name}",
          f"mồ côi kìa {chon_name}",
          f"sao v sợ r à {chon_name}",
          f"cố gắng tí em {chon_name}",
          f"cay cú lắm r {chon_name}",
          f"đấy đấy bắt đầu {chon_name}",
          f"chảy nước đái bò r à em {chon_name}",
          f"sao kìa đừng run {chon_name}",
          f"mày run à:)) {chon_name}",
          f"thg dái lở {chon_name}",
          f"cay mẹ m lắm {chon_name}",
          f"lgbt xuất trận à con đĩ {chon_name}",
          f"thg cặc giết cha mắng mẹ {chon_name}",
          f"sủa mạnh eii {chon_name}",
          f"mày chết r à:)) {chon_name}",
          f"sao chết kìa {chon_name}",
          f"bị t hành nên muốn chết à {chon_name}",
          f"con lồn ngu=)) {chon_name}",
          f"sao kìa {chon_name}",
          f"mạnh lên kìa {chon_name}",
          f"yếu sinh lý à {chon_name}",
          f"sủa đê {chon_name}",
          f"cay à {chon_name}",
          f"hăng đê {chon_name}",
          f"gà kìa ae {chon_name}",
          f"akakaa {chon_name}",
          f"óc chó kìa {chon_name}",
          f"🤣🤣🤣 {chon_name}",
          f"ổn không🤣🤣 {chon_name}",
          f"bất ổn à {chon_name}",
          f"ơ kìaaa {chon_name}",
          f"hăng hái đê {chon_name}",
          f"chạy à 🤣🤣 {chon_name}",
          f"tởn à {chon_name}",
          f"kkkk {chon_name}",
          f"mày dốt à {chon_name}",
          f"cặc ngu {chon_name}",
          f"cháy đê {chon_name}",
          f"chat hăng lên {chon_name}",
          f"cố lên {chon_name}",
          f"mồ côi cay {chon_name}",
          f"cay à {chon_name}",
          f"cn chó ngu {chon_name}",
          f"óc cặc kìa {chon_name}",
          f"đĩ đú:)) {chon_name}",
          f"đú kìa {chon_name}",
          f"cùn v {chon_name}",
          f"r x {chon_name}",
          f"hhhhh {chon_name}",
          f"kkakak {chon_name}",
          f"sao đú đó em {chon_name}",
          f"cac teo a con {chon_name}",
          f"ngu kìa {chon_name}",
          f"chat mạnh đê {chon_name}",
          f"hăng ee {chon_name}",
          f"ơ ơ ơ {chon_name}",
          f"sủa cháy đê {chon_name}",
          f"sủa mạnh eei {chon_name}",
          f"mày óc à con {chon_name}",
          f"tao cho m chạy à {chon_name}",
          f"con đĩ ngu sủa? {chon_name}",
          f"mày chạy à con đĩ lồn {chon_name}",
          f"co len con {chon_name}",
          f"son hang len em {chon_name}",
          f"sao m yeu v {chon_name} ",
          f"co ti nua {chon_name}",
          f"sao kia cham a {chon_name}",
          f"hang hai len ti chu {chon_name}",
          f"toi sang di {chon_name}",
          f"co gang ti con cho {chon_name}",
          f"yeu v con {chon_name}",
          f"con cho {chon_name} co de",
          f"sao m cam kia {chon_name}",
          f"ga v {chon_name}",
          f"may so a k dam chat hang ak {chon_name}",
          f"m ga ma {chon_name}",
          f"may ngu ro ma {chon_name}",
          f"con {chon_name} an hai ma",
          f"cai cun ak {chon_name}",
          f"may con gi khac ko vay {chon_name}",
          f"hoc dot nen nhay dot ak {chon_name}",
          f"co ti di em {chon_name}",
          f"meu a {chon_name}",
          f"sao meu kia {chon_name}",
          f"tao da cho m meu dau {chon_name}",
          f"va le di con {chon_name} dot",
          f"sao kia {chon_name}",
          f"tu bo r a {chon_name}",
          f"manh me ti di con {chon_name}",
          f"co len con cho {chon_name} ngu",
          f"😆 cay tao a con di {chon_name}",
          f"so tao a {chon_name}",
          f"sao cham roi kia {chon_name}",
          f"cay lam phai kh {chon_name}",
          f"{chon_name} ot anh cmnr",
          f"may con choi a {chon_name}",
          f"lam ti keo de {chon_name}",
          f"moi do da met r ha {chon_name}",
          f"sao ga ma son v {chon_name}",
          f"son nhu luc dau cho tao di con {chon_name} dot",
          f"sao duoi roi kia {chon_name}",
          f"ai cho m nhai vay {chon_name}",
          f"cay lam r a {chon_name}",
          f"tu bo di em {chon_name}",
          f"may nghi may lam t cay dc ha {chon_name}",
          f"m dang cay ma {chon_name}",
          f"tao dang hanh m ma {chon_name}",
          f"keo nhay kg ay {chon_name}",
          f"con mo coi {chon_name}",
          f"co len {chon_name} oc cho",
          f"hang tiep di {chon_name}",
          f"toi sang k em {chon_name}",
          f"met roi ha {chon_name}",
          f"speed ti dc ko {chon_name}",
          f"m ga ma {chon_name}",
          f"thay phien a {chon_name}",
          f"tui anh thay phien ban vo loz me con {chon_name} ma kaka",
          f"so tao a con cho {chon_name}",
          f"anh win me roi {chon_name} dot",
          f"ga ma hay the hien ha {chon_name}",
          f"con mo coi {chon_name} keo cai ko em",
          f"co len de {chon_name}",
          f"sao moi 1 ti ma da cam roi {chon_name}",
          f"yeu vay ak {chon_name}",
          f"sao kia {chon_name}",
          f"bat luc r ak {chon_name}",
          f"tim cach roi ha {chon_name}",
          f"ai cuu dc m a :)) {chon_name}",
          f"anh ba cmnr ma {chon_name}",
          f"sao m ga vay {chon_name}",
          f"hang le cho tao di {chon_name}",
          f"con mo coi {chon_name}",
          f"on k em {chon_name}",
          f"bat on roi a {chon_name}",
          f"may oc a con cho {chon_name}",
          f"me may ngu a {chon_name}",
          f"bu cac cha m k em {chon_name}",
          f"mo coi {chon_name} cay anh ha",
          f"me m dot tu roi a {chon_name}",
          f"phe vay {chon_name}",
          f"m on k {chon_name}",
          f"mo coi kia {chon_name}",
          f"sao v so r a {chon_name}",
          f"co gang ti em {chon_name}",
          f"cay cu lam r ha {chon_name}",
          f"dien dai di em {chon_name}",
          f"chay nuoc dai bo r a em {chon_name}",
          f"sao kia dung so anh ma {chon_name}",
          f"may run a:)) {chon_name}",
          f"thg {chon_name} mo coi",
          f"cay tao lam ha {chon_name}",
          f"lgbt len phim ngu ak em {chon_name}",
          f"thg cac giet cha mang me {chon_name}",
          f"sua manh eii {chon_name}",
          f"may chet r a:)) {chon_name}",
          f"sao chet kia {chon_name}",
          f"bi t hanh nen muon chet a {chon_name}",
          f"con {chon_name} loz ngu kaka",
          f"sao kia {chon_name}",
          f"manh len kia {chon_name}",
          f"yeu sinh ly a {chon_name}",
          f"sua de {chon_name}",
          f"cay a {chon_name}",
          f"hang de {chon_name}",
          f"con ga {chon_name}",
          f"phe vat {chon_name}",
          f"oc cho {chon_name}",
          f"me m bi t du hap hoi kia con {chon_name}",
          f"on ko em {chon_name}",
          f"bat on ak {chon_name}",
          f"o kiaaa sao vayy {chon_name}",
          f"hang hai de {chon_name}",
          f"chay ak {chon_name}",
          f"so ak {chon_name}",
          f"quiu luon roi ak {chon_name}",
          f"may dot ak {chon_name}",
          f"cac ngu {chon_name}",
          f"chay de {chon_name}",
          f"chat hang len {chon_name}",
          f"co len {chon_name}",
          f"{chon_name} mo coi",
          f"cn cho ngu {chon_name}",
          f"oc cac {chon_name}",
          f"di du {chon_name}",
          f"du kia {chon_name}",
          f"cun v {chon_name}",
          f"r luon con {chon_name} bi ngu roi",
          f"met r am {chon_name}",
          f"kkakak",
          f"sao du {chon_name}",
          f"cac con {chon_name}",
          f"ngu kia {chon_name}",
          f"chat manh de {chon_name}",
          f"hang ee {chon_name}",
          f"clm thk oc cho {chon_name}",
          f"sua chay de {chon_name}",
          f"sua manh eei {chon_name}",
          f"may oc a con {chon_name}",
          f"tao cho m chay a {chon_name}",
          f"con mo coi {chon_name}",
          f"may chay a con di lon {chon_name}",
          f"sua de {chon_name}",
          f"con phen {chon_name}",
          f"bat on ho {chon_name}",
          f"s do  {chon_name}",
          f"sua lien tuc de {chon_name}",
          f"moi tay ak {chon_name}",
          f"choi t giet cha ma m ne {chon_name}",
          f"hang xiu de {chon_name}",
          f"th ngu {chon_name}",
          f"len daica bieu ne {chon_name}",
          f"sua chill de {chon_name}",
          f"m thich du ko da {chon_name}",
          f"son hang dc kg {chon_name}",
          f"cam chay nhen {chon_name}",
          f"m mau de {chon_name}",
          f"duoi ak {chon_name}",
          f"th ngu {chon_name}",
          f"con {chon_name} len day anh sut chet me may",
          f"m khoc ak {chon_name}",
          f"sua lien tuc de {chon_name}",
          f"thg {chon_name} cho dien",
          f"bi ngu ak {chon_name}",
          f"speed de {chon_name}",
          f"cham v cn culi {chon_name}",
          f"hoang loan ak {chon_name}",
          f"bat on ak {chon_name}",
          f"run ak {chon_name}",
          f"chay ak {chon_name}",
          f"duoi ak {chon_name}",
          f"met r ak {chon_name}",
          f"sua mau {chon_name}",
          f"manh dan len {chon_name}",
          f"nhanh t cho co hoi cuu ma m ne {chon_name}",
          f"cam mach me nha {chon_name}",
          f"ao war ak {chon_name}",
          f"tk {chon_name} dot v ak",
          f"cham chap ak {chon_name}",
          f"th cho bua m sao v {chon_name}",
          f"th dau buoi mat cho {chon_name}",
          f"cam hoang loan ma {chon_name}",
          f"lo lo sao may cam v {chon_name}",
          f"ai cho may cam vayy {chon_name}",
          f"anh cho chx ay=)) {chon_name}",
          f"cmm hai a {chon_name}",
          f"hai vay em {chon_name}",
          f"co gi khac khong {chon_name}",
          f"khong a {chon_name}",
          f"ga den vay a {chon_name}",
          f"thang an hai lien tuc di {chon_name}",
          f"bi anh dap dau ma {chon_name}",
          f"cay cu anh lam dk {chon_name}",
          f"âkkak sua di em {chon_name}",
          f"ccho ngu sua {chon_name}",
          f"xem ns occho kia {chon_name}",
          f"ngu hay sua a👉😏 {chon_name}",
          f"alo alo cdy ngu {chon_name}👉🤪",
          f"leg keg loc troc lay sa beg dap dau may {chon_name}👉🤣",
          f"sua hang hai ti di em ey {chon_name}👉🤪",
          f"may vua sua bi tao lay sa beg dap vo 2 hon trug dai ma {chon_name}👉😋",
          f"o o cn culi {chon_name} bia ngu a👉🤣🤣",
          f"cay anh ma lmj dc anh dau {chon_name} dk🤞🤞",
          f"culi {chon_name} cn oc bem a con😋",
          f"sao do coan zai {chon_name} cn sua dc khong ay👉😏",
          f"khong a {chon_name}🤣🤣",
          f"anh biet anh ba ma {chon_name}",
          f"ccho ngu hay sua a {chon_name}🤪🤪",
          f"mat may nhu trai ot roi kia {chon_name}🤣🤣",
          f"ngu ngu bi anh dap dau vo cot dien chetme may nha {chon_name}🤣🤣",
          f"anh thog minh vcll ma {chon_name}🤪🤪",
          f"may ngu nguc vcll ma em {chon_name}🤣🤣",
          f"dk {chon_name} em😏🤞",
          f"dung a {chon_name}🤣🤣",
          f"may lam tao cuoi dc roi ds {chon_name}🤪🤞",
          f"dien siet duoc roi do {chon_name} ngu ey🤣🤣",
          f"anh chuc may dien ko ai coi nha {chon_name}👉🤣",
          f"bi anh hanh ha den die dk {chon_name}😏🤞",
          f"anh dap chetme may ma {chon_name} em🤣🤣",
          f"sua lam vay {chon_name} kiki🤣🤣",
          f"cn me nay hap hoi a {chon_name}👉😏🤞",
          f"may bua nhan a {chon_name}🤣🤣",
          f"run ray khi gap a ma {chon_name}🤪🤞",
          f"anh len san la may khiep so dk {chon_name}🤣🤣",
          f"do ah ba qua nen may so dk {chon_name}👉😏",
          f"may van xin anh tha thu ma {chon_name}😝🙏",
          f"tao cam ak47 na vo dau mat chetme may {chon_name}😝🙏",
          f"may sua dien cuong di {chon_name}🤣🤣",
          f"cmm ngu the em {chon_name}🤣🤞",
          f"ai ngu = may nua dau {chon_name} em 👉🤣🤞",
          f"may nhu culi giang tran vay {chon_name}🤣🤣",
          f"may ma culi j may lgbt ma {chon_name} em🤣",
          f"anh Đức Phát ba dao san war ma {chon_name} cu😝👎",
          f"may an cut san treo ma {chon_name} 👉🤣🤞",
          f"bu cut tao song qua ngay ma {chon_name}🤣🤣",
          f"xao lon cn gay a {chon_name}😝",
          f"culi biet sua la day a {chon_name}😏🤞",
          f"ga ma gay quai vay {chon_name}🤪👌",
          f"may can ngon roi a {chon_name}😏🤞",
          f"con gi khac hon khong {chon_name}🤪🤪",
          f"khog a {chon_name}🤣",
          f"ngu den vay la cung ha {chon_name}😏🤞",
          f"sao may phe nhan vay😏🤞",
          f"con nghich tu phan loan {chon_name}🤣🤣",
          f"con cho chiu so phan di {chon_name}😏🤞",
          f"chiu so phan bi anh dam cha giet ma {chon_name} ha🤣🤣",
          f"anh cs hoi dau may tu tra loi a {chon_name}🤣",
          f"tk bua nhan {chon_name}😏🤞",
          f"sao culi khong sua nx di {chon_name}🤣🤣",
          f"nin ngon roi a {chon_name}🤣🤪",
          f"gap phai cha la may phai ngam ot roi {chon_name}🤣🤣",
          f"ngon xam cac lay len doi bem ah a tk culi {chon_name}🤪🤞",
          f"cn cali mat mam sua j ay {chon_name}😏🤞",
          f"len nhay vs ah toi trang tron di {chon_name}😝",
          f"sao ay tai mat roi a {chon_name}🤣🤣",
          f"so lam roi a {chon_name}😏🤞",
          f"co may anh da dau may toi chet me {chon_name}🤣",
          f"dcm cay cu anh a {chon_name}🤣🤣",
]
      clear()
      runbanner(chontool)
      delay=int(input(f'\033[1;31m[\033[1;37mTAT07\033[1;31m] {xanhnhat}Nhập Delay [Khuyến Cáo Trên 10s] :{vang} '))
      print("\033[1;31m────────────────────────────────────────────────────────────")
      while True:
        try:
          ping = requests.get("https://www.google.com")
          if ping.status_code == 200:
            for nd in CAU_CHUI:
                data = f"fb_dtsg={fb_dtsg}&jazoest={jazoest}&body={nd}&send=Send&tids=cid.g.{idcanspam}&wwwupp=C3&platform_xmd=&referrer=&ctype=&cver=legacy&csid=366a74a7-2d30-45dd-94c2-ad47d662dcfb"  
                response = requests.post("https://mbasic.facebook.com/messages/send/", params=params, headers=headers, data=data.encode('utf-8'))
                chonname = chon_name
                NOIDUNG = f"\033[1;35m[ID BOX: {idcanspam}] \033[1;32m[{nd}\033[1;32m] => \033[1;35mTRẠNG THÁI\033[1;97m: {xanh_la}Nhây Thành Công"
                print(f"{NOIDUNG}")
                idelay(delay)
        except Exception as e:
          print(f"{do}EORRO!")
          time.sleep(5)