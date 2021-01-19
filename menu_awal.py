import Flogin
import time
import os
import getpass

if __name__ == "__main__":
    TGREEN = '\033[32m'  # Green Text
    TRED = '\033[31;1;40m'
    TRESET = '\033[m'
    print(TGREEN + "============Selamat Datang============")
    pil = input("|Apakah Anda sudah memiliki akuny? Y/T|\n:")
    print("====================================")
    if pil == 'Y' or pil == 'y':
        pil2 = input("Login sebagai :\n1.Admin\n2.pembeli\n:")
        if pil2 == '1':
            time.sleep(1)
            os.system('clear')
            print("====================================")
            uid = input(TRED + "Masukan Username: ")
            pas = getpass.getpass(TRED + "Masukan Password: ")
            adm = Flogin.Admin(uid, pas)
            print(TRESET)
            os.system('clear')
            # os.system('clear')#clear terminal linux
            adm.Admauth()

        elif pil2 == '2':
            print("Please Wait...")
            time.sleep(1)
            os.system('clear')
            print("====================================")
            uid = input(TRED + "Masukan Username: ")
            pas = getpass.getpass(TRED + "Masukan Password: ")
            cus = Flogin.Customer(uid, pas)
            print(TRESET)
            os.system('clear')
            # os.system('clear')#clear terminal linux
            cus.login()
    elif pil == 'T' or pil == 't':
        print("Please Wait...")
        time.sleep(1)
        os.system('clear')
        print("====================================")
        uid = input(TRED + "Masukan Username: ")
        pas = getpass.getpass(TRED + "Masukan Password: ")
        cus = Flogin.Customer(uid, pas)
        os.system('clear')
        # os.system('clear')#clear terminal linux
        cus.regis()
