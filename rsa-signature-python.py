"""
デジタル署名をPythonで実装する｜RSAで「改ざん」を見抜くしくみ

元記事: https://security.yurufuwa.work/learn/rsa-signature-python
ゆるふわサイバーセキュリティ (security.yurufuwa.work) の解説記事から抜粋したコードです。
"""

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

message = "Maru -> Bob: 契約Aを承認します".encode("utf-8")

signature = private_key.sign(
    message,
    padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
    hashes.SHA256(),
)
print("署名の長さ:", len(signature), "バイト")   # 256バイト

from cryptography.exceptions import InvalidSignature

def verify(pub, msg, sig):
    try:
        pub.verify(
            sig, msg,
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256(),
        )
        return True
    except InvalidSignature:
        return False

print(verify(public_key, message, signature))                       # True
print(verify(public_key, "Maru -> Bob: 契約Bを承認します".encode("utf-8"), signature))  # False
