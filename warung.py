from rich.console import Console
from rich.table import Table
from services import db
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def add():
    kode_barang = input('kode barang : ')
    nama_barang = input('nama barang : ')
    harga_barang = int(input('harga barang : '))
    stok_barang = int(input('stok barang : '))
    db.tambah_barang(kode_barang, nama_barang,harga_barang, stok_barang)

    
def check():
    items = db.lihat_semua_barang() 
    
    clear_screen()    
    console1 = Console()
    table = Table(title="Data Barang")
    
    table.add_column("id")
    table.add_column("Kode Barang")
    table.add_column("Nama")
    table.add_column("Harga")
    table.add_column("Stok")
    for item in items:
        id_barang = item[0]
        kode_barang = item[1]
        nama_barang = item[2] 
        harga_barang = item[3] 
        stok_barang = item[4]  
        table.add_row(str(id_barang),str(kode_barang), nama_barang, str(harga_barang), str(stok_barang))
    console1.print(table)



while True:
    clear_screen()    
    console1 = Console()
    table = Table(title="Selamat Datang di Warung Mini")
    table.add_column("Tombol")
    table.add_column("Action")
    table.add_row("c", "Tambah Barang")
    table.add_row("v", "Lihat Barang")
    table.add_row("q", "Quit")
    console1.print(table)

    pilih = input("Pilih: ")
    if pilih == "c":
        clear_screen()
        add()
        input("Tekan enter untuk kembali ke menu...")
    elif pilih == "v":
        clear_screen()
        check()
        input("Tekan enter untuk kembali ke menu...")
    elif pilih == "q":
        exit()