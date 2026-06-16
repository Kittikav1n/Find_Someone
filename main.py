import questionary
import requests
import pyfiglet
import shutil
import sys
import time
import os
from screen import clear_screen, Home_screen, Mission1_screen, Mission2_screen

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
        send_spy_log("MISSION 1", "🔹 น้องเลือก Mission 1", color=15158332)
        return Game_1() 
    else:
        send_spy_log("GAME EXITED", "⚠️ น้องเลือกออกจากเกม", color=15158332)
        print("\n[!] SYSTEM: บาย!")
        sys.exit()            
        return
    
def Choose_Mission2():
    clear_screen()
    Home_screen()
    choice = questionary.select(
    "[!] เลือกภารกิจที่จะทำ:",
    choices = ["[⭕️] ภารกิจที่ 2 : หา OUTPUT ให้หน่อย 😩", "[❌] ออกจากเกม "]
    ).ask()
    if choice == "[⭕️] ภารกิจที่ 2 : หา OUTPUT ให้หน่อย 😩":
        send_spy_log("MISSION 2", "🔹 น้องเลือก Mission 2", color=15158332)
        Game_2()
    else:
        send_spy_log("GAME EXITED", "⚠️ น้องเลือกออกจากเกม", color=15158332)
        print("\n[!] SYSTEM: บาย!")
        sys.exit()            
        return

# ---- game1 ----
def Game_1():
    Mission1_screen()
    unlock = 1
    while True:
        if unlock == 5:
            clear_screen()
            terminal_width = shutil.get_terminal_size().columns
            full_border = "=" * terminal_width
            ascii_banner = pyfiglet.figlet_format(" MISSION 1 SUCCEED ", font="slant")
            print()
            print(full_border)
            for line in ascii_banner.splitlines():
                print(line.center(terminal_width))
            print(full_border)
            print("\n" + "🎉 ยินดีด้วย! คุณผ่านภารกิจถอดรหัสลับครบถ้วนแล้ว 🎉".center(terminal_width))
            
            input("\n" + "(กด Enter เพื่อบันทึกข้อมูลและกลับสู่หน้าหลัก...)".center(terminal_width))
            clear_screen()
            Home_screen()
            return True

        Mission1_screen()
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
            
        # ---- Level 1 ----
        elif "Level 1" in Choose_level:
            if unlock < 1:
                print("\n🔒 [ACCESS DENIED]: ด่านนี้ถูกล็อกอยู่!")
                time.sleep(1)
                continue

            while True: 
                Mission1_screen()
                send_spy_log("MISSION1 LEVEL 1", "🔹 น้องเลือก Level 1: ง่ายสุดสุด", color=3066993)

                print("LVEVL 1: ง่ายสุดสุด")
                print("\nรหัสปริศนา: 01011010 01000101 01010010 01001111 00100000 01010100 01001000 01010010 01000101 01000101")
                
                ans = questionary.text("ถอดรหัสนี้ (พิมพ์ตัวพิมพ์ใหญ่อังกฤษ): ").ask()
                
                if ans.lower() == "exit":
                    print("\n[!] SYSTEM: กลับสู่หน้าหลัก...\n")
                    send_spy_log("MISSION1 EXITED", "⚠️ น้องออกจากภารกิจ 1 (พิมพ์ exit ออกจากด่าน)", color=15158332)
                    break
                
                if ans.strip() == "ZERO THREE":
                    print("\n⭕️ ถูกต้อง! คุณผ่าน Level 1 แล้ว!")
                    send_spy_log("MISSION 1", "⭕️ ผ่าน Level 1 ", color=3066993)
                    unlock = max(unlock, 2) # ปลดล็อกด่าน 2
                    time.sleep(0.5)
                    clear_screen()
                    break 
                else:
                    print("\n❌ คำตอบผิด! ลองใหม่นะ")
                    send_spy_log("MISSION 1", "❌ น้องตอบผิด : " + ans , color=15158332)
                    time.sleep(0.5)
                    clear_screen()

        # ---- Level 2 ----

        elif "Level 2" in Choose_level:
            if unlock < 2:
                print("\n🔒 [ACCESS DENIED]: คุณต้องผ่าน Level 1 ก่อน!")
                time.sleep(0.5)
                continue

            while True:
                Mission1_screen()
                send_spy_log("MISSION1 LEVEL 2", "🔹 น้องเลือก Level 2: ง่าย", color=3066993)
                
                print("LVEVL 2: ง่าย")
                print("\nรหัสปริศนา: 4F 4E 45 20 45 49 47 48 54 20 46 49 56 45")
                
                ans = questionary.text("ถอดรหัสนี้ (พิมพ์ตัวพิมพ์ใหญ่อังกฤษ): ").ask()
                
                if ans.lower() == "exit":
                    print("\n[!] SYSTEM: กลับสู่หน้าหลัก...\n")
                    send_spy_log("MISSION1 EXITED", "⚠️ น้องออกจากภารกิจ 1 (พิมพ์ exit ออกจากด่าน)", color=15158332)
                    break
                
                if ans.strip() == "ONE EIGHT FIVE":
                    print("\n⭕️ ถูกต้อง! คุณผ่าน Level 2 แล้ว!")
                    send_spy_log("MISSION 1", "⭕️ ผ่าน Level 2 ", color=3066993)
                    unlock = max(unlock, 3) # ปลดล็อกด่าน 3
                    time.sleep(0.5)
                    clear_screen()
                    break
                else:
                    print("\n❌ คำตอบผิด! ลองใหม่นะ")
                    send_spy_log("MISSION 1", "❌ น้องตอบผิด : " + ans , color=15158332)
                    time.sleep(0.5)
                    clear_screen()

        # ---- Level 3 ----

        elif "Level 3" in Choose_level:
            if unlock < 3:
                print("\n🔒 [ACCESS DENIED]: คุณต้องผ่าน Level 2 ก่อน!")
                time.sleep(0.5)
                continue

            while True:
                Mission1_screen()
                send_spy_log("MISSION1 LEVEL 3", "🔹 น้องเลือก Level 3: เริ่มยาก", color=3066993)
                
                print("LVEVL 3: เริ่มยาก")
                print("\nรหัสปริศนา: QUNT")
                
                ans = questionary.text("ถอดรหัสนี้ (พิมพ์ตัวพิมพ์ใหญ่อังกฤษ): ").ask()
                
                if ans.lower() == "exit":
                    print("\n[!] SYSTEM: กลับสู่หน้าหลัก...\n")
                    send_spy_log("MISSION1 EXITED", "⚠️ น้องออกจากภารกิจ 1 (พิมพ์ exit ออกจากด่าน)", color=15158332)
                    break
                    
                if ans.strip() == "ACS":
                    print("\n⭕️ ถูกต้อง! คุณผ่าน Level 3 แล้ว!")
                    send_spy_log("MISSION 1", "⭕️ ผ่าน Level 3 ", color=3066993)
                    unlock = max(unlock, 4) # ปลดล็อกด่าน 4
                    time.sleep(0.5)
                    clear_screen()
                    break
                else:
                    print("\n❌ คำตอบผิด! ลองใหม่นะ")
                    send_spy_log("MISSION 1", "❌ น้องตอบผิด : " + ans , color=15158332)
                    time.sleep(0.5)
                    clear_screen()

        # ---- Level 4 ----

        elif "Level 4" in Choose_level:
            if unlock < 4:
                print("\n🔒 [ACCESS DENIED]: คุณต้องผ่าน Level 3 ก่อน!")
                time.sleep(0.5)
                continue

            while True:
                Mission1_screen()
                send_spy_log("MISSION1 LEVEL 4", "🔹 น้องเลือก Level 4: ยากนิดๆ", color=3066993)
                
                print("LVEVL 4: ยากนิดๆ")
                print("\nรหัสปริศนา: 77 65 76 69")
                
                ans = questionary.text("ถอดรหัสนี้ (พิมพ์ตัวพิมพ์ใหญ่อังกฤษ): ").ask()
                
                if ans.lower() == "exit":
                    print("\n[!] SYSTEM: กลับสู่หน้าหลัก...\n")
                    send_spy_log("MISSION1 EXITED", "⚠️ น้องออกจากภารกิจ 1 (พิมพ์ exit ออกจากด่าน)", color=15158332)
                    break
                    
                if ans.strip() == "MALE":
                    print("\n⭕️ ถูกต้อง! คุณผ่าน Level 4 แล้ว!")
                    send_spy_log("MISSION 1", "⭕️ ผ่าน Level 4 ", color=3066993)
                    time.sleep(0.5)
                    unlock = 5 
                    clear_screen()
                    break
                else:
                    print("\n❌ คำตอบผิด! ลองใหม่นะ")
                    send_spy_log("MISSION 1", "❌ น้องตอบผิด : " + ans , color=15158332)
                    time.sleep(0.5)
                    clear_screen()            
            continue 


def Game_2():
    Mission2_screen()
    unlock = 1
    while True:
        if unlock == 5:
            clear_screen()
            terminal_width = shutil.get_terminal_size().columns
            full_border = "=" * terminal_width
            ascii_banner = pyfiglet.figlet_format(" MISSION 2 SUCCEED ", font="slant")
            print()
            print(full_border)
            for line in ascii_banner.splitlines():
                print(line.center(terminal_width))
            print(full_border)
            print("\n" + "🎉 ยินดีด้วย! คุณผ่านภารกิจหา OUTPUT ครบถ้วนแล้ว 🎉".center(terminal_width))
            
            input("\n" + "(กด Enter เพื่อบันทึกข้อมูลและกลับสู่หน้าหลัก...)".center(terminal_width))
            clear_screen()
            Home_screen()
            return True

        Mission2_screen()
        Choose_level = questionary.select(
            "เลือกระดับความยากของภารกิจนี้:",
            choices=[
                f"{'⭕️' if unlock >= 1 else '❌'} [ Level 1 ] ง่าย ",
                f"{'⭕️' if unlock >= 2 else '❌'} [ Level 2 ] ง่ายย ",
                f"{'⭕️' if unlock >= 3 else '❌'} [ Level 3 ] ง่ายยย ",
                f"{'⭕️' if unlock >= 4 else '❌'} [ Level 4 ] ง่ายยยย ",
                "👋 [  EXIT.  ] ออกจากภารกิจ "
            ]
        ).ask()

        if Choose_level == "👋 [  EXIT.  ] ออกจากภารกิจ ":
            print("\n[!] SYSTEM: กลับสู่หน้าหลัก...\n")
            send_spy_log("MISSION1 EXITED", "⚠️ น้องออกจากภารกิจ 1", color=15158332)
            Choose_Mission2()
            break
    

        
def main():
    Home_screen()

    # --- เริ่ม ---    
    send_spy_log("GAME START", "🔹 เปิดรันสคริปต์เกมสำเร็จแล้ว!", color=3447003)

    if rigis_ID():
        if Choose_Choices_1():
            if Choose_Mission():
                Choose_Mission2()

        
    

    


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # ดักกรณีถ้าน้องกวนประสาทกด Ctrl+C เพื่อปิดโปรแกรมกลางคัน
        send_spy_log("GAME CLOSED", "⚠️ น้องกด Ctrl+C ปิดโปรแกรมกลางคัน", color=9807270)
        print("\n\n[!] สัญญาณขาดหาย...") 