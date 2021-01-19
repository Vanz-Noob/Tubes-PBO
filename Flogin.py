import time
from admin import main
from mainUser import main_Customer
import os


#induk kelas
class User:
    error = None
    def __init__(self, uid, passw):
        self.uid = uid
        self.passw = passw
        User.error = "Enter a valid user id and password"
#anak kelas admin
class Admin(User):
    def __init__(self, uid, passw):
        super().__init__(uid, passw)
    def Admauth(self):
        if (self.uid == 'admin' and self.passw == 'admin'):
            print ("Login successful")
            print ("Please Wait...")
            time.sleep(1)
            os.system('clear')
            main()
        else:
            print (User.error)
#anak kelas customer
class Customer(User):
    def __init__(self, uid, passw):
        super().__init__(uid, passw)
    def login(self):
        self.passw = self.passw+'\n';
        cek = False
        file = open("user.txt",'r')
        x = 1;
        for i in file:
            search = i.split(",")
            if ((search[0] == self.uid) and (search[1] == self.passw)):
                cek = True
                break
        if (cek):
            print ("Login successful")
            print ("Please Wait...")
            time.sleep(1)
            os.system('clear')
            main_Customer()
        else:
            print("Salah")
            exit()
        file.close()
    def regis(self):
        file = open("user.txt","a")
        file.write(self.uid+","+self.passw+'\n')
        file.close()
        print ("Login successful")
        print ("Please Wait...")
        time.sleep(1)
        os.system('clear')
        main_Customer()