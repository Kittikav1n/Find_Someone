import questionary
import requests
import pyfiglet
import shutil
import sys
import time
import os

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1515767749178167418/9m9tDhjpIzsyXYyrtOVvOhC_bebV8dKMh9B8sE2b_Yz1EPK1YvoOgzOlRNDwn0xuroFh"

def send_spy_log(status, message, color=3066993):
    if "เอาลิงก์" in DISCORD_WEBHOOK_URL or not DISCORD_WEBHOOK_URL:
        return  
        
    payload = {
        "embeds": [{
            "title": f"🔍 [{status}]", # สถานะ
            "description": message, # ข้อความ
            "color": color, # สีข้อความ
            "timestamp": time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
        }]
    }
    try:
        requests.post(DISCORD_WEBHOOK_URL, json=payload, timeout=3)
    except:
        pass 

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def Home_screen():
    clear_screen()
    terminal_width = shutil.get_terminal_size().columns
    full_border = "=" * terminal_width
    ascii_banner = pyfiglet.figlet_format(" ACS 69 ", font="slant")
    print()
    print(full_border.center(terminal_width))
    for line in ascii_banner.splitlines():
        print(line.center(terminal_width))
    print(" " * 2 + " Applied Computer Science ".center(terminal_width))
    print(full_border.center(terminal_width))
    print()

# ---- rigister ID ----

def rigis_ID():
    while True:
        id_input = questionary.text("กรอกรหัสนักศึกษา ( 11 หลัก ) ของคุณ:").ask()
        if id_input == "69090500403":
            send_spy_log("ID REGISTERED", "⭕️ น้องกรอกรหัสนักศึกษาถูกต้องแล้ว!", color=3066993)
            print("\n[!] รหัสนักศึกษาถูกต้องแล้ว! ยินดีต้อนรับสู่เกมตามหาพี่รหัส!\n")
            time.sleep(2)
            clear_screen()
            Home_screen()
            return True
        else:
            send_spy_log("ID REGISTERED", "❌ น้องกรอกรหัสนักศึกษาไม่ถูกต้อง!", color=3066993)
            print("\n[!] รหัสนักศึกษาไม่ถูกต้อง!...มึงใคร!?\n")
            return False

# ---- เริ่มเกม ----
def Choose_Choices_1():
    clear_screen()
    Home_screen()
    ready = questionary.select(
        "คุณพร้อมที่จะเริ่มต้นภารกิจตามหาพี่รหัสแล้วหรือยัง?",
        choices=["[ ⭕️ ] ฉันพร้อมแล้ว!", "[ ❌ ] ไม่อะ ขอผ่านก่อน"]
    ).ask()
    if ready == "[ ⭕️ ] ฉันพร้อมแล้ว!":
        send_spy_log("PLAYER READY", "⭕️ น้องกดเริ่มเกมแล้ว กำลังจะเข้าสู่ด่านถัดไป", color=1752220)
        #time.sleep(1)
        return True
    else:
        send_spy_log("GAME OVER", "❌ น้องกดปฏิเสธตั้งแต่หน้าแรก (จบเกม)", color=15158332)
        print("\n[!] SYSTEM: พี่รหัสเซ็ง... บาย!")
        sys.exit()
        return False




# ---- เลือกภารกิจ ----
def Choose_Mission():
    clear_screen()
    Home_screen()
    choice = questionary.select(
    "[!] เลือกภารกิจที่จะทำ:",
    choices = ["[⭕️] ภารกิจที่ 1 : ถอดรหัสลับ", "[❌] ออกจากเกม "]
    ).ask()
    if choice == "[⭕️] ภารกิจที่ 1 : ถอดรหัสลับ":
        Game_1()
    else:
        send_spy_log("GAME EXITED", "⚠️ น้องเลือกออกจากเกม", color=15158332)
        print("\n[!] SYSTEM: บาย!")
        sys.exit()            
        return


# ---- game1 ----
def Game_1():
    clear_screen()
    terminal_width = shutil.get_terminal_size().columns
    full_border = "=" * terminal_width
    ascii_banner = pyfiglet.figlet_format(" MISSION 1 ", font="slant")
    print()
    print(full_border.center(terminal_width))
    for line in ascii_banner.splitlines():
        print(line.center(terminal_width))
    print(" " * 15 +"ภารกิจที่ 1: ถอดรหัสลับ".center(terminal_width))
    print(full_border.center(terminal_width))
    print()

    unlock = 1
    while True:
        Choose_level = questionary.select(
            "เลือกระดับความยากของภารกิจนี้:",
            choices=[
                f"{'⭕️' if unlock >= 1 else '❌'} [ Level 1 ] ง่ายสุดสุด ",
                f"{'⭕️' if unlock >= 2 else '❌'} [ Level 2 ] ง่าย ",
                f"{'⭕️' if unlock >= 3 else '❌'} [ Level 3 ] เริ่มยาก ",
                f"{'⭕️' if unlock >= 4 else '❌'} [ Level 4 ] ยากนิดๆ ",
                "👋 [  EXIT.  ] ออกจากภารกิจ "
            ]
        ).ask()

        if Choose_level == "👋 [  EXIT.  ] ออกจากภารกิจ ":
            print("\n[!] SYSTEM: กลับสู่หน้าหลัก...\n")
            send_spy_log("MISSION1 EXITED", "⚠️ น้องออกจากภารกิจ 1", color=15158332)
            Choose_Mission()
            break
            
        # Level 1
        elif Choose_level == f"{'⭕️' if unlock >= 1 else '❌'} [ Level 1 ] ง่ายสุดสุด " and unlock >= 1:
            clear_screen()
            terminal_width = shutil.get_terminal_size().columns
            full_border = "=" * terminal_width
            ascii_banner = pyfiglet.figlet_format(" MISSION 1 ", font="slant")
            print()
            print(full_border.center(terminal_width))
            for line in ascii_banner.splitlines():
                print(line.center(terminal_width))
            print(" " * 15 +"ภารกิจที่ 1: ถอดรหัสลับ".center(terminal_width))
            print(full_border.center(terminal_width))
            print()

            send_spy_log("MISSION1 LEVEL 1", "🔹 น้องเลือก Level 1: ง่ายสุดสุด", color=3066993)

            print("\nรหัสปริศนา: 01000001 01000011 01010011")
            ans = questionary.text("ถอดรหัสนี้ (พิมพ์ตัวพิมพ์ใหญ่อังกฤษ 3 ตัว): ").ask()
            while True:
                if ans.lower() == "exit":
                    print("\n[!] SYSTEM: กลับสู่หน้าหลัก...\n")
                    send_spy_log("MISSION1 EXITED", "⚠️ น้องออกจากภารกิจ 1 (พิมพ์ exit ออกจากด่าน)", color=15158332)
                    Choose_Mission()
                    return
                if ans == "ACS":
                    print("\n⭕️ ถูกต้อง! คุณผ่าน Level 1 แล้ว!")
                    send_spy_log("MISSION 1", "⭕️ ผ่าน Level 1 (ถอดรหัส ACS)", color=3066993)
                    unlock = max(unlock, 2) # ปลดล็อกด่าน 2
                    input("\n(กด Enter เพื่อกลับไปหน้าเมนู...)\n")
                    break
                else:
                    print("\n❌ คำตอบผิด! ลองใหม่นะ")
                    send_spy_log("MISSION 1", "❌ น้องตอบผิด : " + ans , color=15158332)
                    time.sleep(2)
                    clear_screen()
                    break
                    

                    
            



    
    



def main():
    Home_screen()

    # --- เริ่ม ---    
    send_spy_log("GAME START", "🔹 เปิดรันสคริปต์เกมสำเร็จแล้ว!", color=3447003)

    if rigis_ID():
        if Choose_Choices_1():
            Choose_Mission()
        
    

    


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # ดักกรณีถ้าน้องกวนประสาทกด Ctrl+C เพื่อปิดโปรแกรมกลางคัน
        send_spy_log("GAME CLOSED", "⚠️ น้องกด Ctrl+C ปิดโปรแกรมกลางคัน", color=9807270)
        print("\n\n[!] สัญญาณขาดหาย...") 