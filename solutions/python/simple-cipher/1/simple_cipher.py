import secrets
class Cipher:
    def __init__(self, key=None):
        if key is not None:
            self.key = key
        else:
            self.key = "".join([chr(ord("a") + secrets.randbelow(26)) for x in range(100)])

    def encode(self, plaintext):
        result = []
        for i in range(len(plaintext)):
            position = ord(plaintext[i]) - ord('a')
            keyposition = ord(self.key[i % len(self.key)]) - ord('a')
            new_position = (position + keyposition) % 26
            result.append(chr(new_position + ord('a')))
        return "".join(result)
    def decode(self, text):
        result = []
        for i in range(len(text)):
            position = ord(text[i]) - ord('a')
            keyposition = ord(self.key[i % len(self.key)]) - ord('a')
            new_position = (position - keyposition) % 26
            result.append(chr(new_position + ord('a')))
        return "".join(result)
