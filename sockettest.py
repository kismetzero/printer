
import socket

ESC = b"\x1b"
GS = b"\x1d"

RESET = ESC + b"\x40"

LF = b"\x0a"

LEFT = ESC + b'\x61\x00'
CENTER = ESC + b'\x61\x01'
RIGHT = ESC + b'\x61\x02'

MOVE_2 = ESC + b'\x64\x02'
MOVE_4 = ESC + b'\x64\x04'
MOVE_6 = ESC + b'\x64\x06'
CUT = GS + b'\x56\x01'

XP0001FIND = b'\x58\x50\x30\x30\x30\x31\x46\x49\x4e\x44'

xtest_qr0 =  b'\x1d\x28\x6b\x30\x67\x08' + \
            b'\x1d\x28\x6b\x30\x69\x30' + \
            b'\x1d\x28\x6b\x30\x80\x0c\x00' + \
            b'Hello World!' + \
            b'\x1d\x28\x6b\x30\x81'

xtest_qr1 =  b'\x1d\x28\x6b\x30\x67\x08' + \
            b'\x1d\x28\x6b\x30\x69\x30' + \
            b'\x1d\x28\x6b\x30\x80\x0c\x01' + \
            b'abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ==========0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ==========0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ==========abcdefghijklmnopqrstuvwxyz' + \
            b'\x1d\x28\x6b\x30\x81'

escpos_qr = b'\x1d\x28\x6b\x03\x00\x31\x43\x08' + \
            b'\x1d\x28\x6b\x03\x00\x31\x45\x30' + \
            b'\x1d\x28\x6b\x0f\x00\x31\x50\x30' + \
            b'Hello World!' + \
            b'\x1d\x28\x6b\x03\x00\x31\x51\x30'

def test1(s):
    s.sendall(b'\x1b\x76\x00')
    print(s.recv(32).hex())
    print(s.recv(32).hex()) # 期望：14 00 00 00；实际：00

def test2(s):
    s.sendall(b'\x10\x04\x02')
    print(s.recv(32).hex()) # 期望：12；实际：12

def test3(s):
    s.sendall(  RESET + b'ESC @ -- 1B 40' + LF + \
                    xtest_qr0 + MOVE_2 + \
                    b'====MOVE 2====' + MOVE_2 + b'====MOVE 4====' + MOVE_4 + b'====MOVE 6====' + MOVE_6 + b'====MOVE END====' + LF + \
                    LEFT + b'left' + LF + CENTER + b'center' + LF + RIGHT + b'right' + LF + \
                    MOVE_6 + CUT)

if __name__ == "__main__":
    s = socket.create_connection(('192.168.50.5', 9100), timeout=5)
    s.sendall(RESET + xtest_qr1 + MOVE_6 + CUT)
    s.close()

