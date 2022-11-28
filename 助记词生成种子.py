import hashlib
import binascii
mnemonicSentence = b'patch purpose fat march slow tiny quarter age spring orphan twin wish'  #助记词
passphrase = b'mnemonic'+b''	#passphrase,mneonic为默认，passphrase 填入后面 b''
seed = hashlib.pbkdf2_hmac('sha512', mnemonicSentence, passphrase, 2048,64)		#把助记词 + passphrase 用pbkdf2 用 sha512 2048 次后得出一个128位hex
print(binascii.hexlify(seed))
