#impor modul socket
import socket
 
#ukuran buffer ketika menerima pesan
SIZE = 1024
 
#membuat objek socket
try :
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except :
    print "Tidak dapat membuat socket..."
else :
    print "Socket berhasil dibuat..."
    while 1 :    

    #bind ke alamat dan port server
        try :
            server_port = input("Masukkan Port: ")
            s.bind(('localhost',server_port))
        except :
            print "Proses bind tidak berhasil..."
        else :
            print "Proses bind berhasil..."
            #mendengarkan koneksi dari client
            s.listen(50)
        
            #siap menerima pesan terus-menerus dari client
            while 1 :
             print "Menunggu koneksi pada port :", server_port
 
             #menerima koneksi dari client
             client, client_address = s.accept()
 
             print "Terhubung dengan client : ", client_address
 
             while 1 :
             #menerima pesan dari client
                 try:
                     message = client.recv(SIZE)
                     print message
                     if(message == "0"):
                         balasan = "Daftar File:\n 1. A.txt\n 2. B.txt"
                         client.send(balasan)
                         try :
                             pilihan = client.recv(SIZE)
                             if(pilihan == "1") :
                                 f = open('A.txt','r')
                                 isifile = f.read()
                                 client.send(isifile)
                             elif(pilihan == "2") :
                                 f = open('B.txt','r')
                                 isifile = f.read()
                                 client.send(isifile)
                             else :
                                 kirim = "Tidak ada dalam daftar pilihan!"
                                 client.send(kirim)
                         except :
                             if not pilihan: break
                     else :
                         balasan = "Pesan terkirim!"
                         client.send(balasan)
                 except :
                     #jika tidak ada pesan, keluar dari while
                     if not message: break
          
             #menutup client
             client.close()
 
            #menutup socket
            s.close()
            
        #menutup koneksi server
        print "Masukkan nomor port yang lain"
