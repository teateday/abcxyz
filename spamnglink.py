import requests
import os
from pystyle import Colors, Colorate
import time

def ngl():
    
    G = "\033[1;32m"
    W = "\033[0;37m" 
    R = "\033[1;31m"  

    os.system('cls' if os.name == 'nt' else 'clear')

    print(Colorate.Vertical(Colors.cyan_to_blue,"""
 █████╗ ███╗   ██╗██╗  ██╗████████╗██╗   ██╗ █████╗ ███╗   ██╗
██╔══██╗████╗  ██║██║  ██║╚══██╔══╝██║   ██║██╔══██╗████╗  ██║
███████║██╔██╗ ██║███████║   ██║   ██║   ██║███████║██╔██╗ ██║
██╔══██║██║╚██╗██║██╔══██║   ██║   ██║   ██║██╔══██║██║╚██╗██║
██║  ██║██║ ╚████║██║  ██║   ██║   ╚██████╔╝██║  ██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝
            Copyright By: @TAT07-ExE | Xin Chào!"""))
    print (Colorate.Diagonal(Colors.blue_to_red, "--------------------------------------------------------------"))
    print (Colorate.Diagonal(Colors.blue_to_red, "[</>] => Tool Spam NgLink MaxSpeed V1"))
    print (Colorate.Diagonal(Colors.blue_to_red, "[</>] => Box Tele: https://t.me/sharesrctool"))
    print (Colorate.Diagonal(Colors.blue_to_red, "[</>] => YouTube: https://www.youtube.com/@sharesrctool"))
    print (Colorate.Diagonal(Colors.blue_to_red, "[</>] => Admin: Tran Anh Tuan [TAT07] "))
    print (Colorate.Diagonal(Colors.blue_to_red, "--------------------------------------------------------------"))
    
    nglusername = input(Colorate.Vertical(Colors.blue_to_purple,"[</>] => Username [Bỏ @]:  "))
    message = input(Colorate.Vertical(Colors.blue_to_purple,"[</>] => Nội Dung Message:  "))
    Count = int(input(Colorate.Vertical(Colors.blue_to_purple,"[</>] => Số Lượng:  ")))
    print(Colorate.Vertical(Colors.blue_to_red,"--------------------------------------------------------------"))
    time.sleep(0.05)
    print(Colorate.Vertical(Colors.blue_to_red,"[</>] => Bắt Đầu Spam "))
    time.sleep(0.05)

    value =0
    notsend =0
    while value < Count:
        headers = {
            'Host': 'ngl.link',
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'accept': '*/*',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'x-requested-with': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            'sec-ch-ua-platform': '"Windows"',
            'origin': 'https://ngl.link',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': f'https://ngl.link/{nglusername}',
            'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        data = {
            'username': f'{nglusername}',
            'question': f'{message}',
            'deviceId': '0',
            'gameSlug': '',
            'referrer': '',
        }

        response = requests.post('https://ngl.link/api/submit',headers=headers, data=data)
        if response.status_code == 200:
            notsend = 0
            value += 1
            print(G+"[TAT07] "+W+"| Spam Thành Công | "+G+"✈ ✈ ✈ "+R+" [ {} ]".format(value)+W)
        else:
            notsend += 1
            print(R+"[-]"+W+"Not Send")
        if notsend == 10:
            print(R+"[!]"+W+"Wait 5 Seconds")
            time.sleep(5)
            notsend = 0
ngl()
