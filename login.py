from rich.console import Console
from rich.table import Table
from services import db
import warung
import time

def login():
    while True:
        name = input("Masukkan username: ")
        password = input("Masukkan password: ")
        result = db.login_user(name, password)
        if result:
            print("Login Berhasil")
            warung.main_menu()
            break
        else:
            print("Login Gagal")
            time.sleep(1)
            warung.clear_screen()
            



def register():
    username = input("Masukkan username : ")
    password = input("Masukkan password : ")
    db.register_user(username, password)


while True:
    warung.clear_screen()    
    console = Console()
    table = Table(title="Selamat Datang Silahkan Login")
    table.add_column("Tombol")
    table.add_column("Action")
    table.add_row("1", "Admin")
    table.add_row("2", "User")
    table.add_row("3", "Register")
    console.print(table)        
    
    pilihan = int(input("pilih menu : "))

    if pilihan == 1:
        pass
    elif pilihan == 2:
        login()
    elif pilihan == 3:
        register()
    else:
        print("Menu Tidak Tersedia")

        
        



