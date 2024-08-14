import mysql.connector
import time

db = mysql.connector.connect(
    host = 'localhost', 
    user = 'root',
    password = '',
    database = 'mini_market'
)

def tambah_barang(kode_barang,nama_barang,harga_barang,stok_barang):
    cursor = db.cursor()
    cursor.execute("INSERT INTO tbl_barang(kode_barang, nama_barang, harga_barang, stok_barang) VALUES(%s, %s, %s, %s)",(kode_barang,nama_barang,harga_barang,stok_barang))
    db.commit()
    if cursor.rowcount > 0 :
        print ("data berhasil dimasukkan")
    else:
        print ("data gagal dimasukkan")

def lihat_semua_barang():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tbl_barang")
    return cursor.fetchall()
    
def update_barang(kode_barang, nama_barang, harga_barang, stok_barang,id):
    cursor = db.cursor()
    cursor.execute("UPDATE tbl_barang SET kode_barang=%s, nama_barang=%s, harga_barang=%s, stok_barang=%s WHERE id=%s",(kode_barang,nama_barang, harga_barang, stok_barang,id))
    db.commit()
    if cursor.rowcount > 0 :
        print ("data berhasil diupdate")
        time.sleep(1)
    else:
        print ("data gagal diupdate")

def delete_barang(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM tbl_barang WHERE id=%s",(id,))
    db.commit()
    if cursor.rowcount > 0 :
        print ("data berhasil dihapus")
        time.sleep(1)
    else:
        print ("data gagal dihapus")
        
        
def register_user(name,password):
    cursor = db.cursor()
    cursor.execute("INSERT INTO tbl_user(name, password) VALUES(%s,%s)",(name,password))
    db.commit()
    if cursor.rowcount > 0 :
        print("Register Berhasil")
    else:
        print("Register Gagal")

def login_user(name, password):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tbl_user WHERE name=%s AND password=%s",(name,password))
    result = cursor.fetchone()
    return result is not None