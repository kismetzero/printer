
from escpos.printer import Network

if __name__ == "__main__":
    p = Network("192.168.50.5", 9100, timeout=10)
    # p.text("Hello World!\n")
    # p.qr(content="abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ====================abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ====================abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ====================", native=True)
    p.image("1.png")
    p.cut()
    p.close()
