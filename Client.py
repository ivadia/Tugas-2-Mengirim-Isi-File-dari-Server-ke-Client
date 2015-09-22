#impor modul socket
import socket
 
#ukuran buffer ketika menerima pesan
SIZE = 1024

try :
    #membuat objek socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except :
    print "Tidak dapat membuat socket..."
else :
    print "Socket berhasil dibuat..."
    while 1 :
        try :
            server_address = raw_input("Masukkan IP Server: ")
            server_port = input("Masukkan Port Server: ")

            #koneksi server
            s.connect((server_address,server_port))
        except :
            print "Error koneksi ke server..."
        else :
            print "Terhubung dengan server:", server_address, "pada port:", server_port
            while 1:
             pesan = raw_input("Pesan: ")
             if not pesan : break
 
             #mengirim pesan ke server
             s.send(pesan)
 
             #menerima pesan dari server
             try:
                 message = s.recv(SIZE)
                 print message
             except:
                 if not message : break
    #menutup socket
    s.close()
