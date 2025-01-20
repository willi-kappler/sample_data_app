import segno
import random
import time
import base64

if __name__ == "__main__":
    t1: bytes = int(time.time()).to_bytes(5, byteorder="big")
    t2: str = base64.b32hexencode(t1).decode("utf-8")

    b1: bytes = random.randbytes(40)
    b2: str = base64.b32hexencode(b1).decode("utf-8")

    data = f"TERRA_{t2}_{b2}"
    qrcode = segno.make_qr(data, error="H")
    qrcode.save(f"{data}.png", scale=5)

