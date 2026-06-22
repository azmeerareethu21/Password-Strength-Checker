import socket

def check_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((host, port))

    if result == 0:
        print(f"Port {port} is OPEN on {host}")
    else:
        print(f"Port {port} is CLOSED on {host}")

    s.close()

host = input("Enter host (e.g., localhost): ")
port = int(input("Enter port number: "))

check_port(host, port)