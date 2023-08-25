#List Data Pasien
data_pasien= [{'id':123,'nama':'Fajar Prasetyo',  'usia': 45, 'jenis_kelamin':'Pria', 'jenis_pelayanan':'Umum','alamat':'Jl. Bandung Raya N0. 112, Bandung, Indonesia', 'pekerjaan':'wiraswasta'},
{'id':124,'nama':'Bahrul Kurnia','usia': 33, 'jenis_kelamin':'Pria', 'jenis_pelayanan':'BPJS','alamat':'Jl. Rancaekek N0. 19, Ciamis, Indonesia', 'pekerjaan':'ASN'},
{'id':125,'nama':'Citra Pitaloka',  'usia': 54, 'jenis_kelamin':'Wanita', 'jenis_pelayanan':'Asuransi','alamat':'Jl. Bale Endah N0. 10, Tasikmalaya, Indonesia', 'pekerjaan':'Apoteker'},
{'id':126,'nama':'Arunika Lituayu', 'usia': 29, 'jenis_kelamin':'Wanita', 'jenis_pelayanan':'Umum','alamat':'Jl. Rahayu N0. 27, Cianjur, Indonesia', 'pekerjaan':'Programmer'},
{'id':127,'nama':'Bagas Hadinata',  'usia': 35, 'jenis_kelamin':'Pria', 'jenis_pelayanan':'BPJS','alamat':'Jl. Kabalen N0. 41, Bekasi, Indonesia', 'pekerjaan':'Data Scientist'}]

# Deklarasi Menu 1.1
def tampil(id = 0,sort='',reverse=False):
    if len(data_pasien) != 0:
        print("Daftar Pasien")
        print(f"Nomor | {'Nama':<20} | {'Usia':<5} | {'Jenis Kelamin':<15} | {'jenis Pelayanan':<20} | {'Alamat':<50} | {'Pekerjaan':<15}")
        if id == 0:
            if sort == '':
                for i in data_pasien:
                    print(f'{i["id"]:<5} | {i["nama"]:<20} | {i["usia"]:<5} | {i["jenis_kelamin"]:<15} | {i["jenis_pelayanan"]:<20} | {i["alamat"]:<50} | {i["pekerjaan"]:<15}')
                print()
            else :
                newList = sorted(data_pasien, key=lambda d: d[sort],reverse=reverse)
                for i in newList:
                    print(f'{i["id"]:<5} | {i["nama"]:<20} | {i["usia"]:<5} | {i["jenis_kelamin"]:<15} | {i["jenis_pelayanan"]:<20} | {i["alamat"]:<50} | {i["pekerjaan"]:<15}')
                print() 
        else :
            for i in data_pasien:
                if i["id"] == id:
                    print(f'{i["id"]:<5} | {i["nama"]:<20} | {i["usia"]:<5} | {i["jenis_kelamin"]:<15} | {i["jenis_pelayanan"]:<20} | {i["alamat"]:<50} | {i["pekerjaan"]:<15}')
            print()
            
    else :
        print("Data Pasien Tidak Ada")
#Deklarasi Menu 2.1 (List Untuk mencari data pasien, Update & Delete)
def filter_id(id,step='read'):
    data = list(filter(lambda i:i if i['id'] == id else '',data_pasien))
    if len(data) > 0:
        if step == 'edit':
            tampil(id)
            handleEdit(data)
        elif step == 'delete':
            tampil(id)
            handleDelete(data)
        elif step == 'read' :
            tampil(id)
    else:
        print(f"Data Pasien dengan nomor {id} Tidak Ada")
#Deklarasi Menu 3 (mengupdate Data Pasien)    
def handleEdit(data):
    index = data_pasien.index(data[0])
    check_input = True
    while check_input :
        edit = input(f"Apakah ingin mengupdate data dengan nomor pasien {data[0]['id']} (Ya/Tidak) : ")
        if edit.lower() == 'ya'    :
            check_input = False
            form_edit = True
            while form_edit:
                menu_edit = input('''
Pilih kolom yang ingin diupdate
1. Nama
2. Usia
3. Jenis Pelayanan
4. Alamat
5. Pekerjaan
6. Kembali Ke Menu Edit
Masukkan angka kolom yang ingin diupdate :''')
                if menu_edit == '1':
                    check_nama = True
                    while check_nama :
                        new_value = input("Masukkan Nama Pasien : ")
                        if len(new_value) != 0:
                            kata = new_value.split()
                            gabung = ''.join(kata)
                            if gabung.isalpha() == True:
                                check_nama = False
                            else:
                                print("masukan huruf saja!")
                        else:
                            print("Nama Harus diisi")
                    print(f"Update nama dari {data[0]['nama']} menjadi {new_value}")
                    check_edit = True
                    while check_edit:
                        check = input("Apakah ingin mengupdate data lain? (Ya/Tidak) : ")
                        if check.lower() == 'ya'   :
                            check_edit = False
                            data_pasien[index]['nama'] = new_value
                            print("Data Berhasil Di Update")
                            tampil(data_pasien[index]['id'])
                            check_more = True
                            while check_more:
                                more = input("Apakah ingin mengupdate data lain? (Ya/Tidak) :")
                                if more.lower() == 'ya'   :
                                    check_more = False
                                    form_edit = True
                                elif more.lower() == 'tidak'   :
                                    check_more = False
                                    form_edit = False    
                                else :
                                    print("Input Tidak Sesuai")
                        elif check.lower() == 'tidak' :
                            check_edit = False
                        else :
                            print("Input Tidak Sesuai")
                elif menu_edit == '2':
                    try:
                        new_value = int(input("Masukkan Usia Baru Pasien :"))
                        print(f"Update data dari {data[0]['usia']} menjadi {new_value}")
                        check_edit = True
                        while check_edit:
                            check = input("Apakah tetap ingin mengupdate data lain? (Ya/Tidak) : ")
                            if check.lower() == 'ya'   :
                                check_edit = False
                                data_pasien[index]['usia'] = new_value
                                print("Data Berhasil Di Update")
                                tampil(data_pasien[index]['id'])
                                check_more = True
                                while check_more:
                                    more = input("Apakah ingin mengupdate data lain? (Ya/Tidak) :")
                                    if more.lower() == 'ya'   :
                                        check_more = False
                                        form_edit = True
                                    elif more.lower() == 'tidak'   :
                                        check_more = False
                                        form_edit = False   
                                    else :
                                        print("Input Tidak Sesuai")
                            elif check.lower() == 'tidak' :
                                check_edit = False
                            else :
                                print("Input Tidak Sesuai")
                    except ValueError:
                        print('Masukkan Angka yang Benar')
                elif menu_edit == '3':
                    new_value = input("Masukkan Jaminan baru pasien :")
                    print(f"Update jaminan dari {data[0]['jenis_pelayanan']} menjadi {new_value}")
                    check_edit = True
                    while check_edit:
                        check = input("Apakah tetap ingin mengupdate data lain? (Ya/Tidak) : ")
                        if check.lower() == 'ya'   :
                            check_edit = False
                            data_pasien[index]['jenis Pelayanan'] = new_value
                            print("Data Berhasil Di Update")
                            tampil(data_pasien[index]['id'])
                            check_more = True
                            while check_more:
                                more = input("Apakah ingin mengupdate kolom lain? (Ya/Tidak) :")
                                if more.lower() == 'ya'   :
                                    check_more = False
                                    form_edit = True
                                elif more.lower() == 'tidak'   :
                                    check_more = False
                                    form_edit = False    
                                else :
                                    print("Input Tidak Sesuai")
                        elif check.lower() == 'tidak' :
                            check_edit = False
                        else :
                            print("Input Tidak Sesuai")
                elif menu_edit == '4':
                    new_value = input("Masukkan Alamat Baru Pasien :")
                    print(f"Update alamat dari  {data[0]['alamat']} menjadi {new_value}")
                    check_edit = True
                    while check_edit:
                        check = input("Apakah tetap ingin mengupdate data lain? (Ya/Tidak) : ")
                        if check.lower() == 'ya'   :
                            check_edit = False
                            data_pasien[index]['alamat'] = new_value
                            print("Data Berhasil Di Update")
                            tampil(data_pasien[index]['id'])
                            check_more = True
                            while check_more:
                                more = input("Apakah ingin mengupdate kolom lain? (Ya/Tidak) :")
                                if more.lower() == 'ya'   :
                                    check_more = False
                                    form_edit = True
                                elif more.lower() == 'tidak'   :
                                    check_more = False
                                    form_edit = False    
                                else :
                                    print("Input Tidak Sesuai")
                        elif check.lower() == 'tidak' :
                            check_edit = False
                        else :
                            print("Input Tidak Sesuai")
                elif menu_edit == '5':
                    new_value = input("Masukkan Pekerjaan Baru Pasien :")
                    print(f"Update pekerjaan dari  {data[0]['pekerjaan']} menjadi {new_value}")
                    check_edit = True
                    while check_edit:
                        check = input("Apakah tetap ingin mengupdate data lain? (Ya/Tidak) : ")
                        if check.lower() == 'ya'   :
                            check_edit = False
                            data_pasien[index]['pekerjaan'] = new_value
                            print("Data Berhasil Di Update")
                            tampil(data_pasien[index]['id'])
                            check_more = True
                            while check_more:
                                more = input("Apakah ingin mengupdate kolom lain? (Ya/Tidak) :")
                                if more.lower() == 'ya'   :
                                    check_more = False
                                    form_edit = True
                                elif more.lower() == 'tidak'   :
                                    check_more = False
                                    form_edit = False    
                                else :
                                    print("Input Tidak Sesuai")
                        elif check.lower() == 'tidak' :
                            check_edit = False
                        else :
                            print("Input Tidak Sesuai")
                elif menu_edit == '6' :
                    form_edit = False
                else :
                    print("Input Tidak Valid")
        elif edit.lower() == 'tidak' :
            check_input = False
        else :
            print("Input tidak valid")   
#Deklarasi Menu 4.1              
def handleDelete(data):
    check_hapus = True
    while check_hapus:
        check = input(f"Apakah yakin ingin menghapus data dengan nomor pasien {data[0]['id']}? (Ya/Tidak) : ")
        if check.lower() == 'ya':
            check_hapus = False
            data_pasien.remove(data[0])
            print("Data Pasien Berhasil Di Hapus")
            tampil()
        elif check.lower() == 'tidak':
            check_hapus = False
        else :
            print("Input Tidak Valid")
                        
#Main Menu
def main_menu():
    menu = input('''
Selamat Datang di Nels Hospital
1. Menampilkan Data Pasien
2. Menambahkan Data Pasien
3. Update Data Pasien
4. Menghapus Data Pasien 
5. Sorting Data Pasien
6. Exit 
Masukan Angka menu yang ingin anda operasikan: ''')
    
    if menu=='1':
        menu1()
    elif menu=='2':
        menu2()
    elif menu=='3':
        menu3()
    elif menu=='4':
        menu4()
    elif menu=='5':
        menu5()
    elif menu=='6':
        print("Terimakasih, Stay Healty ")
        exit()
    else:
        print('The option you entered is not Valid')
        main_menu()        
# 1.Menu Read
def menu1():
    menu = input('''
Menampilkan Data Pasien
1. Menampilkan Seluruh Data Pasien
2. Mencari Data Pasien (ID)
3. Kembali Ke Menu Utama
Masukkan angka Menu yang ingin dijalankan :''')    
    if menu == '1':
        tampil()
    elif menu== '2':
        try:
            id = int(input('Masukkan Nomor Pasien yang ingin dilihat : '))
            filter_id(id)
        except ValueError:
            print('Masukkan Angka yang Benar')
    elif menu== '3':
        main_menu()
    else:
        print('Menu Tidak Tersedia')
    menu1()   
# 2.Menu Create 
def menu2():
    menu= input('''
Menambah Data Pasien
1. Menambah Data Pasien
2. Kembali ke Menu Utama
Masukkan angka Menu yang ingin dijalankan :''')
    if menu == '1':
        print()
        try :
            masukan_nama = True
            while masukan_nama :
                add_nama = input("Masukkan Nama Pasien : ")
                add_nama= add_nama.title()
                if len(add_nama) != 0:
                    kata = add_nama.split()
                    gabung = ''.join(kata)
                    if gabung.isalpha() == True:
                        masukan_nama = False
                    else:
                        print("input hanya huruf saja")
                else:
                    print("Nama Harus diisi")
            masukan_usia = True
            while masukan_usia:
                try:
                    add_usia = int(input("Masukkan Usia Pasien : "))
                    if add_usia== int:
                        masukan_usia= True
                    break    
                except ValueError:
                    print('Input Harus Angka')
            check_gender = True
            while check_gender :
                add_gender = input("Masukkan Jenis Kelamin Pasien (Pria/Wanita) : ")
                if add_gender.lower() == 'pria' or add_gender.lower() == 'wanita'  :
                    check_gender= False
                else :
                    print("Jenis kelamin tidak sesuai")
            #tambah jenis pelayanan, alamat & Jenis Kelamin
            add_jenispelayanan= input("Masukkan Jenis Pelayanan yang digunakan (BPJS/Asuransi/Umum/Lainnya (Sebutkan)) : ")
            add_alamat = input("Masukkan Alamat Pasien : ")
            add_alamat = add_alamat.title()
            add_pekerjaan = input("Masukkan Pekerjaan Pasien : ")
            add_pekerjaan= add_pekerjaan.title()
            data_pasien.append({
                'id':data_pasien[len(data_pasien)-1]['id'] + 1 , 
                'nama':add_nama,
                'usia':add_usia,
                'jenis_kelamin':add_gender.capitalize(),
                'jenis_pelayanan':add_jenispelayanan,
                'alamat':add_alamat,
                'pekerjaan':add_pekerjaan,
                })    
            print("Data Pasien Berhasil Ditambahkan")
            tampil()
        except ValueError:
            print('Masukan sesuai perintah')    
    elif menu == '2':
        main_menu()
    else:
        print('Menu Tidak Tersedia')
    menu2()    
# 3.Menu Update
def menu3():
    menu = input('''
Mengupdate Data Pasien
1. Mengupdate Data Pasien
2. Kembali Ke Menu Utama
Masukkan angka Menu yang ingin dijalankan :''') 
    if menu == '1':
        try:
            tampil()
            id = int(input('Masukkan Nomor Pasien yang ingin diupdate : '))
            filter_id(id,'edit')
        except ValueError:
            print('Masukkan Angka yang Benar')
    elif menu == '2':
        main_menu()
    else:
        print('Menu Tidak Tersedia')
    menu3()  

# 4.Menu Delete
def menu4():
    menu = input('''
Menghapus Data Pasien
1. Menghapus Data Pasien
2. Kembali Ke Menu Awal
Masukkan angka Menu yang ingin dijalankan :''')    
    if menu == '1':
        try:
            tampil()
            id = int(input('Masukkan Nomor Pasien yang ingin dihapus : '))
            filter_id(id,'delete')
        except ValueError:
            print('Masukkan Angka yang Benar')
    elif menu == '2':
        main_menu()
    else:
        print('Menu Tidak Tersedia')
    menu4()
# 6.Menu Sorting data pasien         
def menu5():
    menu = input('''
Sorting Data Pasien Berdasarkan
1. Nama (A-Z)
2. Nama (Z-A)
3. Usia (Muda - Tua)
4. Usia (Tua - Muda)
5. Kembali Ke Menu Awal
Masukkan angka Menu yang ingin dijalankan :''')
    if menu == '1':
        tampil(0,'nama')
    elif menu == '2':
        tampil(0,'nama',True)
    elif menu == '3':
        tampil==(0,'usia')
    elif menu == '4':
        tampil(0,'usia',True)          
    elif menu == '5':
        main_menu()
    else:
        print('Menu Tidak Tersedia')
    menu5()
main_menu()