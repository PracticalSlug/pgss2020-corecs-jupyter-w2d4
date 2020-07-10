"""
The function below is used for decrypting the flag when the correct password is given,
however, it is quite dense and uses a function `zip` that I don't intend to cover in
this class. It exists here so that the actual flags can live in this Notebook but only
be viewed if the correct password is given.
Documentation: https://stackoverflow.com/questions/20557999/xor-python-text-encryption-decryption
"""
def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])



"""
Short demo of using the `str_xor` encode/decode function for the curious
"""
##################################################################################### DELETE PWS:
# * The key for str_xor is 'blah' in ASCII, but truly, it is just a number.
# * In ASCII ciphers, the "key" was the amount of shift in each letter.
#key = 'blah'
key = "my-super-secret-key"

# The string we're encrypting is 'hoop'
#secret = 'hoop'
secret = 'picoCTF{p4p4-wh1sk3y-11m4-t35t-f14g}'

print("Secret: " + secret)

# ciphertext is the resulting text after putting a secret string through a cipher
ciphertext = str_xor(secret, key)
ciphertext_bytes = bytearray()
ciphertext_bytes.extend(ciphertext.encode())

# For the ASCII cipher, we keep all shifting to the printable alphabet, but this
#   enciphering results in number that have no corresponding letter, number or symbol.
print("Encrypted: " + str(ciphertext_bytes))

# * plaintext should be the orginal secret string after deciphering the ciphertext
# * like ROT47, for str_xor, encoding and decoding are the same function with the 
#     same key
plaintext = str_xor(ciphertext, key)

print("Decrypted: " + plaintext)