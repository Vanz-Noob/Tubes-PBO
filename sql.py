import mysql.connector

#db = mysql.connector.connect(host="localhost", user="root", passwd="", database="gudang")
#if db.is_connected():
#    print("Hello World")
#cursor = db.cursor()
#cursor.execute("CREATE DATABASE gudang")
#print("database berasil")
#sql = """CREATE TABLE StockBarang(
#    nama VARCHAR(100) PRIMARY KEY,
#    jumlah INT,
#    harga FLOAT
#    )"""
#cursor.execute(sql)
#nama = input("Masukna nama barang: ")
#jumlah = int(input("Masukan jumlah barang: "))
#harga = float(input("Masukan harga barang: "))
#sql =""" INSERT INTO StockBarang (nama,jumlah,harga) VALUES(%s,%s,%s)"""
#cursor.execute(sql,[(nama),(jumlah),(harga)])
#db.commit()
#print("1 data berhasil ditambahkan")\
#nama = input("Masukan nama barang: ")
#sql ="""SELECT harga FROM StockBarang WHERE nama=%s"""
#cursor.execute(sql,[nama])
#result =cursor.fetchall()
#for hasil in result:
#    y = list(hasil)
#    z=y[0]-float(100)
#    print(z)

sql = """CREATE TABLE Keranjang(
nama VARCHAR(100) PRIMARY KEY,
jumlah INT
)"""
cursor.execute(sql)
print("tabel berhasil di buat")