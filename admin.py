import mysql.connector
import numpy as np
import os

db = mysql.connector.connect(host="localhost", user="root", passwd="", database="gudang")
cursor = db.cursor()


class Administrator:
    def __init__(self, Barang, Jumlah):
        self.Barang = Barang
        self.Jumlah = Jumlah


class Toko(Administrator):
    def __init__(self, Barang, Jumlah, harga):
        super().__init__(Barang, Jumlah)
        self.harga = harga

    def stock(self):
        TBLUE = '\033[34;1m'
        sql = """SELECT nama FROM StockBarang where nama = %s"""
        cursor.execute(sql, [self.Barang])
        temp_bar = cursor.fetchall()
        bar = np.array(temp_bar, dtype=str)
        if self.Barang == bar:
            print("Maaf barang yang anda input sudah tersedia coba lagi")
            self.Barang = " "
            main()
        else:
            pass
        sql = """ INSERT INTO StockBarang (nama,jumlah,harga) VALUES(%s,%s,%s)"""
        cursor.execute(sql, [(self.Barang), (self.Jumlah), (self.harga)])
        db.commit()
        print("1 data berhasil ditambahkan")
        print(TBLUE + "====================================")
        pil = input("Apakah ingin kembali ke menu? Y/T\n:")
        if pil == 'Y' or pil == 'y':
            os.system('clear')
            main()
        elif pil == 'T' or pil == 'y':
            os.system('clear')
            exit()

    def deleteLine(self):
        TBLUE = '\033[34;1m'
        TYELLOW = '\033[33m'
        nama = input(TBLUE + "Masukan nama barang yang akan di hapus: ")
        sql = """DELETE FROM StockBarang WHERE nama = %s"""
        cursor.execute(sql, [nama])
        db.commit()
        print(TYELLOW + "1 data berhasil di hapus")
        pil = input(TBLUE + "Ingin balik ke menu lagi? Y/T\n:")
        if pil == 'Y' or pil == 'y':
            os.system('clear')
            main()
        elif pil == 'T' or pil == 't':
            exit()

    def getinfo(self):
        TBLUE = '\033[34;1m'
        TYELLOW = '\033[33m'
        sql = """SELECT *FROM StockBarang"""
        cursor.execute(sql)
        result = cursor.fetchall()
        print(TYELLOW)
        for hasil in result:
            print(hasil)
        print(TBLUE + "====================================")
        pil = input("Apakah Anda ingin Meng edit barang? Y/T\n:")
        if pil == 'Y':
            x = Toko('', '', '')
            x.deleteLine()
        elif pil == 'T':
            os.system('clear')
            return main()


def main():
    TBLUE = '\033[34;1m'
    TYELLOW = '\033[33m'
    TRESET = '\033[m'
    print(TBLUE + "====================================")
    print("Selamat Datang Admin Toko Bangunan\n")
    print("Menu \n1.Input Barang\n2.Edit Barang\n3.Exit")
    print("====================================")
    pil = int(input(TYELLOW + "pilihan : "))
    if pil == 1:
        a = int(input("berapa banyak barang yg di input? "))
        for i in range(a):
            print(TBLUE + "====================================")
            Barang = input(TYELLOW + "Barang : ")
            Jumlah = int(input("Jumlah : "))
            harga = float(input("Masukan Harga Perbarang : "))
            x = Toko(Barang, Jumlah, harga)
            x.stock()

    elif pil == 2:
        os.system('clear')
        print(TBLUE + "====================================")
        y = Toko('', '', '')
        y.getinfo()
    elif pil == 3:
        exit()