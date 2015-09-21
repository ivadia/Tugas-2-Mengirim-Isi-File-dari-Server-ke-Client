#impor modul socket
import socket
 
#ukuran buffer ketika menerima pesan
SIZE = 1024
 
#membuat objek socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = raw_input("Masukkan IP Server: ")
server_port = input("Masukkan Port Server: ")
 
#koneksi server
s.connect((server_address,server_port))
 
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
s.close()
