import questionary
import requests
import pyfiglet
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

def welcome_screen():
    print("=" * 43)
    print()
    ascii_banner = pyfiglet.figlet_format(" ACS 69 ", font="slant")
    print(ascii_banner)
    print("=" * 43)
    print()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def rigis_ID():
    while True:
        id_input = questionary.text("กรอกรหัสนักศึกษา ( 11 หลัก ) ของคุณ:").ask()
        if id_input == "69090500403":
            send_spy_log("ID REGISTERED", "⭕️ น้องกรอกรหัสนักศึกษาถูกต้องแล้ว!", color=3066993)
            print("\n[!] รหัสนักศึกษาถูกต้องแล้ว! ยินดีต้อนรับสู่เกมตามหาพี่รหัส!\n")
            return True
        else:
            send_spy_log("ID REGISTERED", "❌ น้องกรอกรหัสนักศึกษาไม่ถูกต้อง!", color=3066993)
            print("\n[!] รหัสนักศึกษาไม่ถูกต้อง!...มึงใคร!?\n")
            return False






def Choose_Choices_1():

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


def Game_1():
    clear_screen()
    print("=" * 55)
    print()
    print(pyfiglet.figlet_format(" MISSION 1 ", font="slant"))
    print("=" * 55)
    print()
    send_spy_log("MISSION1 START", "🔹 เริ่มภารกิจที่ 1: ถอดรหัสลับ", color=3447003)
    print("\n[!] ภารกิจที่ 1: ถอดรหัสลับ\n")



def main():
    welcome_screen()

    # --- เริ่ม ---    
    send_spy_log("GAME START", "🔹 เปิดรันสคริปต์เกมสำเร็จแล้ว!", color=3447003)

    if rigis_ID():
        if Choose_Choices_1():
            Game_1()
        
    

    


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # ดักกรณีถ้าน้องกวนประสาทกด Ctrl+C เพื่อปิดโปรแกรมกลางคัน
        send_spy_log("GAME CLOSED", "⚠️ น้องกด Ctrl+C ปิดโปรแกรมกลางคัน", color=9807270)
        print("\n\n[!] สัญญาณขาดหาย...") 