import random

welcome_message = "WELCOME TO PUMPPY GAMES"
pumppy_position = random.randint(1, 4)

print("*****************************")
print(f"** {welcome_message} **")
print("*****************************")

nama_user = input("Masukan nama kamu: ")

print(f'''
Hallo {nama_user}!!! Coba perhatikan Goa dibawah ini
|_| |_| |_| |_|     
''')

pilihan_user = int (input("Menurut kamu dimana PUMPPY berada? [1 / 2 / 3 / 4]: "))

if pilihan_user ==pumppy_position:
    print(f"SELAMAT {nama_user} KAMU MENANG! posisi PUMPPY ada di {pumppy_position} dan pilihanmu adalah goa nomor  {pilihan_user}")
else:
    print(f"KAMU KALAH! pumppy bukan berada disitu!, tapi ada di goa nomor {pumppy_position}. Sedangkan kamu memilih goa nomor {pilihan_user}")