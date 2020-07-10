import hashlib

### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
###############################################################################

# v-- this is the flag in encrypted form!
flag_enc = bytearray(b"\x11\x19\x0c\x08&1\'\x0b\x1fS\x15QL\x07\x07V\x16\x0eR\tBVT\x08U]\x1b\x0f\x17VR]\x0cQ\\\x01\x1c")



def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()



def level_3_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    user_pw_hash = hash_pw(user_pw)
    
    if( user_pw_hash == bytearray(b'\xc6&\xef\x0b{>\nRw\xabo\xbb\x9a\xaa\xfd_') ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")



level_3_pw_check()

### NOTE: You can make a new cell or put code below here to work with it.
### NOTE: You can comment out the `level_3_pw_check()` line viz. insert "#" at
###         beginning of line.

# The strings below are 7 possibilities for the correct password. 
#   (Only 1 is correct)
pos_pw_list = ["cortana", "maximus", "apogee", "astraeus", "xenophobia", "byzantine", "enkidu"]