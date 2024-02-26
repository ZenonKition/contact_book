import socket
import sys

HOST = 'localhost'
PORT = 10000
address = (HOST, PORT)
# создаем ТСР/IP сокет
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#b = open(book.txt, w)
# привязывваем сокет к порту
print(f'Старт сервера на {HOST} порт {PORT}')
s.bind(address)

# слушаем входящие подключения
s.listen(1)
book = open('contacts_book.txt', 'w')
while True:
    # ждём соединения
    print(" Ожидание соединения...")
    connection, client_address = s.accept()

    try:
        print('Подключение к: ', client_address)

        # принимаем данные порциями и ретранслируем их

        while True:
                # формируем и отправляем запрос на имя
                name_ans = 'Введите имя'
                name_ansver = name_ans.encode()
                connection.send(name_ansver)
                # получаем ответ
                name_r = connection.recv(60)
                print(f'Получено имя <{name_r.decode()}>')


                # формируем и отправляем запрос на номер
                number_ans = 'Введите номер'
                number_ansver = number_ans.encode()
                connection.send(number_ansver)
                # получаем ответ
                num_r = connection.recv(60)
                print(f'Получен номер <{num_r.decode()}>')

                # сообщение о следующих действиях
                mes = 'Записываем контакт...'
                connection.send(mes.encode())
                book.write(name_r.decode() + '-' + num_r.decode() + '\n')
                mes = 'Запись завершена успешно!'
                connection.send(mes.encode())

    finally:
        # очищаем соединение
        print('Сеанс связи завершен.')
        connection.close()