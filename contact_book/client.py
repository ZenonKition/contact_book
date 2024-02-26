import socket
import sys

# создаем TCP/IP сокет
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# подключаем сокет к порту, через который прослушивается сервер
server_address = ('localhost', 10000)
print('Прдключено к {} порт {}'.format(*server_address))
s.connect(server_address)
i = True
try:
    print('Производим запись контактов')
    while i:

        # получаем запрос:
        ans_name = s.recv(60)
        ansver_name = ans_name.decode()
        print(ansver_name)

        # отвечаем на запрос:
        name = input()
        s.send(name.encode())

        # получаем следубший запрос:
        ans_num = s.recv(60)
        ansver_num = ans_num.decode()
        print(ansver_num)

        # отвечаем на запрос:
        num = input()
        s.send(num.encode())

        mes = s.recv(60)
        print(mes.decode())
        mes = s.recv(60)
        print(mes.decode())

        # data = s.recv(1024)
        # print(data.decode())
        # d = input()
        # dd = d.encode()
        # s.sendall(dd)
        print('Еще номерок? (да - жми Enter. нет - введи что-нибудь и жми Enter)')
        x = input()
        if x == '':
            i = True
        else:
            i = False

finally:
    print("Закрываем сокет")
    s.close()