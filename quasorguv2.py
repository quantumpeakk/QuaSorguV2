import requests
from colorama import init, Fore, Back, Style
import os
import time

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    clear_screen()
    banner = f"""
{Fore.RED}╔════════════════════════════════════════════════════════════╗
{Fore.RED}║{Fore.CYAN}             QUASORGU PANELİ              v2.0              {Fore.RED}║
{Fore.RED}╚════════════════════════════════════════════════════════════╝
    """
    print(banner)

def check_password():
    password = "lyrica"
    attempts = 3

    while attempts > 0:
        print(f"{Fore.YELLOW}Lütfen şifreyi giriniz (Kalan deneme hakkı: {attempts}):")
        user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}")

        if user_input == password:
            return True
        else:
            print(f"{Fore.RED}Hatalı şifre!{Style.RESET_ALL}")
            attempts -= 1
            time.sleep(1)

    print(f"{Fore.RED}Çok fazla hatalı giriş yaptınız. Program kapatılıyor...")
    time.sleep(2)
    exit()

def ad_soyad_sorgula(ad, soyad):
    url = f"https://api.hexnox.pro/sowixapi/adsoyadilice.php?ad={ad}&soyad={soyad}"
    response = requests.get(url)
    return response.json()

def ad_soyad_il_ilce_sorgula(ad, soyad, il, ilce):
    url = f"https://api.hexnox.pro/sowixapi/adsoyadilce.php?ad={ad}&soyad={soyad}&il={il}&ilce={ilce}"
    response = requests.get(url)
    return response.json()

def tc_pro_sorgula(tc):
    url = f"https://api.hexnox.pro/sowixapi/tcpro.php?tc={tc}"
    response = requests.get(url)
    return response.json()

def gsm_tc_sorgula(gsm):
    url = f"https://api.hexnox.pro/sowixapi/gsm.php?gsm={gsm}"
    response = requests.get(url)
    return response.json()

def tc_gsm_sorgula(tc):
    url = f"https://api.hexnox.pro/sowixapi/tcgsm.php?tc={tc}"
    response = requests.get(url)
    return response.json()

def tapu_sorgula(tc):
    url = f"https://api.hexnox.pro/sowixapi/tapu.php?tc={tc}"
    response = requests.get(url)
    return response.json()

def okul_no_sorgula(tc):
    url = f"https://api.hexnox.pro/sowixapi/okulno.php?tc={tc}"
    response = requests.get(url)
    return response.json()

def sgk_yetkili_sorgula(tc):
    url = f"https://api.hexnox.pro/sowixapi/isyeriyetkili.php?tc={tc}"
    response = requests.get(url)
    return response.json()

def is_yeri_sorgula(tc):
    url = f"https://api.hexnox.pro/sowixapi/isyeri.php?tc={tc}"
    response = requests.get(url)
    return response.json()

def adres_sorgula(tc):
    url = f"https://api.hexnox.pro/sowixapi/adres.php?tc={tc}"
    response = requests.get(url)
    return response.json()

def aile_sorgula(tc):
    url = f"https://api.hexnox.pro/sowixapi/aile.php?tc={tc}"
    response = requests.get(url)
    return response.json()

def print_menu():
    print(f"\n{Fore.CYAN}╔══════════════════════════════════════════════════╗")
    print(f"{Fore.CYAN}║{Fore.YELLOW}       QUASORGU PANELİ V2.00                   {Fore.CYAN}║")
    print(f"{Fore.CYAN}╠══════════════════════════════════════════════════╣")
    print(f"{Fore.CYAN}║{Fore.WHITE} 1. {Fore.GREEN}Ad Soyad Sorgula                     {Fore.CYAN}║")
    print(f"{Fore.CYAN}║{Fore.WHITE} 2. {Fore.GREEN}Ad Soyad İl İlçe Sorgula             {Fore.CYAN}║")
    print(f"{Fore.CYAN}║{Fore.WHITE} 3. {Fore.GREEN}TC Pro Sorgula                       {Fore.CYAN}║")
    print(f"{Fore.CYAN}║{Fore.WHITE} 4. {Fore.GREEN}GSM > TC Sorgula                     {Fore.CYAN}║")
    print(f"{Fore.CYAN}║{Fore.WHITE} 5. {Fore.GREEN}TC > GSM Sorgula                     {Fore.CYAN}║")
    print(f"{Fore.CYAN}║{Fore.WHITE} 6. {Fore.GREEN}Tapu Sorgula                         {Fore.CYAN}║")
    print(f"{Fore.CYAN}║{Fore.WHITE} 7. {Fore.GREEN}Okul No Sorgula                      {Fore.CYAN}║")
    print(f"{Fore.CYAN}║{Fore.WHITE} 8. {Fore.GREEN}SGK Yetkili Sorgula                  {Fore.CYAN}║")
    print(f"{Fore.CYAN}║{Fore.WHITE} 9. {Fore.GREEN}İş Yeri Sorgula                      {Fore.CYAN}║")
    print(f"{Fore.CYAN}║{Fore.WHITE}10. {Fore.GREEN}Adres Sorgula                        {Fore.CYAN}║")
    print(f"{Fore.CYAN}║{Fore.WHITE}11. {Fore.GREEN}Aile Sorgula                         {Fore.CYAN}║")
    print(f"{Fore.CYAN}║{Fore.WHITE} 0. {Fore.RED}Çıkış                                 {Fore.CYAN}║")
    print(f"{Fore.CYAN}╚══════════════════════════════════════════════════╝{Style.RESET_ALL}")

def main():
    print_banner()
    check_password()

    while True:
        print_banner()
        print_menu()

        try:
            secim = input(f"\n{Fore.YELLOW}Lütfen bir seçenek girin (0-11): {Style.RESET_ALL}")

            if secim == "1":
                clear_screen()
                print(f"{Fore.CYAN}╔══════════════════════════════════════════════════╗")
                print(f"{Fore.CYAN}║{Fore.YELLOW}           AD SOYAD SORGULAMA                {Fore.CYAN}║")
                print(f"{Fore.CYAN}╚══════════════════════════════════════════════════╝")
                ad = input(f"{Fore.GREEN}Ad: {Style.RESET_ALL}")
                soyad = input(f"{Fore.GREEN}Soyad: {Style.RESET_ALL}")
                result = ad_soyad_sorgula(ad, soyad)
                print(f"\n{Fore.CYAN}Sonuç: {Fore.YELLOW}{result}")
                input(f"\n{Fore.GREEN}Devam etmek için bir tuşa basın...{Style.RESET_ALL}")

            elif secim == "2":
                clear_screen()
                print(f"{Fore.CYAN}╔══════════════════════════════════════════════════╗")
                print(f"{Fore.CYAN}║{Fore.YELLOW}        AD SOYAD İL İLÇE SORGULAMA           {Fore.CYAN}║")
                print(f"{Fore.CYAN}╚══════════════════════════════════════════════════╝")
                ad = input(f"{Fore.GREEN}Ad: {Style.RESET_ALL}")
                soyad = input(f"{Fore.GREEN}Soyad: {Style.RESET_ALL}")
                il = input(f"{Fore.GREEN}İl: {Style.RESET_ALL}")
                ilce = input(f"{Fore.GREEN}İlçe: {Style.RESET_ALL}")
                result = ad_soyad_il_ilce_sorgula(ad, soyad, il, ilce)
                print(f"\n{Fore.CYAN}Sonuç: {Fore.YELLOW}{result}")
                input(f"\n{Fore.GREEN}Devam etmek için bir tuşa basın...{Style.RESET_ALL}")

            elif secim == "3":
                clear_screen()
                print(f"{Fore.CYAN}╔══════════════════════════════════════════════════╗")
                print(f"{Fore.CYAN}║{Fore.YELLOW}             TC PRO SORGULAMA                {Fore.CYAN}║")
                print(f"{Fore.CYAN}╚══════════════════════════════════════════════════╝")
                tc = input(f"{Fore.GREEN}TC Kimlik No: {Style.RESET_ALL}")
                result = tc_pro_sorgula(tc)
                print(f"\n{Fore.CYAN}Sonuç: {Fore.YELLOW}{result}")
                input(f"\n{Fore.GREEN}Devam etmek için bir tuşa basın...{Style.RESET_ALL}")

            elif secim == "4":
                clear_screen()
                print(f"{Fore.CYAN}╔══════════════════════════════════════════════════╗")
                print(f"{Fore.CYAN}║{Fore.YELLOW}             GSM > TC SORGULAMA              {Fore.CYAN}║")
                print(f"{Fore.CYAN}╚══════════════════════════════════════════════════╝")
                gsm = input(f"{Fore.GREEN}GSM No: {Style.RESET_ALL}")
                result = gsm_tc_sorgula(gsm)
                print(f"\n{Fore.CYAN}Sonuç: {Fore.YELLOW}{result}")
                input(f"\n{Fore.GREEN}Devam etmek için bir tuşa basın...{Style.RESET_ALL}")

            elif secim == "5":
                clear_screen()
                print(f"{Fore.CYAN}╔══════════════════════════════════════════════════╗")
                print(f"{Fore.CYAN}║{Fore.YELLOW}             TC > GSM SORGULAMA              {Fore.CYAN}║")
                print(f"{Fore.CYAN}╚══════════════════════════════════════════════════╝")
                tc = input(f"{Fore.GREEN}TC Kimlik No: {Style.RESET_ALL}")
                result = tc_gsm_sorgula(tc)
                print(f"\n{Fore.CYAN}Sonuç: {Fore.YELLOW}{result}")
                input(f"\n{Fore.GREEN}Devam etmek için bir tuşa basın...{Style.RESET_ALL}")

            elif secim == "6":
                clear_screen()
                print(f"{Fore.CYAN}╔══════════════════════════════════════════════════╗")
                print(f"{Fore.CYAN}║{Fore.YELLOW}              TAPU SORGULAMA                {Fore.CYAN}║")
                print(f"{Fore.CYAN}╚══════════════════════════════════════════════════╝")
                tc = input(f"{Fore.GREEN}TC Kimlik No: {Style.RESET_ALL}")
                result = tapu_sorgula(tc)
                print(f"\n{Fore.CYAN}Sonuç: {Fore.YELLOW}{result}")
                input(f"\n{Fore.GREEN}Devam etmek için bir tuşa basın...{Style.RESET_ALL}")

            elif secim == "7":
                clear_screen()
                print(f"{Fore.CYAN}╔══════════════════════════════════════════════════╗")
                print(f"{Fore.CYAN}║{Fore.YELLOW}            OKUL NO SORGULAMA               {Fore.CYAN}║")
                print(f"{Fore.CYAN}╚══════════════════════════════════════════════════╝")
                tc = input(f"{Fore.GREEN}TC Kimlik No: {Style.RESET_ALL}")
                result = okul_no_sorgula(tc)
                print(f"\n{Fore.CYAN}Sonuç: {Fore.YELLOW}{result}")
                input(f"\n{Fore.GREEN}Devam etmek için bir tuşa basın...{Style.RESET_ALL}")

            elif secim == "8":
                clear_screen()
                print(f"{Fore.CYAN}╔══════════════════════════════════════════════════╗")
                print(f"{Fore.CYAN}║{Fore.YELLOW}          SGK YETKİLİ SORGULAMA             {Fore.CYAN}║")
                print(f"{Fore.CYAN}╚══════════════════════════════════════════════════╝")
                tc = input(f"{Fore.GREEN}TC Kimlik No: {Style.RESET_ALL}")
                result = sgk_yetkili_sorgula(tc)
                print(f"\n{Fore.CYAN}Sonuç: {Fore.YELLOW}{result}")
                input(f"\n{Fore.GREEN}Devam etmek için bir tuşa basın...{Style.RESET_ALL}")

            elif secim == "9":
                clear_screen()
                print(f"{Fore.CYAN}╔══════════════════════════════════════════════════╗")
                print(f"{Fore.CYAN}║{Fore.YELLOW}            İŞ YERİ SORGULAMA               {Fore.CYAN}║")
                print(f"{Fore.CYAN}╚══════════════════════════════════════════════════╝")
                tc = input(f"{Fore.GREEN}TC Kimlik No: {Style.RESET_ALL}")
                result = is_yeri_sorgula(tc)
                print(f"\n{Fore.CYAN}Sonuç: {Fore.YELLOW}{result}")
                input(f"\n{Fore.GREEN}Devam etmek için bir tuşa basın...{Style.RESET_ALL}")

            elif secim == "10":
                clear_screen()
                print(f"{Fore.CYAN}╔══════════════════════════════════════════════════╗")
                print(f"{Fore.CYAN}║{Fore.YELLOW}            ADRES SORGULAMA                 {Fore.CYAN}║")
                print(f"{Fore.CYAN}╚══════════════════════════════════════════════════╝")
                tc = input(f"{Fore.GREEN}TC Kimlik No: {Style.RESET_ALL}")
                result = adres_sorgula(tc)
                print(f"\n{Fore.CYAN}Sonuç: {Fore.YELLOW}{result}")
                input(f"\n{Fore.GREEN}Devam etmek için bir tuşa basın...{Style.RESET_ALL}")

            elif secim == "11":
                clear_screen()
                print(f"{Fore.CYAN}╔══════════════════════════════════════════════════╗")
                print(f"{Fore.CYAN}║{Fore.YELLOW}            AİLE SORGULAMA                  {Fore.CYAN}║")
                print(f"{Fore.CYAN}╚══════════════════════════════════════════════════╝")
                tc = input(f"{Fore.GREEN}TC Kimlik No: {Style.RESET_ALL}")
                result = aile_sorgula(tc)
                print(f"\n{Fore.CYAN}Sonuç: {Fore.YELLOW}{result}")
                input(f"\n{Fore.GREEN}Devam etmek için bir tuşa basın...{Style.RESET_ALL}")

            elif secim == "0":
                print(f"\n{Fore.YELLOW}Programdan çıkılıyor...{Style.RESET_ALL}")
                time.sleep(1)
                break

            else:
                print(f"\n{Fore.RED}Geçersiz seçim! Lütfen 0-11 arasında bir sayı girin.{Style.RESET_ALL}")
                time.sleep(1)

        except Exception as e:
            print(f"\n{Fore.RED}Bir hata oluştu: {e}{Style.RESET_ALL}")
            input(f"\n{Fore.GREEN}Devam etmek için bir tuşa basın...{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
