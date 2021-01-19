import mysql.connector
import numpy as np
import time
import os
db = mysql.connector.connect(host="localhost", user="root", passwd="", database="gudang")
cursor = db.cursor()

class Pembeli:
    def __init__ (self):
        pass
class Browse(Pembeli):
    def __init__(self):
        super().__init__()
        TPURPLE = '\033[35m'
        TBLUE = '\033[34m'
        print(TBLUE+"====================================")
        sql= """SELECT *FROM StockBarang"""
        cursor.execute(sql)
        result = cursor.fetchall()
        print(TPURPLE)
        for hasil in result:
            print(list(hasil))
        print(TBLUE+"====================================")
        pil = input(TPURPLE+"Apakah akan balik ke menu? Y/T\n:")
        if pil == 'Y' or pil == 'y':
            main_Customer()
        elif pil == 'T' or pil == 't':
            os.system('clear')
            main_Customer()
class Keranjang(Pembeli):
    totalHarga = 0
    Jumbar = 0
    Nama = ''
    def __init__(self):
        super().__init__()
    def pilih(self):
        TPURPLE = '\033[35m'
        TBLUE = '\033[34m'
        print(TBLUE+"====================================")
        banyak = int(input(TPURPLE+"Akan berapa banyak barang yang akan dibeli? "))
        for i in range (banyak):
            nama = input("Nama barang: ")
            jumbar = int(input("Jumlah barang: "))
            sql = """SELECT jumlah FROM StockBarang WHERE nama = %s"""
            cursor.execute(sql, [nama])
            temp_jum = cursor.fetchall()
            jum = np.array(temp_jum, dtype=int)
            if jum == 0:
                print("Maaf barang yang anda pilih sudah habis")
                print(TBLUE+"====================================")
                main_Customer()
            else:
                if jumbar > jum:
                    print("Maaf barang yang tersedia hanya ", jum)
                    time.sleep(1)
                    os.system('clear')
                    main_Customer()
                else:
                    sql ="""SELECT harga FROM StockBarang WHERE nama=%s"""
                    cursor.execute(sql,[nama])
                    result =cursor.fetchall()
                    harga = np.array(result,dtype=int)
                    TotalHarga = harga * jumbar
                    Keranjang.totalHarga += TotalHarga
                    Keranjang.Jumbar += jumbar
                    Keranjang.Nama = nama
                    print(Keranjang.totalHarga)
                    print(TPURPLE+"data sudah di masukan ke keranjang")
                    print(TBLUE+"====================================")
                    main_Customer()
            
            

class checkout(Pembeli):
    
    TBLUE = '\033[34m'
    def __init__(self, saldo):
        super().__init__()
        self.saldo = saldo
    def hitung (self):
        TPURPLE = '\033[35m'
        print(TPURPLE)
        if self.saldo < Keranjang.totalHarga:
            print("Maaf saldo anda kurang silahkan coba lagi")
            time.sleep(1)
            os.system('clear')
            main_Customer()
        else:
            hitung = self.saldo - Keranjang.totalHarga
            Keranjang.totalHarga = 0
            sql ="""UPDATE StockBarang SET jumlah = jumlah-%s WHERE nama = %s"""
            val = (Keranjang.Jumbar, Keranjang.Nama)
            cursor.execute(sql, val)
            db.commit()
            print(hitung)
            main_Customer()
        

    
def main_Customer():
    TPURPLE = '\033[35m'
    TBLUE = '\033[34m'
    print(TBLUE+"========= Selamat Datang di TB Berkah Jaya =========")
    print(TPURPLE+"Menu")
    pil = int(input("1. List Barang\n2. keranjang\n3. Checkout\n4. Exit\n:"))
    saldo = 0
    if pil == 1:
        os.system('clear')
        Browse()
    elif pil == 2:
        y = Keranjang()
        y.pilih()
    elif pil == 3:
        print(TBLUE+"====================================")
        bayar = input(TPURPLE+"Bayar Sekarang? Y/T\n: ")
        if bayar == 'Y' or bayar == 'y':
            uang = float(input("Masukan Jumlah Uang : "))
            print(TBLUE+"====================================")
            duid = checkout(uang)
            duid.hitung()
        elif bayar == 'T' or bayar == 'y':
            main_Customer()
        else:
            print("Masukan input yang valid!!")
            main_Customer()
    elif pil == 4:
        exit()
    else:
        print("Masukan input yang valid!!")