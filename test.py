import socket


def start_server():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('127.0.0.1', 4000))
        server.listen(4)
        while True:
            print('Сервер запущен')
            client_socket, address = server.accept()
            data = client_socket.recv(1024).decode('utf-8')
            print(data)
            content = get_request(data)
            client_socket.send(content)
            client_socket.shutdown(socket.SHUT_WR)
    except KeyboardInterrupt:
        server.close()
        print('Выключение сервера')


def get_request(request_data):
    HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    path = request_data.split(' ')[1]
    response = ''
    with open('server'+path, 'rb') as file:
        response = file.read()
    return HDRS.encode('utf-8') + response


start_server()
