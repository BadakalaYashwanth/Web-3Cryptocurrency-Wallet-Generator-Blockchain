# wallet.py

import os
import binascii
from ecdsa import SigningKey, SECP256k1

class Wallet:
    def __init__(self):
        self.private_key = SigningKey.generate(curve=SECP256k1)
        self.public_key = self.private_key.get_verifying_key()

    def sign_transaction(self, transaction):
        transaction_data = f"{transaction['sender']}{transaction['recipient']}{transaction['amount']}".encode()
        return binascii.hexlify(self.private_key.sign(transaction_data)).decode()

    def get_address(self):
        return binascii.hexlify(self.public_key.to_string()).decode()

    @staticmethod
    def validate_transaction(transaction, signature, public_key):
        verifying_key = SigningKey.from_string(binascii.unhexlify(public_key), curve=SECP256k1).get_verifying_key()
        transaction_data = f"{transaction['sender']}{transaction['recipient']}{transaction['amount']}".encode()
        return verifying_key.verify(binascii.unhexlify(signature), transaction_data)
