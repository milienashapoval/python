alphabet = "abcdefghijklmnopqrstuvwxyz"
text = input("message:")
def encrypt(text,key):
    result = ""
    for i in range (len(text)):
        result += alphabet[(alphabet.index(text[i]) + key) % len(alphabet)]
    return result
encrypt_message = encrypt(text,3)
print(encrypt_message)



